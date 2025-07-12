# openapi_client.ImagesApi

All URIs are relative to *https://robotoff.openfoodfacts.org/api/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**images_crop_get**](ImagesApi.md#images_crop_get) | **GET** /images/crop | Crop an image


# **images_crop_get**
> bytearray images_crop_get(image_url=image_url, y_min=y_min, x_min=x_min, y_max=y_max, x_max=x_max)

Crop an image

This endpoint is currently only used to generate cropped logos on Hunger Games from a
base image and cropping coordinates. Cropping coordinates are relative (between 0.
and 1. inclusive), with (0, 0) being the upper left corner.


### Example


```python
import openapi_client
from openapi_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://robotoff.openfoodfacts.org/api/v1
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "https://robotoff.openfoodfacts.org/api/v1"
)


# Enter a context with an instance of the API client
with openapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = openapi_client.ImagesApi(api_client)
    image_url = 'https://images.openfoodfacts.org/images/products/541/004/104/0807/3.jpg' # str | The URL of the input image (optional)
    y_min = 0.47795143723487854 # float |  (optional)
    x_min = 0.5583494305610657 # float |  (optional)
    y_max = 0.5653171539306641 # float |  (optional)
    x_max = 0.6795185804367065 # float |  (optional)

    try:
        # Crop an image
        api_response = api_instance.images_crop_get(image_url=image_url, y_min=y_min, x_min=x_min, y_max=y_max, x_max=x_max)
        print("The response of ImagesApi->images_crop_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ImagesApi->images_crop_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **image_url** | **str**| The URL of the input image | [optional] 
 **y_min** | **float**|  | [optional] 
 **x_min** | **float**|  | [optional] 
 **y_max** | **float**|  | [optional] 
 **x_max** | **float**|  | [optional] 

### Return type

**bytearray**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: image/jpeg

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

