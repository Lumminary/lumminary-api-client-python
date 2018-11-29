# lumminary_sdk.AuthApi

All URIs are relative to *https://api.lumminary.com/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**post_jwt_auth**](AuthApi.md#post_jwt_auth) | **POST** /auth/jwt | General-purpose authentication


# **post_jwt_auth**
> JavascriptWebToken post_jwt_auth(username, password, role, _2_fa_token=_2_fa_token, x_fields=x_fields)

General-purpose authentication

If 2FA is enabled, the 2FA token is validated along with the username/password pair. Otherwise, the 2FA token, even if provided, is ignored.  ## Note: * A fresh and not previously used 2FA token should be passed, otherwise authentication will fail. * The JWT tokens returned should be passed to any resource that requires authentication, in the Authentication header, in the format `Bearer: your-token-here` * Only JWT authentication tokens are provided (no refresh tokens). These tokens are valid for 30 seconds from the moment they were issued

### Example
```python
from __future__ import print_function
import time
import lumminary_sdk
from lumminary_sdk.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = lumminary_sdk.AuthApi()
username = 'username_example' # str | The email for a Client, or the API for a partner product
password = 'password_example' # str | The passowrd for a Client, or the API key for a service
role = 'role_example' # str | The role for which authentication will be made. Value : role_product
_2_fa_token = '_2_fa_token_example' # str | The One-time password provided by a 2FA product, if enabled (optional)
x_fields = 'x_fields_example' # str | An optional fields mask (optional)

try:
    # General-purpose authentication
    api_response = api_instance.post_jwt_auth(username, password, role, _2_fa_token=_2_fa_token, x_fields=x_fields)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AuthApi->post_jwt_auth: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **username** | **str**| The email for a Client, or the API for a partner product | 
 **password** | **str**| The passowrd for a Client, or the API key for a service | 
 **role** | **str**| The role for which authentication will be made. Value : role_product | 
 **_2_fa_token** | **str**| The One-time password provided by a 2FA product, if enabled | [optional] 
 **x_fields** | **str**| An optional fields mask | [optional] 

### Return type

[**JavascriptWebToken**](JavascriptWebToken.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/x-www-form-urlencoded, multipart/form-data
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

