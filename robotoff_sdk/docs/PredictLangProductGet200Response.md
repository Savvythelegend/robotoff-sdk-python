# PredictLangProductGet200Response


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**counts** | [**List[PredictLangProductGet200ResponseCountsInner]**](PredictLangProductGet200ResponseCountsInner.md) | the number of words detected for each language, over all images, sorted by descending count  | [optional] 
**percent** | [**List[PredictLangProductGet200ResponsePercentInner]**](PredictLangProductGet200ResponsePercentInner.md) | the percentage of words detected for each language, over all images, sorted by descending percentage  | [optional] 
**image_ids** | **List[float]** | the IDs of the images that were used to generate the predictions  | [optional] 

## Example

```python
from openapi_client.models.predict_lang_product_get200_response import PredictLangProductGet200Response

# TODO update the JSON string below
json = "{}"
# create an instance of PredictLangProductGet200Response from a JSON string
predict_lang_product_get200_response_instance = PredictLangProductGet200Response.from_json(json)
# print the JSON string representation of the object
print(PredictLangProductGet200Response.to_json())

# convert the object into a dict
predict_lang_product_get200_response_dict = predict_lang_product_get200_response_instance.to_dict()
# create an instance of PredictLangProductGet200Response from a dict
predict_lang_product_get200_response_from_dict = PredictLangProductGet200Response.from_dict(predict_lang_product_get200_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


