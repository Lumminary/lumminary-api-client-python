# Authorization

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**scopes** | [**AccessScope**](AccessScope.md) |  | 
**client_uuid** | **str** | The UUID of the client owning the Dataset to which the product is authorized | 
**is_active** | **bool** | If false, the the authorization is revoked and data access authorizations fail | 
**authorization_uuid** | **str** | Identifier of the Authorization | 
**product_uuid** | **str** | Identifier of the Product to be authorized | 
**state** | **str** | The authorization state. One of : [&#39;authorization_state_pending_dataset&#39;, &#39;authorization_state_fulfillable&#39;, &#39;authorization_state_result_available&#39;] | 
**create_timestamp** | **int** | Creation timestamp for the Authorization | 
**report_credentials** | [**list[ReportCredentials]**](ReportCredentials.md) |  | [optional] 
**report_files** | [**list[ReportFile]**](ReportFile.md) |  | [optional] 
**order** | **str** | Optional UUID of the Order that created the Authorization | [optional] 
**sequence_number** | **int** | The sequence number of the Authorization. Used as a filter when fetching new Authorizations | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


