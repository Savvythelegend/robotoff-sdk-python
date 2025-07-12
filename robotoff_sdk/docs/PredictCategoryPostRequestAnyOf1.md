# PredictCategoryPostRequestAnyOf1


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**product** | [**PredictCategoryPostRequestAnyOf1Product**](PredictCategoryPostRequestAnyOf1Product.md) |  | 
**deepest_only** | **bool** | If true, only return the deepest elements in the category taxonomy (don&#39;t return categories that are parents of other predicted categories)  | [optional] 
**threshold** | **float** | The score above which we consider the category to be detected  | [optional] [default to 0.5]

## Example

```python
from openapi_client.models.predict_category_post_request_any_of1 import PredictCategoryPostRequestAnyOf1

# TODO update the JSON string below
json = "{}"
# create an instance of PredictCategoryPostRequestAnyOf1 from a JSON string
predict_category_post_request_any_of1_instance = PredictCategoryPostRequestAnyOf1.from_json(json)
# print the JSON string representation of the object
print(PredictCategoryPostRequestAnyOf1.to_json())

# convert the object into a dict
predict_category_post_request_any_of1_dict = predict_category_post_request_any_of1_instance.to_dict()
# create an instance of PredictCategoryPostRequestAnyOf1 from a dict
predict_category_post_request_any_of1_from_dict = PredictCategoryPostRequestAnyOf1.from_dict(predict_category_post_request_any_of1_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


