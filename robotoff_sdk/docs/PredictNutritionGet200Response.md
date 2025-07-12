# PredictNutritionGet200Response

the extracted nutritional information from the model. 

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**predictions** | [**List[PredictNutritionGet200ResponsePredictionsInner]**](PredictNutritionGet200ResponsePredictionsInner.md) |  | [optional] 

## Example

```python
from openapi_client.models.predict_nutrition_get200_response import PredictNutritionGet200Response

# TODO update the JSON string below
json = "{}"
# create an instance of PredictNutritionGet200Response from a JSON string
predict_nutrition_get200_response_instance = PredictNutritionGet200Response.from_json(json)
# print the JSON string representation of the object
print(PredictNutritionGet200Response.to_json())

# convert the object into a dict
predict_nutrition_get200_response_dict = predict_nutrition_get200_response_instance.to_dict()
# create an instance of PredictNutritionGet200Response from a dict
predict_nutrition_get200_response_from_dict = PredictNutritionGet200Response.from_dict(predict_nutrition_get200_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


