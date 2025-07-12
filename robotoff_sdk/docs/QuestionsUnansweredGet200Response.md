# QuestionsUnansweredGet200Response


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**count** | **int** | The total number of questions that meet the provided criteria | 
**questions** | [**List[QuestionsUnansweredGet200ResponseQuestionsInner]**](QuestionsUnansweredGet200ResponseQuestionsInner.md) |  | 
**status** | **str** | The request status | 

## Example

```python
from openapi_client.models.questions_unanswered_get200_response import QuestionsUnansweredGet200Response

# TODO update the JSON string below
json = "{}"
# create an instance of QuestionsUnansweredGet200Response from a JSON string
questions_unanswered_get200_response_instance = QuestionsUnansweredGet200Response.from_json(json)
# print the JSON string representation of the object
print(QuestionsUnansweredGet200Response.to_json())

# convert the object into a dict
questions_unanswered_get200_response_dict = questions_unanswered_get200_response_instance.to_dict()
# create an instance of QuestionsUnansweredGet200Response from a dict
questions_unanswered_get200_response_from_dict = QuestionsUnansweredGet200Response.from_dict(questions_unanswered_get200_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


