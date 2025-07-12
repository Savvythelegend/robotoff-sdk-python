# openapi_client.QuestionsApi

All URIs are relative to *https://robotoff.openfoodfacts.org/api/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**questions_barcode_get**](QuestionsApi.md#questions_barcode_get) | **GET** /questions/{barcode} | Get questions for a given product
[**questions_get**](QuestionsApi.md#questions_get) | **GET** /questions | Fetch questions
[**questions_popular_get**](QuestionsApi.md#questions_popular_get) | **GET** /questions/popular | Get questions about popular products
[**questions_random_get**](QuestionsApi.md#questions_random_get) | **GET** /questions/random | Get random questions
[**questions_unanswered_get**](QuestionsApi.md#questions_unanswered_get) | **GET** /questions/unanswered | Get unanswered question counts


# **questions_barcode_get**
> QuestionsBarcodeGet200Response questions_barcode_get(barcode, count=count, server_type=server_type, lang=lang, insight_types=insight_types)

Get questions for a given product

Questions are sorted by priority: we want questions with highest impact to be displayed first. The order is the following:
  - category
  - label
  - brand
  - remaining types


### Example


```python
import openapi_client
from openapi_client.models.questions_barcode_get200_response import QuestionsBarcodeGet200Response
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
    api_instance = openapi_client.QuestionsApi(api_client)
    barcode = 5410041040807 # int | The barcode of the product
    count = 1 # int | The number of questions to return (optional) (default to 1)
    server_type = off # str | The server type (=project) to use, such as 'off' (Open Food Facts), 'obf' (Open Beauty Facts),... (optional) (default to off)
    lang = 'en' # str | The language of the question/value (optional) (default to 'en')
    insight_types = 'brand,label' # str | Comma-separated list, filter by insight types (optional)

    try:
        # Get questions for a given product
        api_response = api_instance.questions_barcode_get(barcode, count=count, server_type=server_type, lang=lang, insight_types=insight_types)
        print("The response of QuestionsApi->questions_barcode_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling QuestionsApi->questions_barcode_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **barcode** | **int**| The barcode of the product | 
 **count** | **int**| The number of questions to return | [optional] [default to 1]
 **server_type** | **str**| The server type (&#x3D;project) to use, such as &#39;off&#39; (Open Food Facts), &#39;obf&#39; (Open Beauty Facts),... | [optional] [default to off]
 **lang** | **str**| The language of the question/value | [optional] [default to &#39;en&#39;]
 **insight_types** | **str**| Comma-separated list, filter by insight types | [optional] 

### Return type

[**QuestionsBarcodeGet200Response**](QuestionsBarcodeGet200Response.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Questions about the requested product |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **questions_get**
> QuestionsGet200Response questions_get(lang=lang, count=count, server_type=server_type, insight_types=insight_types, countries=countries, brands=brands, value_tag=value_tag, page=page, reserved_barcode=reserved_barcode, campaigns=campaigns, predictor=predictor, order_by=order_by)

Fetch questions

### Example


```python
import openapi_client
from openapi_client.models.questions_get200_response import QuestionsGet200Response
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
    api_instance = openapi_client.QuestionsApi(api_client)
    lang = 'en' # str | The language of the question/value (optional) (default to 'en')
    count = 25 # int | The number of items to return (optional) (default to 25)
    server_type = off # str | The server type (=project) to use, such as 'off' (Open Food Facts), 'obf' (Open Beauty Facts),... (optional) (default to off)
    insight_types = 'brand,label' # str | Comma-separated list, filter by insight types (optional)
    countries = 'uk' # str | Comma separated list, filter by country value (2-letter code) (optional)
    brands = 'carrefour,ferrero' # str | Comma-separated list, filter by brands (optional)
    value_tag = 'en:organic' # str | Filter by value tag, i.e the value that is going to be sent to Product Opener (optional)
    page = 1 # int | Page index to return (starting at 1) (optional) (default to 1)
    reserved_barcode = False # bool | If true, also return questions about products with reserved barcodes (optional) (default to False)
    campaigns = 'agribalyse-category' # str | Filter by annotation campaigns (the insight must have all the campaigns) An annotation campaign allows to only retrieve questions or insights based on arbitrary criteria defined during insight import. (optional)
    predictor = 'universal-logo-detector' # str | Filter by predictor value A predictor refers to the model/method that was used to generate the prediction. (optional)
    order_by = popularity # str | The field to use for ordering results:   - confidence: order by (descending) model confidence, null confidence insights come last   - popularity: order by (descending) popularity (=scan count)   - random: use a random order  (optional) (default to popularity)

    try:
        # Fetch questions
        api_response = api_instance.questions_get(lang=lang, count=count, server_type=server_type, insight_types=insight_types, countries=countries, brands=brands, value_tag=value_tag, page=page, reserved_barcode=reserved_barcode, campaigns=campaigns, predictor=predictor, order_by=order_by)
        print("The response of QuestionsApi->questions_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling QuestionsApi->questions_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **lang** | **str**| The language of the question/value | [optional] [default to &#39;en&#39;]
 **count** | **int**| The number of items to return | [optional] [default to 25]
 **server_type** | **str**| The server type (&#x3D;project) to use, such as &#39;off&#39; (Open Food Facts), &#39;obf&#39; (Open Beauty Facts),... | [optional] [default to off]
 **insight_types** | **str**| Comma-separated list, filter by insight types | [optional] 
 **countries** | **str**| Comma separated list, filter by country value (2-letter code) | [optional] 
 **brands** | **str**| Comma-separated list, filter by brands | [optional] 
 **value_tag** | **str**| Filter by value tag, i.e the value that is going to be sent to Product Opener | [optional] 
 **page** | **int**| Page index to return (starting at 1) | [optional] [default to 1]
 **reserved_barcode** | **bool**| If true, also return questions about products with reserved barcodes | [optional] [default to False]
 **campaigns** | **str**| Filter by annotation campaigns (the insight must have all the campaigns) An annotation campaign allows to only retrieve questions or insights based on arbitrary criteria defined during insight import. | [optional] 
 **predictor** | **str**| Filter by predictor value A predictor refers to the model/method that was used to generate the prediction. | [optional] 
 **order_by** | **str**| The field to use for ordering results:   - confidence: order by (descending) model confidence, null confidence insights come last   - popularity: order by (descending) popularity (&#x3D;scan count)   - random: use a random order  | [optional] [default to popularity]

### Return type

[**QuestionsGet200Response**](QuestionsGet200Response.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The questions matching the filters |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **questions_popular_get**
> questions_popular_get(lang=lang, count=count, server_type=server_type, insight_types=insight_types, countries=countries, brands=brands, value_tag=value_tag, page=page, reserved_barcode=reserved_barcode, campaigns=campaigns, predictor=predictor)

Get questions about popular products

Questions are ranked by the product popularity (based on scan count).


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
    api_instance = openapi_client.QuestionsApi(api_client)
    lang = 'en' # str | The language of the question/value (optional) (default to 'en')
    count = 25 # int | The number of items to return (optional) (default to 25)
    server_type = off # str | The server type (=project) to use, such as 'off' (Open Food Facts), 'obf' (Open Beauty Facts),... (optional) (default to off)
    insight_types = 'brand,label' # str | Comma-separated list, filter by insight types (optional)
    countries = 'uk' # str | Comma separated list, filter by country value (2-letter code) (optional)
    brands = 'carrefour,ferrero' # str | Comma-separated list, filter by brands (optional)
    value_tag = 'en:organic' # str | Filter by value tag, i.e the value that is going to be sent to Product Opener (optional)
    page = 1 # int | Page index to return (starting at 1) (optional) (default to 1)
    reserved_barcode = False # bool | If true, also return questions about products with reserved barcodes (optional) (default to False)
    campaigns = 'agribalyse-category' # str | Filter by annotation campaigns (the insight must have all the campaigns) An annotation campaign allows to only retrieve questions or insights based on arbitrary criteria defined during insight import. (optional)
    predictor = 'universal-logo-detector' # str | Filter by predictor value A predictor refers to the model/method that was used to generate the prediction. (optional)

    try:
        # Get questions about popular products
        api_instance.questions_popular_get(lang=lang, count=count, server_type=server_type, insight_types=insight_types, countries=countries, brands=brands, value_tag=value_tag, page=page, reserved_barcode=reserved_barcode, campaigns=campaigns, predictor=predictor)
    except Exception as e:
        print("Exception when calling QuestionsApi->questions_popular_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **lang** | **str**| The language of the question/value | [optional] [default to &#39;en&#39;]
 **count** | **int**| The number of items to return | [optional] [default to 25]
 **server_type** | **str**| The server type (&#x3D;project) to use, such as &#39;off&#39; (Open Food Facts), &#39;obf&#39; (Open Beauty Facts),... | [optional] [default to off]
 **insight_types** | **str**| Comma-separated list, filter by insight types | [optional] 
 **countries** | **str**| Comma separated list, filter by country value (2-letter code) | [optional] 
 **brands** | **str**| Comma-separated list, filter by brands | [optional] 
 **value_tag** | **str**| Filter by value tag, i.e the value that is going to be sent to Product Opener | [optional] 
 **page** | **int**| Page index to return (starting at 1) | [optional] [default to 1]
 **reserved_barcode** | **bool**| If true, also return questions about products with reserved barcodes | [optional] [default to False]
 **campaigns** | **str**| Filter by annotation campaigns (the insight must have all the campaigns) An annotation campaign allows to only retrieve questions or insights based on arbitrary criteria defined during insight import. | [optional] 
 **predictor** | **str**| Filter by predictor value A predictor refers to the model/method that was used to generate the prediction. | [optional] 

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

# **questions_random_get**
> QuestionsGet200Response questions_random_get(lang=lang, count=count, server_type=server_type, insight_types=insight_types, countries=countries, brands=brands, value_tag=value_tag, page=page, reserved_barcode=reserved_barcode, campaigns=campaigns, predictor=predictor)

Get random questions

### Example


```python
import openapi_client
from openapi_client.models.questions_get200_response import QuestionsGet200Response
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
    api_instance = openapi_client.QuestionsApi(api_client)
    lang = 'en' # str | The language of the question/value (optional) (default to 'en')
    count = 25 # int | The number of items to return (optional) (default to 25)
    server_type = off # str | The server type (=project) to use, such as 'off' (Open Food Facts), 'obf' (Open Beauty Facts),... (optional) (default to off)
    insight_types = 'brand,label' # str | Comma-separated list, filter by insight types (optional)
    countries = 'uk' # str | Comma separated list, filter by country value (2-letter code) (optional)
    brands = 'carrefour,ferrero' # str | Comma-separated list, filter by brands (optional)
    value_tag = 'en:organic' # str | Filter by value tag, i.e the value that is going to be sent to Product Opener (optional)
    page = 1 # int | Page index to return (starting at 1) (optional) (default to 1)
    reserved_barcode = False # bool | If true, also return questions about products with reserved barcodes (optional) (default to False)
    campaigns = 'agribalyse-category' # str | Filter by annotation campaigns (the insight must have all the campaigns) An annotation campaign allows to only retrieve questions or insights based on arbitrary criteria defined during insight import. (optional)
    predictor = 'universal-logo-detector' # str | Filter by predictor value A predictor refers to the model/method that was used to generate the prediction. (optional)

    try:
        # Get random questions
        api_response = api_instance.questions_random_get(lang=lang, count=count, server_type=server_type, insight_types=insight_types, countries=countries, brands=brands, value_tag=value_tag, page=page, reserved_barcode=reserved_barcode, campaigns=campaigns, predictor=predictor)
        print("The response of QuestionsApi->questions_random_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling QuestionsApi->questions_random_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **lang** | **str**| The language of the question/value | [optional] [default to &#39;en&#39;]
 **count** | **int**| The number of items to return | [optional] [default to 25]
 **server_type** | **str**| The server type (&#x3D;project) to use, such as &#39;off&#39; (Open Food Facts), &#39;obf&#39; (Open Beauty Facts),... | [optional] [default to off]
 **insight_types** | **str**| Comma-separated list, filter by insight types | [optional] 
 **countries** | **str**| Comma separated list, filter by country value (2-letter code) | [optional] 
 **brands** | **str**| Comma-separated list, filter by brands | [optional] 
 **value_tag** | **str**| Filter by value tag, i.e the value that is going to be sent to Product Opener | [optional] 
 **page** | **int**| Page index to return (starting at 1) | [optional] [default to 1]
 **reserved_barcode** | **bool**| If true, also return questions about products with reserved barcodes | [optional] [default to False]
 **campaigns** | **str**| Filter by annotation campaigns (the insight must have all the campaigns) An annotation campaign allows to only retrieve questions or insights based on arbitrary criteria defined during insight import. | [optional] 
 **predictor** | **str**| Filter by predictor value A predictor refers to the model/method that was used to generate the prediction. | [optional] 

### Return type

[**QuestionsGet200Response**](QuestionsGet200Response.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The queried insights |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **questions_unanswered_get**
> QuestionsUnansweredGet200Response questions_unanswered_get(count=count, server_type=server_type, type=type, countries=countries, page=page, reserved_barcode=reserved_barcode, campaigns=campaigns, predictor=predictor)

Get unanswered question counts

Get number of unanswered questions grouped by `value_tag`.
The list is ordered from highest count to lowest.


### Example


```python
import openapi_client
from openapi_client.models.questions_unanswered_get200_response import QuestionsUnansweredGet200Response
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
    api_instance = openapi_client.QuestionsApi(api_client)
    count = 25 # float | The number of distinct `value_tag`s to return (optional) (default to 25)
    server_type = off # str | The server type (=project) to use, such as 'off' (Open Food Facts), 'obf' (Open Beauty Facts),... (optional) (default to off)
    type = 'type_example' # str | Filter by insight type (optional)
    countries = 'uk' # str | Comma separated list, filter by country value (2-letter code) (optional)
    page = 1 # int | Page index to return (starting at 1) (optional) (default to 1)
    reserved_barcode = False # bool | If true, also return questions about products with reserved barcodes (optional) (default to False)
    campaigns = 'agribalyse-category' # str | Filter by annotation campaigns (the insight must have all the campaigns) An annotation campaign allows to only retrieve questions or insights based on arbitrary criteria defined during insight import. (optional)
    predictor = 'universal-logo-detector' # str | Filter by predictor value A predictor refers to the model/method that was used to generate the prediction. (optional)

    try:
        # Get unanswered question counts
        api_response = api_instance.questions_unanswered_get(count=count, server_type=server_type, type=type, countries=countries, page=page, reserved_barcode=reserved_barcode, campaigns=campaigns, predictor=predictor)
        print("The response of QuestionsApi->questions_unanswered_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling QuestionsApi->questions_unanswered_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **count** | **float**| The number of distinct &#x60;value_tag&#x60;s to return | [optional] [default to 25]
 **server_type** | **str**| The server type (&#x3D;project) to use, such as &#39;off&#39; (Open Food Facts), &#39;obf&#39; (Open Beauty Facts),... | [optional] [default to off]
 **type** | **str**| Filter by insight type | [optional] 
 **countries** | **str**| Comma separated list, filter by country value (2-letter code) | [optional] 
 **page** | **int**| Page index to return (starting at 1) | [optional] [default to 1]
 **reserved_barcode** | **bool**| If true, also return questions about products with reserved barcodes | [optional] [default to False]
 **campaigns** | **str**| Filter by annotation campaigns (the insight must have all the campaigns) An annotation campaign allows to only retrieve questions or insights based on arbitrary criteria defined during insight import. | [optional] 
 **predictor** | **str**| Filter by predictor value A predictor refers to the model/method that was used to generate the prediction. | [optional] 

### Return type

[**QuestionsUnansweredGet200Response**](QuestionsUnansweredGet200Response.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The number of questions grouped by &#x60;value_tag&#x60; |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

