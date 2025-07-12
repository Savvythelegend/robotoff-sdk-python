# SuccessfulResponse

the extracted predictions

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**predictions** | [**List[Prediction]**](Prediction.md) | a list of extracted predictions | 

## Example

```python
from openapi_client.models.successful_response import SuccessfulResponse

# TODO update the JSON string below
json = "{}"
# create an instance of SuccessfulResponse from a JSON string
successful_response_instance = SuccessfulResponse.from_json(json)
# print the JSON string representation of the object
print(SuccessfulResponse.to_json())

# convert the object into a dict
successful_response_dict = successful_response_instance.to_dict()
# create an instance of SuccessfulResponse from a dict
successful_response_from_dict = SuccessfulResponse.from_dict(successful_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


