# LogoANNSearchResponseResultsInner


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**logo_id** | **int** | ID of the result logo | 
**distance** | **float** | distance between the query logo and the result logo (closer to 0 means a more similar logo)  | 

## Example

```python
from openapi_client.models.logo_ann_search_response_results_inner import LogoANNSearchResponseResultsInner

# TODO update the JSON string below
json = "{}"
# create an instance of LogoANNSearchResponseResultsInner from a JSON string
logo_ann_search_response_results_inner_instance = LogoANNSearchResponseResultsInner.from_json(json)
# print the JSON string representation of the object
print(LogoANNSearchResponseResultsInner.to_json())

# convert the object into a dict
logo_ann_search_response_results_inner_dict = logo_ann_search_response_results_inner_instance.to_dict()
# create an instance of LogoANNSearchResponseResultsInner from a dict
logo_ann_search_response_results_inner_from_dict = LogoANNSearchResponseResultsInner.from_dict(logo_ann_search_response_results_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


