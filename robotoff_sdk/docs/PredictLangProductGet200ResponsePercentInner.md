# PredictLangProductGet200ResponsePercentInner


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**lang** | **str** | the predicted language (2-letter code). &#x60;null&#x60; if the language could not be detected. | [optional] 
**percent** | **float** | the percentage of words for which the language was detected over all images | [optional] 

## Example

```python
from openapi_client.models.predict_lang_product_get200_response_percent_inner import PredictLangProductGet200ResponsePercentInner

# TODO update the JSON string below
json = "{}"
# create an instance of PredictLangProductGet200ResponsePercentInner from a JSON string
predict_lang_product_get200_response_percent_inner_instance = PredictLangProductGet200ResponsePercentInner.from_json(json)
# print the JSON string representation of the object
print(PredictLangProductGet200ResponsePercentInner.to_json())

# convert the object into a dict
predict_lang_product_get200_response_percent_inner_dict = predict_lang_product_get200_response_percent_inner_instance.to_dict()
# create an instance of PredictLangProductGet200ResponsePercentInner from a dict
predict_lang_product_get200_response_percent_inner_from_dict = PredictLangProductGet200ResponsePercentInner.from_dict(predict_lang_product_get200_response_percent_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


