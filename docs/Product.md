# Product

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**snps_authorized_any** | **bool** | A boolean value specifying if SNP set is not strict | 
**snps_authorized** | **list[str]** | A superset of snps_min_required, containing all SNPs to which an Product has access (includes optional SNPs) | 
**authorized_scopes** | **list[str]** | A list of scopes that the product can require from clients | 
**email** | **str** | The contact email for the product | [optional] 
**redirect_uri** | **str** | A redirect url registered as a callback for the Connect with Lumminary authorization flow | [optional] 
**snps_min_required_any** | **bool** | A boolean value specifying if SNP set is not strict | 
**snps_min_required** | [**SnpsMinRequired**](SnpsMinRequired.md) | Minimum required snps for Dataset-Product compatibility | 
**product_uuid** | **str** | The product identifier | 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


