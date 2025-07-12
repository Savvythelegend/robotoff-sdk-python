# QuestionsBarcodeGet200Response


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**status** | **str** |  | [optional] 
**questions** | **List[object]** |  | [optional] 

## Example

```python
from openapi_client.models.questions_barcode_get200_response import QuestionsBarcodeGet200Response

# TODO update the JSON string below
json = "{}"
# create an instance of QuestionsBarcodeGet200Response from a JSON string
questions_barcode_get200_response_instance = QuestionsBarcodeGet200Response.from_json(json)
# print the JSON string representation of the object
print(QuestionsBarcodeGet200Response.to_json())

# convert the object into a dict
questions_barcode_get200_response_dict = questions_barcode_get200_response_instance.to_dict()
# create an instance of QuestionsBarcodeGet200Response from a dict
questions_barcode_get200_response_from_dict = QuestionsBarcodeGet200Response.from_dict(questions_barcode_get200_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


