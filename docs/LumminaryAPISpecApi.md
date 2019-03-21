# lumminary_sdk.LumminaryAPISpecApi

All URIs are relative to *https://api.lumminary.com/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_authorizations_queue**](LumminaryAPISpecApi.md#get_authorizations_queue) | **GET** /products/{productId}/authorizations | 
[**get_client_gene**](LumminaryAPISpecApi.md#get_client_gene) | **GET** /clients/{clientId}/datasets/{datasetId}/genes/{geneSymbol} | Get gene by symbol
[**get_client_snp**](LumminaryAPISpecApi.md#get_client_snp) | **GET** /clients/{clientId}/datasets/{datasetId}/snps/{snpId} | Get SNP information
[**get_client_snp_group**](LumminaryAPISpecApi.md#get_client_snp_group) | **GET** /clients/{clientId}/datasets/{datasetId}/snps/ | 
[**get_gene**](LumminaryAPISpecApi.md#get_gene) | **GET** /reference/genes/databases/{databaseName}/accessions/{accession} | Generic gene information
[**get_product**](LumminaryAPISpecApi.md#get_product) | **GET** /products/{productId} | Get product details
[**get_product_authorization**](LumminaryAPISpecApi.md#get_product_authorization) | **GET** /products/{productId}/authorizations/{authorizationId} | 
[**get_reference_chromosome**](LumminaryAPISpecApi.md#get_reference_chromosome) | **GET** /reference/genomes/{genomeBuildAccession}/chromosomes/{chromosomeAccession} | Sequence for a region of the reference genome
[**get_reference_genome**](LumminaryAPISpecApi.md#get_reference_genome) | **GET** /reference/genomes/{genomeBuildAccession}/chromosomes | Reference genome metadata
[**get_reference_genomes_group**](LumminaryAPISpecApi.md#get_reference_genomes_group) | **GET** /reference/genomes/ | Reference genome builds
[**get_reference_snp**](LumminaryAPISpecApi.md#get_reference_snp) | **GET** /reference/snps/{snpAccession} | Reference SNP data
[**post_authorization_result_credentials**](LumminaryAPISpecApi.md#post_authorization_result_credentials) | **POST** /products/{productId}/authorizations/{authorizationId}/credentials | Provide a result for the authorization
[**post_authorization_result_file**](LumminaryAPISpecApi.md#post_authorization_result_file) | **POST** /products/{productId}/authorizations/{authorizationId}/file | Provide a file result to the authorization, e
[**post_client_snp_group**](LumminaryAPISpecApi.md#post_client_snp_group) | **POST** /clients/{clientId}/datasets/{datasetId}/snps/ | Get a large group of SNPs
[**post_jwt_auth**](LumminaryAPISpecApi.md#post_jwt_auth) | **POST** /auth/jwt | General-purpose authentication
[**post_product_authorization**](LumminaryAPISpecApi.md#post_product_authorization) | **POST** /products/{productId}/authorizations/{authorizationId} | Signal that processing is complete, without uploading any result
[**post_product_authorization_unfulfillable**](LumminaryAPISpecApi.md#post_product_authorization_unfulfillable) | **POST** /products/{productId}/authorizations/{authorizationId}/unfulfillable | Catch-all Authorization state, for authorizations that passed all verifications and should reach the partner Product, but cannot be fulfilled for various reasons


# **get_authorizations_queue**
> list[Authorization] get_authorizations_queue(product_id, seq_num_start=seq_num_start, x_fields=x_fields)



### Example
```python
from __future__ import print_function
import time
import lumminary_sdk
from lumminary_sdk.rest import ApiException
from pprint import pprint

# Configure API key authorization: Bearer
configuration = lumminary_sdk.Configuration()
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# create an instance of the API class
api_instance = lumminary_sdk.LumminaryAPISpecApi(lumminary_sdk.ApiClient(configuration))
product_id = 'product_id_example' # str | The UUID of the product
seq_num_start = 'seq_num_start_example' # str | The first sequence number from which to fetch (the sequence number of the last processed authorization) (optional)
x_fields = 'x_fields_example' # str | An optional fields mask (optional)

try:
    api_response = api_instance.get_authorizations_queue(product_id, seq_num_start=seq_num_start, x_fields=x_fields)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling LumminaryAPISpecApi->get_authorizations_queue: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **product_id** | **str**| The UUID of the product | 
 **seq_num_start** | **str**| The first sequence number from which to fetch (the sequence number of the last processed authorization) | [optional] 
 **x_fields** | **str**| An optional fields mask | [optional] 

### Return type

[**list[Authorization]**](Authorization.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_client_gene**
> ClientGene get_client_gene(client_id, dataset_id, gene_symbol, x_fields=x_fields)

Get gene by symbol

Gets A gene by its symbol, which can be found by querying the reference/ resource.  Will return a 404 if a gene exists as a reference, but its genomic coordinates intersect no SNPs in the dataset

### Example
```python
from __future__ import print_function
import time
import lumminary_sdk
from lumminary_sdk.rest import ApiException
from pprint import pprint

# Configure API key authorization: Bearer
configuration = lumminary_sdk.Configuration()
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# create an instance of the API class
api_instance = lumminary_sdk.LumminaryAPISpecApi(lumminary_sdk.ApiClient(configuration))
client_id = 'client_id_example' # str | The UUID of the client
dataset_id = 'dataset_id_example' # str | The UUID of one of the client's dataset
gene_symbol = 'gene_symbol_example' # str | The symbol of a gene to be fetched
x_fields = 'x_fields_example' # str | An optional fields mask (optional)

try:
    # Get gene by symbol
    api_response = api_instance.get_client_gene(client_id, dataset_id, gene_symbol, x_fields=x_fields)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling LumminaryAPISpecApi->get_client_gene: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **client_id** | **str**| The UUID of the client | 
 **dataset_id** | **str**| The UUID of one of the client&#39;s dataset | 
 **gene_symbol** | **str**| The symbol of a gene to be fetched | 
 **x_fields** | **str**| An optional fields mask | [optional] 

### Return type

[**ClientGene**](ClientGene.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_client_snp**
> ClientSNP get_client_snp(client_id, dataset_id, snp_id, x_fields=x_fields)

Get SNP information

Gets SNP information, as provided by the dataset.  If fetching this as an product, the client must have already granted access to the snip (see the 'products' group)

### Example
```python
from __future__ import print_function
import time
import lumminary_sdk
from lumminary_sdk.rest import ApiException
from pprint import pprint

# Configure API key authorization: Bearer
configuration = lumminary_sdk.Configuration()
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# create an instance of the API class
api_instance = lumminary_sdk.LumminaryAPISpecApi(lumminary_sdk.ApiClient(configuration))
client_id = 'client_id_example' # str | The UUID of the client
dataset_id = 'dataset_id_example' # str | The UUID of one of the client's dataset
snp_id = 'snp_id_example' # str | The rsId of a SNP to be fetched
x_fields = 'x_fields_example' # str | An optional fields mask (optional)

try:
    # Get SNP information
    api_response = api_instance.get_client_snp(client_id, dataset_id, snp_id, x_fields=x_fields)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling LumminaryAPISpecApi->get_client_snp: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **client_id** | **str**| The UUID of the client | 
 **dataset_id** | **str**| The UUID of one of the client&#39;s dataset | 
 **snp_id** | **str**| The rsId of a SNP to be fetched | 
 **x_fields** | **str**| An optional fields mask | [optional] 

### Return type

[**ClientSNP**](ClientSNP.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_client_snp_group**
> list[ClientSNP] get_client_snp_group(client_id, dataset_id, x_fields=x_fields)



### Example
```python
from __future__ import print_function
import time
import lumminary_sdk
from lumminary_sdk.rest import ApiException
from pprint import pprint

# Configure API key authorization: Bearer
configuration = lumminary_sdk.Configuration()
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# create an instance of the API class
api_instance = lumminary_sdk.LumminaryAPISpecApi(lumminary_sdk.ApiClient(configuration))
client_id = 'client_id_example' # str | The UUID of the client
dataset_id = 'dataset_id_example' # str | The UUID of one of the client's dataset
x_fields = 'x_fields_example' # str | An optional fields mask (optional)

try:
    api_response = api_instance.get_client_snp_group(client_id, dataset_id, x_fields=x_fields)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling LumminaryAPISpecApi->get_client_snp_group: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **client_id** | **str**| The UUID of the client | 
 **dataset_id** | **str**| The UUID of one of the client&#39;s dataset | 
 **x_fields** | **str**| An optional fields mask | [optional] 

### Return type

[**list[ClientSNP]**](ClientSNP.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_gene**
> PublicGene get_gene(database_name, accession, dbsnp_build=dbsnp_build, reference_genome=reference_genome, x_fields=x_fields)

Generic gene information

### Example
```python
from __future__ import print_function
import time
import lumminary_sdk
from lumminary_sdk.rest import ApiException
from pprint import pprint

# Configure API key authorization: Bearer
configuration = lumminary_sdk.Configuration()
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# create an instance of the API class
api_instance = lumminary_sdk.LumminaryAPISpecApi(lumminary_sdk.ApiClient(configuration))
database_name = 'database_name_example' # str | The name of the database to search. E.g: Genbank
accession = 'accession_example' # str | The accession within the selected database
dbsnp_build = 149 # int | The dbSNP build for which to consider snps belonging to the gene. Defaults to 149 (optional) (default to 149)
reference_genome = 'GRCH37P13' # str | The reference genome for which gene annotations will be returned. Defaults to GRCh37p13 (optional) (default to GRCH37P13)
x_fields = 'x_fields_example' # str | An optional fields mask (optional)

try:
    # Generic gene information
    api_response = api_instance.get_gene(database_name, accession, dbsnp_build=dbsnp_build, reference_genome=reference_genome, x_fields=x_fields)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling LumminaryAPISpecApi->get_gene: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **database_name** | **str**| The name of the database to search. E.g: Genbank | 
 **accession** | **str**| The accession within the selected database | 
 **dbsnp_build** | **int**| The dbSNP build for which to consider snps belonging to the gene. Defaults to 149 | [optional] [default to 149]
 **reference_genome** | **str**| The reference genome for which gene annotations will be returned. Defaults to GRCh37p13 | [optional] [default to GRCH37P13]
 **x_fields** | **str**| An optional fields mask | [optional] 

### Return type

[**PublicGene**](PublicGene.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_product**
> Product get_product(product_id, x_fields=x_fields)

Get product details

### Example
```python
from __future__ import print_function
import time
import lumminary_sdk
from lumminary_sdk.rest import ApiException
from pprint import pprint

# Configure API key authorization: Bearer
configuration = lumminary_sdk.Configuration()
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# create an instance of the API class
api_instance = lumminary_sdk.LumminaryAPISpecApi(lumminary_sdk.ApiClient(configuration))
product_id = 'product_id_example' # str | The UUID of the product
x_fields = 'x_fields_example' # str | An optional fields mask (optional)

try:
    # Get product details
    api_response = api_instance.get_product(product_id, x_fields=x_fields)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling LumminaryAPISpecApi->get_product: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **product_id** | **str**| The UUID of the product | 
 **x_fields** | **str**| An optional fields mask | [optional] 

### Return type

[**Product**](Product.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_product_authorization**
> Authorization get_product_authorization(product_id, authorization_id, x_fields=x_fields)



### Example
```python
from __future__ import print_function
import time
import lumminary_sdk
from lumminary_sdk.rest import ApiException
from pprint import pprint

# Configure API key authorization: Bearer
configuration = lumminary_sdk.Configuration()
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# create an instance of the API class
api_instance = lumminary_sdk.LumminaryAPISpecApi(lumminary_sdk.ApiClient(configuration))
product_id = 'product_id_example' # str | The UUID of the product
authorization_id = 'authorization_id_example' # str | The UUID of the authorization
x_fields = 'x_fields_example' # str | An optional fields mask (optional)

try:
    api_response = api_instance.get_product_authorization(product_id, authorization_id, x_fields=x_fields)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling LumminaryAPISpecApi->get_product_authorization: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **product_id** | **str**| The UUID of the product | 
 **authorization_id** | **str**| The UUID of the authorization | 
 **x_fields** | **str**| An optional fields mask | [optional] 

### Return type

[**Authorization**](Authorization.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_reference_chromosome**
> ReferenceSequence get_reference_chromosome(genome_build_accession, chromosome_accession, range_start, range_stop, x_fields=x_fields)

Sequence for a region of the reference genome

Fetch a closed interval of nucleotides on a given chromosome. Includes start and stop positions

### Example
```python
from __future__ import print_function
import time
import lumminary_sdk
from lumminary_sdk.rest import ApiException
from pprint import pprint

# Configure API key authorization: Bearer
configuration = lumminary_sdk.Configuration()
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# create an instance of the API class
api_instance = lumminary_sdk.LumminaryAPISpecApi(lumminary_sdk.ApiClient(configuration))
genome_build_accession = 'genome_build_accession_example' # str | The accession of the reference genome
chromosome_accession = 'chromosome_accession_example' # str | The accession to the chromosome
range_start = 56 # int | Location on the chromosome
range_stop = 56 # int | Location on the chromosome
x_fields = 'x_fields_example' # str | An optional fields mask (optional)

try:
    # Sequence for a region of the reference genome
    api_response = api_instance.get_reference_chromosome(genome_build_accession, chromosome_accession, range_start, range_stop, x_fields=x_fields)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling LumminaryAPISpecApi->get_reference_chromosome: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **genome_build_accession** | **str**| The accession of the reference genome | 
 **chromosome_accession** | **str**| The accession to the chromosome | 
 **range_start** | **int**| Location on the chromosome | 
 **range_stop** | **int**| Location on the chromosome | 
 **x_fields** | **str**| An optional fields mask | [optional] 

### Return type

[**ReferenceSequence**](ReferenceSequence.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_reference_genome**
> list[ReferenceChromosomeOverview] get_reference_genome(genome_build_accession, x_fields=x_fields)

Reference genome metadata

### Example
```python
from __future__ import print_function
import time
import lumminary_sdk
from lumminary_sdk.rest import ApiException
from pprint import pprint

# Configure API key authorization: Bearer
configuration = lumminary_sdk.Configuration()
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# create an instance of the API class
api_instance = lumminary_sdk.LumminaryAPISpecApi(lumminary_sdk.ApiClient(configuration))
genome_build_accession = 'genome_build_accession_example' # str | 
x_fields = 'x_fields_example' # str | An optional fields mask (optional)

try:
    # Reference genome metadata
    api_response = api_instance.get_reference_genome(genome_build_accession, x_fields=x_fields)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling LumminaryAPISpecApi->get_reference_genome: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **genome_build_accession** | **str**|  | 
 **x_fields** | **str**| An optional fields mask | [optional] 

### Return type

[**list[ReferenceChromosomeOverview]**](ReferenceChromosomeOverview.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_reference_genomes_group**
> list[ReferenceGenomeOverview] get_reference_genomes_group(x_fields=x_fields)

Reference genome builds

Lists reference genome builds that are available

### Example
```python
from __future__ import print_function
import time
import lumminary_sdk
from lumminary_sdk.rest import ApiException
from pprint import pprint

# Configure API key authorization: Bearer
configuration = lumminary_sdk.Configuration()
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# create an instance of the API class
api_instance = lumminary_sdk.LumminaryAPISpecApi(lumminary_sdk.ApiClient(configuration))
x_fields = 'x_fields_example' # str | An optional fields mask (optional)

try:
    # Reference genome builds
    api_response = api_instance.get_reference_genomes_group(x_fields=x_fields)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling LumminaryAPISpecApi->get_reference_genomes_group: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **x_fields** | **str**| An optional fields mask | [optional] 

### Return type

[**list[ReferenceGenomeOverview]**](ReferenceGenomeOverview.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_reference_snp**
> PublicSNP get_reference_snp(snp_accession, dbsnp_version=dbsnp_version, grch_version=grch_version, x_fields=x_fields)

Reference SNP data

Get reference SNP information, from dbSNP

### Example
```python
from __future__ import print_function
import time
import lumminary_sdk
from lumminary_sdk.rest import ApiException
from pprint import pprint

# Configure API key authorization: Bearer
configuration = lumminary_sdk.Configuration()
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# create an instance of the API class
api_instance = lumminary_sdk.LumminaryAPISpecApi(lumminary_sdk.ApiClient(configuration))
snp_accession = 'snp_accession_example' # str | The rsId of the SNP
dbsnp_version = 149 # int | The dbSNP build. Defaults to 149 (optional) (default to 149)
grch_version = 'GRCH37P13' # str | The GRCh build on which to place snips. Defaults to GRCh37p13 (optional) (default to GRCH37P13)
x_fields = 'x_fields_example' # str | An optional fields mask (optional)

try:
    # Reference SNP data
    api_response = api_instance.get_reference_snp(snp_accession, dbsnp_version=dbsnp_version, grch_version=grch_version, x_fields=x_fields)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling LumminaryAPISpecApi->get_reference_snp: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **snp_accession** | **str**| The rsId of the SNP | 
 **dbsnp_version** | **int**| The dbSNP build. Defaults to 149 | [optional] [default to 149]
 **grch_version** | **str**| The GRCh build on which to place snips. Defaults to GRCh37p13 | [optional] [default to GRCH37P13]
 **x_fields** | **str**| An optional fields mask | [optional] 

### Return type

[**PublicSNP**](PublicSNP.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **post_authorization_result_credentials**
> ReportCredentials post_authorization_result_credentials(product_id, authorization_id, credentials_username=credentials_username, credentials_password=credentials_password, report_url=report_url, x_fields=x_fields)

Provide a result for the authorization

These can be log-in credentials for a website where the result is available

### Example
```python
from __future__ import print_function
import time
import lumminary_sdk
from lumminary_sdk.rest import ApiException
from pprint import pprint

# Configure API key authorization: Bearer
configuration = lumminary_sdk.Configuration()
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# create an instance of the API class
api_instance = lumminary_sdk.LumminaryAPISpecApi(lumminary_sdk.ApiClient(configuration))
product_id = 'product_id_example' # str | The UUID of the product
authorization_id = 'authorization_id_example' # str | The UUID of the authorization
credentials_username = 'credentials_username_example' # str | Credentials for accessing the result. Includes password, username and url (optional)
credentials_password = 'credentials_password_example' # str | Credentials for accessing the result. Includes password, username and url (optional)
report_url = 'report_url_example' # str | Credentials for accessing the result. Includes password, username and url (optional)
x_fields = 'x_fields_example' # str | An optional fields mask (optional)

try:
    # Provide a result for the authorization
    api_response = api_instance.post_authorization_result_credentials(product_id, authorization_id, credentials_username=credentials_username, credentials_password=credentials_password, report_url=report_url, x_fields=x_fields)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling LumminaryAPISpecApi->post_authorization_result_credentials: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **product_id** | **str**| The UUID of the product | 
 **authorization_id** | **str**| The UUID of the authorization | 
 **credentials_username** | **str**| Credentials for accessing the result. Includes password, username and url | [optional] 
 **credentials_password** | **str**| Credentials for accessing the result. Includes password, username and url | [optional] 
 **report_url** | **str**| Credentials for accessing the result. Includes password, username and url | [optional] 
 **x_fields** | **str**| An optional fields mask | [optional] 

### Return type

[**ReportCredentials**](ReportCredentials.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: application/x-www-form-urlencoded, multipart/form-data
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **post_authorization_result_file**
> ReportFile post_authorization_result_file(product_id, authorization_id, file_report=file_report, original_filename=original_filename, x_fields=x_fields)

Provide a file result to the authorization, e

g. a pdf report

### Example
```python
from __future__ import print_function
import time
import lumminary_sdk
from lumminary_sdk.rest import ApiException
from pprint import pprint

# Configure API key authorization: Bearer
configuration = lumminary_sdk.Configuration()
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# create an instance of the API class
api_instance = lumminary_sdk.LumminaryAPISpecApi(lumminary_sdk.ApiClient(configuration))
product_id = 'product_id_example' # str | The UUID of the product
authorization_id = 'authorization_id_example' # str | The UUID of the authorization
file_report = '/path/to/file.txt' # file | A binary file (e.g. pdf) that contains the result of the authorization (optional)
original_filename = 'original_filename_example' # str | Optional original filename for the report. If not provided, the filename of uploaded file will be used (optional)
x_fields = 'x_fields_example' # str | An optional fields mask (optional)

try:
    # Provide a file result to the authorization, e
    api_response = api_instance.post_authorization_result_file(product_id, authorization_id, file_report=file_report, original_filename=original_filename, x_fields=x_fields)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling LumminaryAPISpecApi->post_authorization_result_file: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **product_id** | **str**| The UUID of the product | 
 **authorization_id** | **str**| The UUID of the authorization | 
 **file_report** | **file**| A binary file (e.g. pdf) that contains the result of the authorization | [optional] 
 **original_filename** | **str**| Optional original filename for the report. If not provided, the filename of uploaded file will be used | [optional] 
 **x_fields** | **str**| An optional fields mask | [optional] 

### Return type

[**ReportFile**](ReportFile.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: multipart/form-data
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **post_client_snp_group**
> list[ClientSNP] post_client_snp_group(client_id, dataset_id, snps, x_fields=x_fields)

Get a large group of SNPs

SNPs that are not present in the dataset are ignored, 404 is returned only if the dataset/client does not exist

### Example
```python
from __future__ import print_function
import time
import lumminary_sdk
from lumminary_sdk.rest import ApiException
from pprint import pprint

# Configure API key authorization: Bearer
configuration = lumminary_sdk.Configuration()
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# create an instance of the API class
api_instance = lumminary_sdk.LumminaryAPISpecApi(lumminary_sdk.ApiClient(configuration))
client_id = 'client_id_example' # str | The UUID of the client
dataset_id = 'dataset_id_example' # str | The UUID of one of the client's dataset
snps = 'snps_example' # str | JSON-encoded list of snps to be fetched
x_fields = 'x_fields_example' # str | An optional fields mask (optional)

try:
    # Get a large group of SNPs
    api_response = api_instance.post_client_snp_group(client_id, dataset_id, snps, x_fields=x_fields)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling LumminaryAPISpecApi->post_client_snp_group: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **client_id** | **str**| The UUID of the client | 
 **dataset_id** | **str**| The UUID of one of the client&#39;s dataset | 
 **snps** | **str**| JSON-encoded list of snps to be fetched | 
 **x_fields** | **str**| An optional fields mask | [optional] 

### Return type

[**list[ClientSNP]**](ClientSNP.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: application/x-www-form-urlencoded, multipart/form-data
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **post_jwt_auth**
> JavascriptWebToken post_jwt_auth(username, password, role, x_fields=x_fields)

General-purpose authentication

## Note: * The JWT tokens returned should be passed to any resource that requires authentication, in the Authentication header, in the format `Bearer: your-token-here` * Only JWT authentication tokens are provided (no refresh tokens). These tokens are valid for 30 seconds from the moment they were issued

### Example
```python
from __future__ import print_function
import time
import lumminary_sdk
from lumminary_sdk.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = lumminary_sdk.LumminaryAPISpecApi()
username = 'username_example' # str | The email for a Client, or the API for a partner product
password = 'password_example' # str | The passowrd for a Client, or the API key for a service
role = 'role_example' # str | The role for which authentication will be made. Value : role_product
x_fields = 'x_fields_example' # str | An optional fields mask (optional)

try:
    # General-purpose authentication
    api_response = api_instance.post_jwt_auth(username, password, role, x_fields=x_fields)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling LumminaryAPISpecApi->post_jwt_auth: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **username** | **str**| The email for a Client, or the API for a partner product | 
 **password** | **str**| The passowrd for a Client, or the API key for a service | 
 **role** | **str**| The role for which authentication will be made. Value : role_product | 
 **x_fields** | **str**| An optional fields mask | [optional] 

### Return type

[**JavascriptWebToken**](JavascriptWebToken.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/x-www-form-urlencoded, multipart/form-data
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **post_product_authorization**
> post_product_authorization(product_id, authorization_id)

Signal that processing is complete, without uploading any result

### Example
```python
from __future__ import print_function
import time
import lumminary_sdk
from lumminary_sdk.rest import ApiException
from pprint import pprint

# Configure API key authorization: Bearer
configuration = lumminary_sdk.Configuration()
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# create an instance of the API class
api_instance = lumminary_sdk.LumminaryAPISpecApi(lumminary_sdk.ApiClient(configuration))
product_id = 'product_id_example' # str | The UUID of the product
authorization_id = 'authorization_id_example' # str | The UUID of the authorization

try:
    # Signal that processing is complete, without uploading any result
    api_instance.post_product_authorization(product_id, authorization_id)
except ApiException as e:
    print("Exception when calling LumminaryAPISpecApi->post_product_authorization: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **product_id** | **str**| The UUID of the product | 
 **authorization_id** | **str**| The UUID of the authorization | 

### Return type

void (empty response body)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **post_product_authorization_unfulfillable**
> Authorization post_product_authorization_unfulfillable(product_id, authorization_id, x_fields=x_fields)

Catch-all Authorization state, for authorizations that passed all verifications and should reach the partner Product, but cannot be fulfilled for various reasons

### Example
```python
from __future__ import print_function
import time
import lumminary_sdk
from lumminary_sdk.rest import ApiException
from pprint import pprint

# Configure API key authorization: Bearer
configuration = lumminary_sdk.Configuration()
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# create an instance of the API class
api_instance = lumminary_sdk.LumminaryAPISpecApi(lumminary_sdk.ApiClient(configuration))
product_id = 'product_id_example' # str | The UUID of the product
authorization_id = 'authorization_id_example' # str | The UUID of the authorization
x_fields = 'x_fields_example' # str | An optional fields mask (optional)

try:
    # Catch-all Authorization state, for authorizations that passed all verifications and should reach the partner Product, but cannot be fulfilled for various reasons
    api_response = api_instance.post_product_authorization_unfulfillable(product_id, authorization_id, x_fields=x_fields)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling LumminaryAPISpecApi->post_product_authorization_unfulfillable: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **product_id** | **str**| The UUID of the product | 
 **authorization_id** | **str**| The UUID of the authorization | 
 **x_fields** | **str**| An optional fields mask | [optional] 

### Return type

[**Authorization**](Authorization.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

