# openapi_client.PredictionsApi

All URIs are relative to *https://robotoff.openfoodfacts.org/api/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**predictions_get**](PredictionsApi.md#predictions_get) | **GET** /predictions | Get predictions


# **predictions_get**
> PredictionsGet200Response predictions_get(count=count, page=page, server_type=server_type, barcode=barcode, types=types)

Get predictions

### Example


```python
import openapi_client
from openapi_client.models.predictions_get200_response import PredictionsGet200Response
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
    api_instance = openapi_client.PredictionsApi(api_client)
    count = 25 # int | The number of items to return (optional) (default to 25)
    page = 1 # int | Page index to return (starting at 1) (optional) (default to 1)
    server_type = off # str | The server type (=project) to use, such as 'off' (Open Food Facts), 'obf' (Open Beauty Facts),... (optional) (default to off)
    barcode = '5410041040807' # str | Filter by barcode value (optional)
    types = 'brand,label' # str | Comma-separated list, filter by prediction types (optional)

    try:
        # Get predictions
        api_response = api_instance.predictions_get(count=count, page=page, server_type=server_type, barcode=barcode, types=types)
        print("The response of PredictionsApi->predictions_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PredictionsApi->predictions_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **count** | **int**| The number of items to return | [optional] [default to 25]
 **page** | **int**| Page index to return (starting at 1) | [optional] [default to 1]
 **server_type** | **str**| The server type (&#x3D;project) to use, such as &#39;off&#39; (Open Food Facts), &#39;obf&#39; (Open Beauty Facts),... | [optional] [default to off]
 **barcode** | **str**| Filter by barcode value | [optional] 
 **types** | **str**| Comma-separated list, filter by prediction types | [optional] 

### Return type

[**PredictionsGet200Response**](PredictionsGet200Response.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The queried predictions |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

