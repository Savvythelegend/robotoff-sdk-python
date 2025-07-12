# ImagesLogosGet200Response


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**logos** | **List[str]** | Details about requested logos | 
**count** | **float** | Number of returned results | 

## Example

```python
from openapi_client.models.images_logos_get200_response import ImagesLogosGet200Response

# TODO update the JSON string below
json = "{}"
# create an instance of ImagesLogosGet200Response from a JSON string
images_logos_get200_response_instance = ImagesLogosGet200Response.from_json(json)
# print the JSON string representation of the object
print(ImagesLogosGet200Response.to_json())

# convert the object into a dict
images_logos_get200_response_dict = images_logos_get200_response_instance.to_dict()
# create an instance of ImagesLogosGet200Response from a dict
images_logos_get200_response_from_dict = ImagesLogosGet200Response.from_dict(images_logos_get200_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


