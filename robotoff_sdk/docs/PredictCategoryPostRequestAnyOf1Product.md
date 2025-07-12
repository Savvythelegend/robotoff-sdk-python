# PredictCategoryPostRequestAnyOf1Product

product information used as model input. All fields are optional, but at least one field must be provided. 

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**product_name** | **str** |  | [optional] 
**ingredients_tags** | **List[str]** | the ingredient list, as an ordered list of ingredient tags | [optional] 
**image_embeddings** | **List[List[float]]** | Embeddings of the 10 most recent product images generated with clip-vit-base-patch32 model. Each item of the list is the embedding of a single image, provided as a list of dimension 512. Shape: (num_images, 512)  | [optional] 
**ocr** | **List[str]** | A list of string corresponding to the text extracted from the product images with OCR. Each element of the list is the text of a single image, the list order doesn&#39;t affect predictions. We use OCR text to detect ingredient mentions and use it as a model input. For optimal results, this field should be provided even if &#x60;ingredients_tags&#x60; is provided.  | [optional] 
**nutriments** | [**PredictCategoryPostRequestAnyOf1ProductNutriments**](PredictCategoryPostRequestAnyOf1ProductNutriments.md) |  | [optional] 

## Example

```python
from openapi_client.models.predict_category_post_request_any_of1_product import PredictCategoryPostRequestAnyOf1Product

# TODO update the JSON string below
json = "{}"
# create an instance of PredictCategoryPostRequestAnyOf1Product from a JSON string
predict_category_post_request_any_of1_product_instance = PredictCategoryPostRequestAnyOf1Product.from_json(json)
# print the JSON string representation of the object
print(PredictCategoryPostRequestAnyOf1Product.to_json())

# convert the object into a dict
predict_category_post_request_any_of1_product_dict = predict_category_post_request_any_of1_product_instance.to_dict()
# create an instance of PredictCategoryPostRequestAnyOf1Product from a dict
predict_category_post_request_any_of1_product_from_dict = PredictCategoryPostRequestAnyOf1Product.from_dict(predict_category_post_request_any_of1_product_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


