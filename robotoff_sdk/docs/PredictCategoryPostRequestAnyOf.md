# PredictCategoryPostRequestAnyOf


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**barcode** | **str** | The barcode of the product to categorize | 
**server_type** | **str** | The server type (&#x3D;project) to use, such as &#39;off&#39; (Open Food Facts), &#39;obf&#39; (Open Beauty Facts),... Only &#39;off&#39; is currently supported for category prediction  | [optional] [default to 'off']
**deepest_only** | **bool** | If true, only return the deepest elements in the category taxonomy (don&#39;t return categories that are parents of other predicted categories)  | [optional] 
**threshold** | **float** | The score above which we consider the category to be detected  | [optional] [default to 0.5]

## Example

```python
from openapi_client.models.predict_category_post_request_any_of import PredictCategoryPostRequestAnyOf

# TODO update the JSON string below
json = "{}"
# create an instance of PredictCategoryPostRequestAnyOf from a JSON string
predict_category_post_request_any_of_instance = PredictCategoryPostRequestAnyOf.from_json(json)
# print the JSON string representation of the object
print(PredictCategoryPostRequestAnyOf.to_json())

# convert the object into a dict
predict_category_post_request_any_of_dict = predict_category_post_request_any_of_instance.to_dict()
# create an instance of PredictCategoryPostRequestAnyOf from a dict
predict_category_post_request_any_of_from_dict = PredictCategoryPostRequestAnyOf.from_dict(predict_category_post_request_any_of_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


