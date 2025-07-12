# InsightSearchResult

An insight search result as returned by /insights/random or /insights/{barcode}

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | Insight ID | 
**type** | **str** | Insight type | 
**barcode** | **int** | Barcode of the product | 
**countries** | **List[str]** | country tags of the product | 

## Example

```python
from openapi_client.models.insight_search_result import InsightSearchResult

# TODO update the JSON string below
json = "{}"
# create an instance of InsightSearchResult from a JSON string
insight_search_result_instance = InsightSearchResult.from_json(json)
# print the JSON string representation of the object
print(InsightSearchResult.to_json())

# convert the object into a dict
insight_search_result_dict = insight_search_result_instance.to_dict()
# create an instance of InsightSearchResult from a dict
insight_search_result_from_dict = InsightSearchResult.from_dict(insight_search_result_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


