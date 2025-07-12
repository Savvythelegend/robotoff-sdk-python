# PredictionsGet200Response


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**status** | **str** |  | [optional] 
**predictions** | **List[object]** |  | [optional] 
**count** | **int** | The total number of results with the provided filters | [optional] 

## Example

```python
from openapi_client.models.predictions_get200_response import PredictionsGet200Response

# TODO update the JSON string below
json = "{}"
# create an instance of PredictionsGet200Response from a JSON string
predictions_get200_response_instance = PredictionsGet200Response.from_json(json)
# print the JSON string representation of the object
print(PredictionsGet200Response.to_json())

# convert the object into a dict
predictions_get200_response_dict = predictions_get200_response_instance.to_dict()
# create an instance of PredictionsGet200Response from a dict
predictions_get200_response_from_dict = PredictionsGet200Response.from_dict(predictions_get200_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


