# PredictNutritionGet200ResponsePredictionsInner


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**nutrients** | **object** | a dictionary mapping nutrient keys in Open Food Facts format (ex: &#x60;fat_100g&#x60;) to a dictionary containing the detected nutrient value.  | [optional] 
**entities** | [**PredictNutritionGet200ResponsePredictionsInnerEntities**](PredictNutritionGet200ResponsePredictionsInnerEntities.md) |  | [optional] 

## Example

```python
from openapi_client.models.predict_nutrition_get200_response_predictions_inner import PredictNutritionGet200ResponsePredictionsInner

# TODO update the JSON string below
json = "{}"
# create an instance of PredictNutritionGet200ResponsePredictionsInner from a JSON string
predict_nutrition_get200_response_predictions_inner_instance = PredictNutritionGet200ResponsePredictionsInner.from_json(json)
# print the JSON string representation of the object
print(PredictNutritionGet200ResponsePredictionsInner.to_json())

# convert the object into a dict
predict_nutrition_get200_response_predictions_inner_dict = predict_nutrition_get200_response_predictions_inner_instance.to_dict()
# create an instance of PredictNutritionGet200ResponsePredictionsInner from a dict
predict_nutrition_get200_response_predictions_inner_from_dict = PredictNutritionGet200ResponsePredictionsInner.from_dict(predict_nutrition_get200_response_predictions_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


