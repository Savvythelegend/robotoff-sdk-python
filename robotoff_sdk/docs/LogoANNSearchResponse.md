# LogoANNSearchResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**results** | [**List[LogoANNSearchResponseResultsInner]**](LogoANNSearchResponseResultsInner.md) | Each item corresponds to a neighbor logo | 
**count** | **int** | Number of returned results | 
**query_logo_id** | **int** | ID of the query logo | 

## Example

```python
from openapi_client.models.logo_ann_search_response import LogoANNSearchResponse

# TODO update the JSON string below
json = "{}"
# create an instance of LogoANNSearchResponse from a JSON string
logo_ann_search_response_instance = LogoANNSearchResponse.from_json(json)
# print the JSON string representation of the object
print(LogoANNSearchResponse.to_json())

# convert the object into a dict
logo_ann_search_response_dict = logo_ann_search_response_instance.to_dict()
# create an instance of LogoANNSearchResponse from a dict
logo_ann_search_response_from_dict = LogoANNSearchResponse.from_dict(logo_ann_search_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


