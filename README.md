# lumminary_api
A general-purpose API for accessing genomic data

This Python package is automatically generated by the [Swagger Codegen](https://github.com/swagger-api/swagger-codegen) project:

- API version: 1.0
- Package version: 1.0.0
- Build package: io.swagger.codegen.languages.PythonClientCodegen

## Requirements.

Python 2.7 and 3.4+

## Installation & Usage
### pip install

If the python package is hosted on Github, you can install directly from Github

```sh
pip install git+https://github.com/lumminary/sdk-php.git
```
(you may need to run `pip` with root permission: `sudo pip install git+https://github.com/lumminary/sdk-php.git`)

Then import the package:
```python
import lumminary_api 
```

### Setuptools

Install via [Setuptools](http://pypi.python.org/pypi/setuptools).

```sh
python setup.py install --user
```
(or `sudo python setup.py install` to install the package for all users)

Then import the package:
```python
import lumminary_api
```

## Getting Started

Please follow the [installation procedure](#installation--usage) and then run the following:

```python
from __future__ import print_function
import time
import lumminary_api
from lumminary_api.rest import ApiException
from pprint import pprint

# Configure API key authorization: Bearer
lumminary_api.configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# lumminary_api.configuration.api_key_prefix['Authorization'] = 'Bearer'
# create an instance of the API class
api_instance = lumminary_api.LumminaryApi()
app_id = 'app_id_example' # str | The UUID of the app
x_fields = 'x_fields_example' # str | An optional fields mask (optional)

try:
    # Get app details
    api_response = api_instance.get_app(app_id, x_fields=x_fields)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling LumminaryApi->get_app: %s\n" % e)

```

## Documentation for API Endpoints

All URIs are relative to *https://api.lumminary.com/v1*

Class | Method | HTTP request | Description
------------ | ------------- | ------------- | -------------
*LumminaryApi* | [**get_app**](docs/LumminaryApi.md#get_app) | **GET** /apps/{appId} | Get app details
*LumminaryApi* | [**get_app_authorization**](docs/LumminaryApi.md#get_app_authorization) | **GET** /apps/{appId}/authorizations/{authorizationId} | 
*LumminaryApi* | [**get_authorizations_queue**](docs/LumminaryApi.md#get_authorizations_queue) | **GET** /apps/{appId}/authorizations | 
*LumminaryApi* | [**get_client_gene**](docs/LumminaryApi.md#get_client_gene) | **GET** /clients/{clientId}/datasets/{datasetId}/genes/{geneSymbol} | Get gene by symbol
*LumminaryApi* | [**get_client_snp**](docs/LumminaryApi.md#get_client_snp) | **GET** /clients/{clientId}/datasets/{datasetId}/snps/{snpId} | Get SNP information
*LumminaryApi* | [**get_client_snp_group**](docs/LumminaryApi.md#get_client_snp_group) | **GET** /clients/{clientId}/datasets/{datasetId}/snps/ | 
*LumminaryApi* | [**post_app_authorization**](docs/LumminaryApi.md#post_app_authorization) | **POST** /apps/{appId}/authorizations/{authorizationId} | Singnal that processing is complete, without uploading any result
*LumminaryApi* | [**post_authorization_result_credentials**](docs/LumminaryApi.md#post_authorization_result_credentials) | **POST** /apps/{appId}/authorizations/{authorizationId}/credentials | Provide a result for the authorization
*LumminaryApi* | [**post_authorization_result_file**](docs/LumminaryApi.md#post_authorization_result_file) | **POST** /apps/{appId}/authorizations/{authorizationId}/file | Provide a file result to the authorization, e
*LumminaryApi* | [**post_client_snp_group**](docs/LumminaryApi.md#post_client_snp_group) | **POST** /clients/{clientId}/datasets/{datasetId}/snps/ | Get a large group of SNPs
*AuthApi* | [**post_jwt_auth**](docs/AuthApi.md#post_jwt_auth) | **POST** /auth/jwt | General-purpose authentication


## Documentation For Models

 - [AccessScope](docs/AccessScope.md)
 - [App](docs/App.md)
 - [Authorization](docs/Authorization.md)
 - [ClientGene](docs/ClientGene.md)
 - [ClientSNP](docs/ClientSNP.md)
 - [ClientVariations](docs/ClientVariations.md)
 - [CustomerAddress](docs/CustomerAddress.md)
 - [CustomerName](docs/CustomerName.md)
 - [FileLocation](docs/FileLocation.md)
 - [JavascriptWebToken](docs/JavascriptWebToken.md)
 - [MolecularLocation](docs/MolecularLocation.md)
 - [ReportCredentials](docs/ReportCredentials.md)
 - [ReportFile](docs/ReportFile.md)


## Documentation For Authorization


## Bearer

- **Type**: API key
- **API key parameter name**: Authorization
- **Location**: HTTP header


## Author



