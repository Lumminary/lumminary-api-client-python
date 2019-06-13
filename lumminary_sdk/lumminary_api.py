from __future__ import absolute_import
import re
import six
import six.moves.urllib as urllib
import base64
import json
from Crypto.Cipher import AES
from Crypto.Random import get_random_bytes

from lumminary_sdk import LumminaryAPISpecApi as LumminaryApiGenerated

class LumminaryApi(LumminaryApiGenerated):
    CWL_IV_SIZE_BYTES = 12
    CWL_MAC_SIZE_BYTES = 12

    def __init__(self, credentials):
        self._credentials = credentials

        authenticatedJwt = self._authenticate()

        LumminaryApiGenerated.__init__(self)

        self.api_client.configuration.api_key["Authorization"] = "Bearer {0}".format(authenticatedJwt)
        if self._credentials.host is not None:
            self.api_client.configuration.host = self._credentials.host

    def _authenticate(self):
        authApiInstance = LumminaryApiGenerated()
        if self._credentials.host is not None:
            authApiInstance.api_client.configuration.host = self._credentials.host

        authResponse = authApiInstance.post_jwt_auth(
            username= self._credentials.login,
            password = self._credentials.api_key,
            role = self._credentials.role
        )

        return authResponse.access_token

    def get_credentials(self):
        return self._credentials
    
    def post_client_snp_group(self, client_id, dataset_id, snps, **kwargs):
        snpsEncoded = json.dumps({
            "snps": snps
        })

        return self.post_client_snp_group(client_id, dataset_id, snpsEncoded, **kwargs)

    def authorization_metadata(self, authorizationUuid):
        authorization = self.get_product_authorization(product_id = self._credentials.login, authorization_id = authorizationUuid)

        authorizationMetadata = {
            "customer": authorization.client_uuid,
            "product": authorization.product_uuid,
            "authorization": authorization.authorization_uuid,
            "created_timestamp_utc": authorization.create_timestamp
        }

        if hasattr(authorization.scopes, "dataset"):
            authorizationMetadata["dataset"] = authorization.scopes.dataset
        if hasattr(authorization.scopes, "email"):
            authorizationMetadata["customer_email"] = authorization.scopes.email
        if hasattr(authorization.scopes, "name"):
            authorizationMetadata["customer_name"] = {
                "first_name": authorization.scopes.name.first_name,
                "last_name": authorization.scopes.name.last_name
            }
        if hasattr(authorization.scopes, "address"):
            authorizationMetadata["customer_address"] = {
                "city": authorization.scopes.address.city,
                "country": authorization.scopes.address.country,
                "address1": authorization.scopes.address.address1,
                "address2": authorization.scopes.address.address2,
                "zipcode": authorization.scopes.address.zipcode,
                "state": authorization.scopes.address.state
            }
        if hasattr(authorization.scopes, "sex"):
            authorizationMetadata["customer_sex"] = authorization.scopes.sex
        
        return authorizationMetadata

    def authorization_dna_data(self, authorizationUuid):
        authorization = self.get_product_authorization(product_id = self._credentials.login, authorization_id = authorizationUuid)

        if hasattr(authorization.scopes, "dataset"):
            datasetSnps = self.get_client_snp_group(authorization.client_uuid, authorization.scopes.dataset)

            snpRows = []
            snpRows.append("# rsid\tchromosome\tposition\tgenotype")
            for snp in datasetSnps:
                chromosome = LumminaryApi.chromosome_common_symbol(snp.chromosome_accession)

                snpRows.append(
                    "\t".join([snp.snp_id, chromosome, str(snp.location), "".join(snp.genotyped_alleles)])
                )

            return snpRows

        return None

    @classmethod
    def cwl_url_query_extract(cls, callbackUrl, partnerEncryptionKey, jsonDecodePayload = True):
        callbackUrl = urllib.parse.urlparse(callbackUrl)
        callbackQueryParams = dict(urllib.parse.parse_qsl(callbackUrl.query))

        paramsDecrypted = {}
        for qsKey, qsValueEncrypted in callbackQueryParams.items():
            valueDecrypted = cls.cwl_decrypt(qsValueEncrypted, partnerEncryptionKey)

            if jsonDecodePayload:
                paramsDecrypted[qsKey] = json.loads(valueDecrypted)
            else:
                paramsDecrypted[qsKey] = valueDecrypted

        return paramsDecrypted

    @classmethod
    def cwl_decrypt(cls, encryptedData, partnerEncryptionKey):
        partnerEncryptionKey = base64.b64decode(partnerEncryptionKey)

        encryptedData = base64.b64decode(encryptedData)
        iv = encryptedData[:LumminaryApi.CWL_IV_SIZE_BYTES]
        mac = encryptedData[-1 * LumminaryApi.CWL_MAC_SIZE_BYTES:]
        ciphertext = encryptedData[LumminaryApi.CWL_IV_SIZE_BYTES : -1 * LumminaryApi.CWL_MAC_SIZE_BYTES]

        cipher = AES.new(partnerEncryptionKey, AES.MODE_GCM, nonce=iv, mac_len=LumminaryApi.CWL_MAC_SIZE_BYTES)
        plaintext = cipher.decrypt_and_verify(ciphertext, mac)

        plaintextData = json.loads(plaintext.decode("utf-8"))

        return plaintextData

    @classmethod
    def cwl_encrypt(cls, decryptedData, partnerEncryptionKey):
        partnerEncryptionKey = base64.b64decode(partnerEncryptionKey)
        nonce = get_random_bytes(LumminaryApi.CWL_IV_SIZE_BYTES)
        cipher = AES.new(partnerEncryptionKey, AES.MODE_GCM, nonce=nonce, mac_len=LumminaryApi.CWL_MAC_SIZE_BYTES)

        ciphertext, tag = cipher.encrypt_and_digest(decryptedData)

        objEncryptedData = {
            "nonce": nonce,
            "ciphertext": ciphertext,
            "tag": tag
        }

        return objEncryptedData

    @classmethod
    def cwl_data_request_build(cls, dataRequest, partnerEncryptionKey, jsonEncodePayload = True):
        if jsonEncodePayload:
            dataRequest = json.dumps(dataRequest)

        objPayloadEncrypted = cls.cwl_encrypt(str.encode(json.dumps(dataRequest)), partnerEncryptionKey)

        payloadEncoded = base64.b64encode(objPayloadEncrypted["nonce"] + objPayloadEncrypted["ciphertext"] + objPayloadEncrypted["tag"])

        return urllib.parse.quote(payloadEncoded)

    @classmethod
    def chromosome_common_symbol(cls, chromosomeAccession):
        accessionNumberExtract = "NC_[0]+(.*)"
        accessionExtracted = re.search(pattern=accessionNumberExtract, string=chromosomeAccession)
        accessionNumber = int(accessionExtracted.group(1))

        if accessionNumber < 23:
            return str(accessionNumber)
        elif accessionNumber == 24:
            return "Y"
        elif accessionNumber == 23:
            return "X"
        elif accessionNumber == 12920:
            return "MT"
        else:
            raise ValueError(
                "Invalid chromosome accession {0}. Expecting the accession to be formatted like {1}".format(
                    chromosomeAccession,
                    accessionNumberExtract
                )
            )




