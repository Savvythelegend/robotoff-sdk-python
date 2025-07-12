# PredictCategoryPost200Response


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**neural** | [**List[PredictCategoryPost200ResponseNeuralInner]**](PredictCategoryPost200ResponseNeuralInner.md) |  | [optional] 

## Example

```python
from openapi_client.models.predict_category_post200_response import PredictCategoryPost200Response

# TODO update the JSON string below
json = "{}"
# create an instance of PredictCategoryPost200Response from a JSON string
predict_category_post200_response_instance = PredictCategoryPost200Response.from_json(json)
# print the JSON string representation of the object
print(PredictCategoryPost200Response.to_json())

# convert the object into a dict
predict_category_post200_response_dict = predict_category_post200_response_instance.to_dict()
# create an instance of PredictCategoryPost200Response from a dict
predict_category_post200_response_from_dict = PredictCategoryPost200Response.from_dict(predict_category_post200_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


