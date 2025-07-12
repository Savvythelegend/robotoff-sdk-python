# ImagesLogosSearchGet200Response


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**logos** | **List[str]** | Found logos | 
**count** | **float** | Number of returned results | 

## Example

```python
from openapi_client.models.images_logos_search_get200_response import ImagesLogosSearchGet200Response

# TODO update the JSON string below
json = "{}"
# create an instance of ImagesLogosSearchGet200Response from a JSON string
images_logos_search_get200_response_instance = ImagesLogosSearchGet200Response.from_json(json)
# print the JSON string representation of the object
print(ImagesLogosSearchGet200Response.to_json())

# convert the object into a dict
images_logos_search_get200_response_dict = images_logos_search_get200_response_instance.to_dict()
# create an instance of ImagesLogosSearchGet200Response from a dict
images_logos_search_get200_response_from_dict = ImagesLogosSearchGet200Response.from_dict(images_logos_search_get200_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


