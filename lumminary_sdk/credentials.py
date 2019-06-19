import os
import json

class Credentials:
    ROLE_PRODUCT = "role_product"

    def __init__(self, product_uuid = None, api_key = None, api_host = None, role = None):
        """
        The explicit parameters passed here override anything that would be loaded from a config file
        """

        if role is None:
            role = Credentials.ROLE_PRODUCT

        self.product_uuid = product_uuid
        self.api_key = api_key
        self.api_host = api_host
        self.role = role

    def load_json_credentials(self, credentialsFilePath):
        with open(credentialsFilePath, "r") as credentialsFile:
            config = json.load(credentialsFile)

        credentialsExpected = ["product_uuid", "api_key", "role", "api_host"]
        for credentialsAttribute in credentialsExpected:
            if credentialsAttribute in config:
                setattr(self, credentialsAttribute, config[credentialsAttribute])
            else:
                if getattr(self, credentialsAttribute, None) is None:
                    raise ValueError("Expecting config attribute {0} to be either explicitly defined or present in config file. None found".format(
                        credentialsAttribute
                    ))
 