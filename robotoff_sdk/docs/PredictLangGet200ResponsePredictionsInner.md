# PredictLangGet200ResponsePredictionsInner


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**lang** | **str** | the predicted language (2-letter code) | [optional] 
**confidence** | **float** | the probability of the predicted language | [optional] 

## Example

```python
from openapi_client.models.predict_lang_get200_response_predictions_inner import PredictLangGet200ResponsePredictionsInner

# TODO update the JSON string below
json = "{}"
# create an instance of PredictLangGet200ResponsePredictionsInner from a JSON string
predict_lang_get200_response_predictions_inner_instance = PredictLangGet200ResponsePredictionsInner.from_json(json)
# print the JSON string representation of the object
print(PredictLangGet200ResponsePredictionsInner.to_json())

# convert the object into a dict
predict_lang_get200_response_predictions_inner_dict = predict_lang_get200_response_predictions_inner_instance.to_dict()
# create an instance of PredictLangGet200ResponsePredictionsInner from a dict
predict_lang_get200_response_predictions_inner_from_dict = PredictLangGet200ResponsePredictionsInner.from_dict(predict_lang_get200_response_predictions_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


