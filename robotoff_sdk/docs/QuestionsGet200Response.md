# QuestionsGet200Response


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**status** | **str** |  | [optional] 
**questions** | **List[object]** |  | [optional] 
**count** | **int** | The total number of results with the provided filters | [optional] 

## Example

```python
from openapi_client.models.questions_get200_response import QuestionsGet200Response

# TODO update the JSON string below
json = "{}"
# create an instance of QuestionsGet200Response from a JSON string
questions_get200_response_instance = QuestionsGet200Response.from_json(json)
# print the JSON string representation of the object
print(QuestionsGet200Response.to_json())

# convert the object into a dict
questions_get200_response_dict = questions_get200_response_instance.to_dict()
# create an instance of QuestionsGet200Response from a dict
questions_get200_response_from_dict = QuestionsGet200Response.from_dict(questions_get200_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


