# openapi_client.InsightsApi

All URIs are relative to *https://robotoff.openfoodfacts.org/api/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**insights_annotate_post**](InsightsApi.md#insights_annotate_post) | **POST** /insights/annotate | Submit an annotation
[**insights_barcode_get**](InsightsApi.md#insights_barcode_get) | **GET** /insights/{barcode} | Get all insights for a specific product, use GET /insights?barcode&#x3D;{barcode} instead
[**insights_detail_id_get**](InsightsApi.md#insights_detail_id_get) | **GET** /insights/detail/{id} | Get a specific insight
[**insights_dump_get**](InsightsApi.md#insights_dump_get) | **GET** /insights/dump | Generate a CSV dump
[**insights_get**](InsightsApi.md#insights_get) | **GET** /insights | List insights
[**insights_random_get**](InsightsApi.md#insights_random_get) | **GET** /insights/random | Get a random insight, use GET /insights?order_by&#x3D;random instead


# **insights_annotate_post**
> insights_annotate_post(insight_id, annotation, update=update, data=data)

Submit an annotation

The annotation can be submitted as an anonymous user or as a registered user.
If the user is anonymous, the annotation will be accounted as a vote, and several identical
anonymous votes are required to apply the insight. If the vote is sent from a registered user,
it is applied directly.

To send the annotation as a registered user, send Open Food Facts credentials to the API using
Basic Authentication: add a `Authorization: basic {ENCODED_BASE64}` header where `{ENCODED_BASE64}`
is an base64-encoded string of `user:password`. Don't provide an authentication header for anonymous
users.

The annotation is an integer that can take 4 values: `0`, `1`, `2`, `-1`. `0` means the insight is incorrect
(so it won't be applied), `1` means it is correct (so it will be applied) and `-1` means the insight
won't be returned to the user (_skip_). `2` is used when user submit some data to the annotate endpoint 
(for example in some cases of category annotation or ingredients spellcheck).

We use the voting mecanism system to remember which insight to skip for a user (authenticated or not).


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
    api_instance = openapi_client.InsightsApi(api_client)
    insight_id = 'insight_id_example' # str | ID of the insight
    annotation = 56 # int | Annotation of the prediction: 1 to accept the prediction, 0 to refuse it, and -1 for _skip_, 2 to accept and add data
    update = 1 # int | Send the update to Openfoodfacts if `update=1`, don't send the update otherwise. This parameter is useful if the update is performed client-side (optional) (default to 1)
    data = None # object | Additional data provided by the user as key-value pairs (optional)

    try:
        # Submit an annotation
        api_instance.insights_annotate_post(insight_id, annotation, update=update, data=data)
    except Exception as e:
        print("Exception when calling InsightsApi->insights_annotate_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **insight_id** | **str**| ID of the insight | 
 **annotation** | **int**| Annotation of the prediction: 1 to accept the prediction, 0 to refuse it, and -1 for _skip_, 2 to accept and add data | 
 **update** | **int**| Send the update to Openfoodfacts if &#x60;update&#x3D;1&#x60;, don&#39;t send the update otherwise. This parameter is useful if the update is performed client-side | [optional] [default to 1]
 **data** | [**object**](object.md)| Additional data provided by the user as key-value pairs | [optional] 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/x-www-form-urlencoded
 - **Accept**: Not defined

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **insights_barcode_get**
> insights_barcode_get(barcode, server_type=server_type)

Get all insights for a specific product, use GET /insights?barcode={barcode} instead

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
    api_instance = openapi_client.InsightsApi(api_client)
    barcode = 5410041040807 # int | The barcode of the product
    server_type = off # str | The server type (=project) to use, such as 'off' (Open Food Facts), 'obf' (Open Beauty Facts),... (optional) (default to off)

    try:
        # Get all insights for a specific product, use GET /insights?barcode={barcode} instead
        api_instance.insights_barcode_get(barcode, server_type=server_type)
    except Exception as e:
        print("Exception when calling InsightsApi->insights_barcode_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **barcode** | **int**| The barcode of the product | 
 **server_type** | **str**| The server type (&#x3D;project) to use, such as &#39;off&#39; (Open Food Facts), &#39;obf&#39; (Open Beauty Facts),... | [optional] [default to off]

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
**200** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **insights_detail_id_get**
> insights_detail_id_get(id)

Get a specific insight

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
    api_instance = openapi_client.InsightsApi(api_client)
    id = 'id_example' # str | ID of the insight

    try:
        # Get a specific insight
        api_instance.insights_detail_id_get(id)
    except Exception as e:
        print("Exception when calling InsightsApi->insights_detail_id_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| ID of the insight | 

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
**200** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **insights_dump_get**
> str insights_dump_get(server_type=server_type, value_tag=value_tag, insight_types=insight_types, barcode=barcode, annotated=annotated, count=count)

Generate a CSV dump

Generate a CSV dump of insights with specific criteria.
If more than 10,000 insights match provided criteria and `count` is not provided, a `HTTP 400` is returned


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
    api_instance = openapi_client.InsightsApi(api_client)
    server_type = off # str | The server type (=project) to use, such as 'off' (Open Food Facts), 'obf' (Open Beauty Facts),... (optional) (default to off)
    value_tag = 'en:organic' # str | Filter by value tag, i.e the value that is going to be sent to Product Opener (optional)
    insight_types = 'brand,label' # str | Comma-separated list, filter by insight types (optional)
    barcode = '5410041040807' # str | Filter by barcode value (optional)
    annotated = True # bool | The annotation status of the insight. If not provided, both annotated and non-annotated insights are returned (optional)
    count = 56 # int | Maximum number of insights to return. If not provided, an HTTP 400 response may be returned if more than 10,000 insights match the criteria (optional)

    try:
        # Generate a CSV dump
        api_response = api_instance.insights_dump_get(server_type=server_type, value_tag=value_tag, insight_types=insight_types, barcode=barcode, annotated=annotated, count=count)
        print("The response of InsightsApi->insights_dump_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling InsightsApi->insights_dump_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **server_type** | **str**| The server type (&#x3D;project) to use, such as &#39;off&#39; (Open Food Facts), &#39;obf&#39; (Open Beauty Facts),... | [optional] [default to off]
 **value_tag** | **str**| Filter by value tag, i.e the value that is going to be sent to Product Opener | [optional] 
 **insight_types** | **str**| Comma-separated list, filter by insight types | [optional] 
 **barcode** | **str**| Filter by barcode value | [optional] 
 **annotated** | **bool**| The annotation status of the insight. If not provided, both annotated and non-annotated insights are returned | [optional] 
 **count** | **int**| Maximum number of insights to return. If not provided, an HTTP 400 response may be returned if more than 10,000 insights match the criteria | [optional] 

### Return type

**str**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: text/csv

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The CSV dump |  -  |
**204** | HTTP 204 is returned if no insights were found |  -  |
**400** | HTTP 400 is returned if more than 10,000 insights match the criteria and &#x60;count&#x60; is not provided |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **insights_get**
> InsightsGet200Response insights_get(insight_types=insight_types, barcode=barcode, annotated=annotated, annotation=annotation, value_tag=value_tag, brands=brands, countries=countries, server_type=server_type, predictor=predictor, order_by=order_by, count=count, page=page, campaigns=campaigns, lc=lc)

List insights

### Example


```python
import openapi_client
from openapi_client.models.insights_get200_response import InsightsGet200Response
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
    api_instance = openapi_client.InsightsApi(api_client)
    insight_types = 'brand,label' # str | Comma-separated list, filter by insight types (optional)
    barcode = 5410041040807 # int | Filter by barcode value (optional)
    annotated = true # bool | Filter by annotation status of the insight. A true value (`1`, `true`) means we only return annotated insights, a false value (`0`, `false`) only non-annotated insights. If the parameter is not provided, both annotated and non-annotated insights are returned. (optional)
    annotation = 1 # int | Filter by annotation value of the insight. If not provided, all insights are returned. This works in conjunction with the `annotated` parameter. (optional)
    value_tag = 'en:organic' # str | Filter by value tag, i.e the value that is going to be sent to Product Opener (optional)
    brands = 'carrefour,ferrero' # str | Comma-separated list, filter by brands (optional)
    countries = 'uk' # str | Comma separated list, filter by country value (2-letter code) (optional)
    server_type = off # str | The server type (=project) to use, such as 'off' (Open Food Facts), 'obf' (Open Beauty Facts),... (optional) (default to off)
    predictor = 'universal-logo-detector' # str | Filter by predictor value A predictor refers to the model/method that was used to generate the prediction. (optional)
    order_by = 'popularity' # str | How to order by insight results. By default, results are not ordered. Possible values are:   - `random`: insights are ordered randomly   - `popularity`: insights are returned by decreasing popularity, using the number of scans as proxy  (optional)
    count = 25 # int | The number of items to return (optional) (default to 25)
    page = 1 # int | Page index to return (starting at 1) (optional) (default to 1)
    campaigns = 'agribalyse-category' # str | Filter by annotation campaigns (the insight must have all the campaigns) An annotation campaign allows to only retrieve questions or insights based on arbitrary criteria defined during insight import. (optional)
    lc = 'en,fr,de' # str | Comma-separated list of language codes to filter insights by language (optional)

    try:
        # List insights
        api_response = api_instance.insights_get(insight_types=insight_types, barcode=barcode, annotated=annotated, annotation=annotation, value_tag=value_tag, brands=brands, countries=countries, server_type=server_type, predictor=predictor, order_by=order_by, count=count, page=page, campaigns=campaigns, lc=lc)
        print("The response of InsightsApi->insights_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling InsightsApi->insights_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **insight_types** | **str**| Comma-separated list, filter by insight types | [optional] 
 **barcode** | **int**| Filter by barcode value | [optional] 
 **annotated** | **bool**| Filter by annotation status of the insight. A true value (&#x60;1&#x60;, &#x60;true&#x60;) means we only return annotated insights, a false value (&#x60;0&#x60;, &#x60;false&#x60;) only non-annotated insights. If the parameter is not provided, both annotated and non-annotated insights are returned. | [optional] 
 **annotation** | **int**| Filter by annotation value of the insight. If not provided, all insights are returned. This works in conjunction with the &#x60;annotated&#x60; parameter. | [optional] 
 **value_tag** | **str**| Filter by value tag, i.e the value that is going to be sent to Product Opener | [optional] 
 **brands** | **str**| Comma-separated list, filter by brands | [optional] 
 **countries** | **str**| Comma separated list, filter by country value (2-letter code) | [optional] 
 **server_type** | **str**| The server type (&#x3D;project) to use, such as &#39;off&#39; (Open Food Facts), &#39;obf&#39; (Open Beauty Facts),... | [optional] [default to off]
 **predictor** | **str**| Filter by predictor value A predictor refers to the model/method that was used to generate the prediction. | [optional] 
 **order_by** | **str**| How to order by insight results. By default, results are not ordered. Possible values are:   - &#x60;random&#x60;: insights are ordered randomly   - &#x60;popularity&#x60;: insights are returned by decreasing popularity, using the number of scans as proxy  | [optional] 
 **count** | **int**| The number of items to return | [optional] [default to 25]
 **page** | **int**| Page index to return (starting at 1) | [optional] [default to 1]
 **campaigns** | **str**| Filter by annotation campaigns (the insight must have all the campaigns) An annotation campaign allows to only retrieve questions or insights based on arbitrary criteria defined during insight import. | [optional] 
 **lc** | **str**| Comma-separated list of language codes to filter insights by language | [optional] 

### Return type

[**InsightsGet200Response**](InsightsGet200Response.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **insights_random_get**
> InsightsRandomGet200Response insights_random_get(type=type, countries=countries, value_tag=value_tag, server_type=server_type, count=count, predictor=predictor)

Get a random insight, use GET /insights?order_by=random instead

### Example


```python
import openapi_client
from openapi_client.models.insights_random_get200_response import InsightsRandomGet200Response
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
    api_instance = openapi_client.InsightsApi(api_client)
    type = 'type_example' # str | Filter by insight type (optional)
    countries = 'uk' # str | Comma separated list, filter by country value (2-letter code) (optional)
    value_tag = 'en:organic' # str | Filter by value tag, i.e the value that is going to be sent to Product Opener (optional)
    server_type = off # str | The server type (=project) to use, such as 'off' (Open Food Facts), 'obf' (Open Beauty Facts),... (optional) (default to off)
    count = 25 # int | The number of items to return (optional) (default to 25)
    predictor = 'universal-logo-detector' # str | Filter by predictor value A predictor refers to the model/method that was used to generate the prediction. (optional)

    try:
        # Get a random insight, use GET /insights?order_by=random instead
        api_response = api_instance.insights_random_get(type=type, countries=countries, value_tag=value_tag, server_type=server_type, count=count, predictor=predictor)
        print("The response of InsightsApi->insights_random_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling InsightsApi->insights_random_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **type** | **str**| Filter by insight type | [optional] 
 **countries** | **str**| Comma separated list, filter by country value (2-letter code) | [optional] 
 **value_tag** | **str**| Filter by value tag, i.e the value that is going to be sent to Product Opener | [optional] 
 **server_type** | **str**| The server type (&#x3D;project) to use, such as &#39;off&#39; (Open Food Facts), &#39;obf&#39; (Open Beauty Facts),... | [optional] [default to off]
 **count** | **int**| The number of items to return | [optional] [default to 25]
 **predictor** | **str**| Filter by predictor value A predictor refers to the model/method that was used to generate the prediction. | [optional] 

### Return type

[**InsightsRandomGet200Response**](InsightsRandomGet200Response.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

