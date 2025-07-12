# InsightsGet200Response


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**insights** | [**List[InsightSearchResult]**](InsightSearchResult.md) |  | [optional] 
**status** | **str** |  | [optional] 
**count** | **int** | The total number of results with the provided filters | [optional] 

## Example

```python
from openapi_client.models.insights_get200_response import InsightsGet200Response

# TODO update the JSON string below
json = "{}"
# create an instance of InsightsGet200Response from a JSON string
insights_get200_response_instance = InsightsGet200Response.from_json(json)
# print the JSON string representation of the object
print(InsightsGet200Response.to_json())

# convert the object into a dict
insights_get200_response_dict = insights_get200_response_instance.to_dict()
# create an instance of InsightsGet200Response from a dict
insights_get200_response_from_dict = InsightsGet200Response.from_dict(insights_get200_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


