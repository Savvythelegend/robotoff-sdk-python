# openapi_client.ImagePredictionsApi

All URIs are relative to *https://robotoff.openfoodfacts.org/api/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**image_predictions_get**](ImagePredictionsApi.md#image_predictions_get) | **GET** /image_predictions | Get image predictions


# **image_predictions_get**
> ImagePredictionsGet200Response image_predictions_get(count=count, page=page, server_type=server_type, barcode=barcode, with_logo=with_logo, model_name=model_name, image_id=image_id, type=type, model_version=model_version, min_confidence=min_confidence)

Get image predictions

### Example


```python
import openapi_client
from openapi_client.models.image_predictions_get200_response import ImagePredictionsGet200Response
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
    api_instance = openapi_client.ImagePredictionsApi(api_client)
    count = 25 # int | The number of items to return (optional) (default to 25)
    page = 1 # int | Page index to return (starting at 1) (optional) (default to 1)
    server_type = off # str | The server type (=project) to use, such as 'off' (Open Food Facts), 'obf' (Open Beauty Facts),... (optional) (default to off)
    barcode = '5410041040807' # str | Filter by barcode value (optional)
    with_logo = True # bool | if True, only return image predictions that have associated logos (only valid for universal-logo-detector image predictions). If false, only return image predictions that have no associated logos. Otherwise, return all image predictions. (optional)
    model_name = 'universal-logo-detector' # str | filter by name of the image predictor model (optional)
    image_id = '1' # str | filter by image ID. It should be a digit (raw images only), otherwise no result will be returned. (optional)
    type = 'object_detection' # str | filter by type of the image predictor model (optional)
    model_version = 'model_version_example' # str | filter by model version value (optional)
    min_confidence = 3.4 # float | filter by minimum confidence score value (optional)

    try:
        # Get image predictions
        api_response = api_instance.image_predictions_get(count=count, page=page, server_type=server_type, barcode=barcode, with_logo=with_logo, model_name=model_name, image_id=image_id, type=type, model_version=model_version, min_confidence=min_confidence)
        print("The response of ImagePredictionsApi->image_predictions_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ImagePredictionsApi->image_predictions_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **count** | **int**| The number of items to return | [optional] [default to 25]
 **page** | **int**| Page index to return (starting at 1) | [optional] [default to 1]
 **server_type** | **str**| The server type (&#x3D;project) to use, such as &#39;off&#39; (Open Food Facts), &#39;obf&#39; (Open Beauty Facts),... | [optional] [default to off]
 **barcode** | **str**| Filter by barcode value | [optional] 
 **with_logo** | **bool**| if True, only return image predictions that have associated logos (only valid for universal-logo-detector image predictions). If false, only return image predictions that have no associated logos. Otherwise, return all image predictions. | [optional] 
 **model_name** | **str**| filter by name of the image predictor model | [optional] 
 **image_id** | **str**| filter by image ID. It should be a digit (raw images only), otherwise no result will be returned. | [optional] 
 **type** | **str**| filter by type of the image predictor model | [optional] 
 **model_version** | **str**| filter by model version value | [optional] 
 **min_confidence** | **float**| filter by minimum confidence score value | [optional] 

### Return type

[**ImagePredictionsGet200Response**](ImagePredictionsGet200Response.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The queried image predictions |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

