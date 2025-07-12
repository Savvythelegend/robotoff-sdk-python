# PredictCategoryPost200ResponseNeuralInner


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**value_tag** | **str** | The predicted &#x60;value_tag&#x60; | 
**confidence** | **float** | The confidence score of the model | 

## Example

```python
from openapi_client.models.predict_category_post200_response_neural_inner import PredictCategoryPost200ResponseNeuralInner

# TODO update the JSON string below
json = "{}"
# create an instance of PredictCategoryPost200ResponseNeuralInner from a JSON string
predict_category_post200_response_neural_inner_instance = PredictCategoryPost200ResponseNeuralInner.from_json(json)
# print the JSON string representation of the object
print(PredictCategoryPost200ResponseNeuralInner.to_json())

# convert the object into a dict
predict_category_post200_response_neural_inner_dict = predict_category_post200_response_neural_inner_instance.to_dict()
# create an instance of PredictCategoryPost200ResponseNeuralInner from a dict
predict_category_post200_response_neural_inner_from_dict = PredictCategoryPost200ResponseNeuralInner.from_dict(predict_category_post200_response_neural_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


