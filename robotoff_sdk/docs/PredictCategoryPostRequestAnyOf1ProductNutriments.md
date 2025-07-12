# PredictCategoryPostRequestAnyOf1ProductNutriments

Nutriment values. These fields have exactly the same meaning as those of Product Opener. All fields are optional, only send data for the field for which the value is not missing. 

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**fat_100g** | **float** |  | [optional] 
**saturated_fat_100g** | **float** |  | [optional] 
**carbohydrates_100g** | **float** |  | [optional] 
**sugars_100g** | **float** |  | [optional] 
**fiber_100g** | **float** |  | [optional] 
**proteins_100g** | **float** |  | [optional] 
**salt_100g** | **float** |  | [optional] 
**energy_kcal_100g** | **float** |  | [optional] 
**fruits_vegetables_nuts_100g** | **float** |  | [optional] 

## Example

```python
from openapi_client.models.predict_category_post_request_any_of1_product_nutriments import PredictCategoryPostRequestAnyOf1ProductNutriments

# TODO update the JSON string below
json = "{}"
# create an instance of PredictCategoryPostRequestAnyOf1ProductNutriments from a JSON string
predict_category_post_request_any_of1_product_nutriments_instance = PredictCategoryPostRequestAnyOf1ProductNutriments.from_json(json)
# print the JSON string representation of the object
print(PredictCategoryPostRequestAnyOf1ProductNutriments.to_json())

# convert the object into a dict
predict_category_post_request_any_of1_product_nutriments_dict = predict_category_post_request_any_of1_product_nutriments_instance.to_dict()
# create an instance of PredictCategoryPostRequestAnyOf1ProductNutriments from a dict
predict_category_post_request_any_of1_product_nutriments_from_dict = PredictCategoryPostRequestAnyOf1ProductNutriments.from_dict(predict_category_post_request_any_of1_product_nutriments_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


