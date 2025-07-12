# ImagePredictionsGet200Response


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**status** | **str** |  | [optional] 
**image_predictions** | **List[object]** |  | [optional] 
**count** | **int** | The total number of results with the provided filters | [optional] 

## Example

```python
from openapi_client.models.image_predictions_get200_response import ImagePredictionsGet200Response

# TODO update the JSON string below
json = "{}"
# create an instance of ImagePredictionsGet200Response from a JSON string
image_predictions_get200_response_instance = ImagePredictionsGet200Response.from_json(json)
# print the JSON string representation of the object
print(ImagePredictionsGet200Response.to_json())

# convert the object into a dict
image_predictions_get200_response_dict = image_predictions_get200_response_instance.to_dict()
# create an instance of ImagePredictionsGet200Response from a dict
image_predictions_get200_response_from_dict = ImagePredictionsGet200Response.from_dict(image_predictions_get200_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


