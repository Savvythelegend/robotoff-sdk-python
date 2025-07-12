# PredictLangGet200Response


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**predictions** | [**List[PredictLangGet200ResponsePredictionsInner]**](PredictLangGet200ResponsePredictionsInner.md) | a list of predicted languages, sorted by descending probability | [optional] 

## Example

```python
from openapi_client.models.predict_lang_get200_response import PredictLangGet200Response

# TODO update the JSON string below
json = "{}"
# create an instance of PredictLangGet200Response from a JSON string
predict_lang_get200_response_instance = PredictLangGet200Response.from_json(json)
# print the JSON string representation of the object
print(PredictLangGet200Response.to_json())

# convert the object into a dict
predict_lang_get200_response_dict = predict_lang_get200_response_instance.to_dict()
# create an instance of PredictLangGet200Response from a dict
predict_lang_get200_response_from_dict = PredictLangGet200Response.from_dict(predict_lang_get200_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


