# openapi_client.ANNApi

All URIs are relative to *https://robotoff.openfoodfacts.org/api/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**ann_search_get**](ANNApi.md#ann_search_get) | **GET** /ann/search | Approximate search for nearest neighbors of a random query logo
[**ann_search_logo_id_int_get**](ANNApi.md#ann_search_logo_id_int_get) | **GET** /ann/search/{logo_id:int} | Approximate search for nearest neighbors of a specified query logo


# **ann_search_get**
> LogoANNSearchResponse ann_search_get(count=count, server_type=server_type)

Approximate search for nearest neighbors of a random query logo

Return ID and distance of each logo found, the number of neighbors returned and the ID of the query logo.

### Example


```python
import openapi_client
from openapi_client.models.logo_ann_search_response import LogoANNSearchResponse
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
    api_instance = openapi_client.ANNApi(api_client)
    count = 25 # int | Number of neighbors to return (optional) (default to 25)
    server_type = off # str | The server type (=project) to use, such as 'off' (Open Food Facts), 'obf' (Open Beauty Facts),... (optional) (default to off)

    try:
        # Approximate search for nearest neighbors of a random query logo
        api_response = api_instance.ann_search_get(count=count, server_type=server_type)
        print("The response of ANNApi->ann_search_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ANNApi->ann_search_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **count** | **int**| Number of neighbors to return | [optional] [default to 25]
 **server_type** | **str**| The server type (&#x3D;project) to use, such as &#39;off&#39; (Open Food Facts), &#39;obf&#39; (Open Beauty Facts),... | [optional] [default to off]

### Return type

[**LogoANNSearchResponse**](LogoANNSearchResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Response from ANN search |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **ann_search_logo_id_int_get**
> LogoANNSearchResponse ann_search_logo_id_int_get(count=count, server_type=server_type)

Approximate search for nearest neighbors of a specified query logo

Return ID and distance of each logo found, the number of neighbors returned and the ID of the query logo.

### Example


```python
import openapi_client
from openapi_client.models.logo_ann_search_response import LogoANNSearchResponse
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
    api_instance = openapi_client.ANNApi(api_client)
    count = 25 # int | Number of neighbors to return (optional) (default to 25)
    server_type = off # str | The server type (=project) to use, such as 'off' (Open Food Facts), 'obf' (Open Beauty Facts),... (optional) (default to off)

    try:
        # Approximate search for nearest neighbors of a specified query logo
        api_response = api_instance.ann_search_logo_id_int_get(count=count, server_type=server_type)
        print("The response of ANNApi->ann_search_logo_id_int_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ANNApi->ann_search_logo_id_int_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **count** | **int**| Number of neighbors to return | [optional] [default to 25]
 **server_type** | **str**| The server type (&#x3D;project) to use, such as &#39;off&#39; (Open Food Facts), &#39;obf&#39; (Open Beauty Facts),... | [optional] [default to off]

### Return type

[**LogoANNSearchResponse**](LogoANNSearchResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Response from ANN search |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

