# openapi_client.LogosApi

All URIs are relative to *https://robotoff.openfoodfacts.org/api/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**images_logos_get**](LogosApi.md#images_logos_get) | **GET** /images/logos | Fetch logos
[**images_logos_logo_id_reset_post**](LogosApi.md#images_logos_logo_id_reset_post) | **POST** /images/logos/{logo_id}/reset | Reset logo annotation
[**images_logos_search_get**](LogosApi.md#images_logos_search_get) | **GET** /images/logos/search | Search for logos


# **images_logos_get**
> ImagesLogosGet200Response images_logos_get(logo_ids=logo_ids)

Fetch logos

Return details about requested logos (maximum 500 logos can be fetched per request).

### Example


```python
import openapi_client
from openapi_client.models.images_logos_get200_response import ImagesLogosGet200Response
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
    api_instance = openapi_client.LogosApi(api_client)
    logo_ids = 'logo_ids_example' # str | Comma-separated string of logo IDs (optional)

    try:
        # Fetch logos
        api_response = api_instance.images_logos_get(logo_ids=logo_ids)
        print("The response of LogosApi->images_logos_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling LogosApi->images_logos_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **logo_ids** | **str**| Comma-separated string of logo IDs | [optional] 

### Return type

[**ImagesLogosGet200Response**](ImagesLogosGet200Response.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The fetch results |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **images_logos_logo_id_reset_post**
> images_logos_logo_id_reset_post(logo_id)

Reset logo annotation

Reset logo annotations, and delete all annotation-associated predictions and insights

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
    api_instance = openapi_client.LogosApi(api_client)
    logo_id = 1 # int | The ID of the logo whose annotation to reset

    try:
        # Reset logo annotation
        api_instance.images_logos_logo_id_reset_post(logo_id)
    except Exception as e:
        print("Exception when calling LogosApi->images_logos_logo_id_reset_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **logo_id** | **int**| The ID of the logo whose annotation to reset | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**204** | HTTP 204 is returned if the reset operation was successful |  -  |
**404** | HTTP 404 is returned if the &#x60;logo_id&#x60; was not found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **images_logos_search_get**
> ImagesLogosSearchGet200Response images_logos_search_get(server_type=server_type, barcode=barcode, count=count, type=type, value=value, taxonomy_value=taxonomy_value, min_confidence=min_confidence, random=random, annotated=annotated)

Search for logos

Search for logos detected using the universal-logo-detector model that 
meet some criteria (annotation status, annotated, type,...)


### Example


```python
import openapi_client
from openapi_client.models.images_logos_search_get200_response import ImagesLogosSearchGet200Response
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
    api_instance = openapi_client.LogosApi(api_client)
    server_type = off # str | The server type (=project) to use, such as 'off' (Open Food Facts), 'obf' (Open Beauty Facts),... (optional) (default to off)
    barcode = '5410041040807' # str | Filter by barcode value (optional)
    count = 25 # float | Number of results to return (optional) (default to 25)
    type = 'packager_code' # str | Filter by logo type (optional)
    value = 'lidl' # str | Filter by annotated value (optional)
    taxonomy_value = 'en:organic' # str | Filter by taxonomy value, i.e. the canonical value present is the associated taxonomy. This parameter is mutually exclusive with `value`, and should be used for `label` type. (optional)
    min_confidence = 3.4 # float | Filter logos that have a confidence score above a threshold (optional)
    random = False # bool | If true, randomized result order (optional) (default to False)
    annotated = True # bool | The annotation status of the logo. If not provided, both annotated and non-annotated logos are returned (optional)

    try:
        # Search for logos
        api_response = api_instance.images_logos_search_get(server_type=server_type, barcode=barcode, count=count, type=type, value=value, taxonomy_value=taxonomy_value, min_confidence=min_confidence, random=random, annotated=annotated)
        print("The response of LogosApi->images_logos_search_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling LogosApi->images_logos_search_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **server_type** | **str**| The server type (&#x3D;project) to use, such as &#39;off&#39; (Open Food Facts), &#39;obf&#39; (Open Beauty Facts),... | [optional] [default to off]
 **barcode** | **str**| Filter by barcode value | [optional] 
 **count** | **float**| Number of results to return | [optional] [default to 25]
 **type** | **str**| Filter by logo type | [optional] 
 **value** | **str**| Filter by annotated value | [optional] 
 **taxonomy_value** | **str**| Filter by taxonomy value, i.e. the canonical value present is the associated taxonomy. This parameter is mutually exclusive with &#x60;value&#x60;, and should be used for &#x60;label&#x60; type. | [optional] 
 **min_confidence** | **float**| Filter logos that have a confidence score above a threshold | [optional] 
 **random** | **bool**| If true, randomized result order | [optional] [default to False]
 **annotated** | **bool**| The annotation status of the logo. If not provided, both annotated and non-annotated logos are returned | [optional] 

### Return type

[**ImagesLogosSearchGet200Response**](ImagesLogosSearchGet200Response.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The search results |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

