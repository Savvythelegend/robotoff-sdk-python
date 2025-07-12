# openapi_client.PredictApi

All URIs are relative to *https://robotoff.openfoodfacts.org/api/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**predict_category_post**](PredictApi.md#predict_category_post) | **POST** /predict/category | Predict categories for a product
[**predict_lang_get**](PredictApi.md#predict_lang_get) | **GET** /predict/lang | Predict the language of a text
[**predict_lang_product_get**](PredictApi.md#predict_lang_product_get) | **GET** /predict/lang/product | Predict the languages of the product
[**predict_nutrition_get**](PredictApi.md#predict_nutrition_get) | **GET** /predict/nutrition | Extract nutritional information from an image
[**predict_ocr_prediction_get**](PredictApi.md#predict_ocr_prediction_get) | **GET** /predict/ocr_prediction | Generate OCR predictions an OCR JSON


# **predict_category_post**
> PredictCategoryPost200Response predict_category_post(predict_category_post_request=predict_category_post_request)

Predict categories for a product

Predictions are performed using a neural model.
As input, you can either provide:

- the `barcode` of a product: Robotoff will fetch the product from
  Product Opener and will use this data as inputs to predict categories.
- expected inputs under a `product` key. The neural category model
  accepts the following fields as input: `product_name`, `ingredients_tags`,
  `ocr`, `nutriments`, `image_embeddings`. All fields are optional (but you should at least provide one).


### Example


```python
import openapi_client
from openapi_client.models.predict_category_post200_response import PredictCategoryPost200Response
from openapi_client.models.predict_category_post_request import PredictCategoryPostRequest
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
    api_instance = openapi_client.PredictApi(api_client)
    predict_category_post_request = openapi_client.PredictCategoryPostRequest() # PredictCategoryPostRequest |  (optional)

    try:
        # Predict categories for a product
        api_response = api_instance.predict_category_post(predict_category_post_request=predict_category_post_request)
        print("The response of PredictApi->predict_category_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PredictApi->predict_category_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **predict_category_post_request** | [**PredictCategoryPostRequest**](PredictCategoryPostRequest.md)|  | [optional] 

### Return type

[**PredictCategoryPost200Response**](PredictCategoryPost200Response.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | the category predictions |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **predict_lang_get**
> PredictLangGet200Response predict_lang_get(text, k=k, threshold=threshold)

Predict the language of a text

Predict the language of a text using a neural model.
A POST version of this endpoint is also available, it accepts a JSON body with exactly the
same parameters.

Use the POST version if you want to predict the language of a long text, as the GET version
has a limit on the length of the text that can be provided.


### Example


```python
import openapi_client
from openapi_client.models.predict_lang_get200_response import PredictLangGet200Response
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
    api_instance = openapi_client.PredictApi(api_client)
    text = 'hello world' # str | The text to predict language of
    k = 10 # int | the number of predictions to return  (optional) (default to 10)
    threshold = 0.01 # float | the minimum probability for a language to be returned  (optional) (default to 0.01)

    try:
        # Predict the language of a text
        api_response = api_instance.predict_lang_get(text, k=k, threshold=threshold)
        print("The response of PredictApi->predict_lang_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PredictApi->predict_lang_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **text** | **str**| The text to predict language of | 
 **k** | **int**| the number of predictions to return  | [optional] [default to 10]
 **threshold** | **float**| the minimum probability for a language to be returned  | [optional] [default to 0.01]

### Return type

[**PredictLangGet200Response**](PredictLangGet200Response.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | the predicted languages |  -  |
**400** | An HTTP 400 is returned if the provided parameters are invalid |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **predict_lang_product_get**
> PredictLangProductGet200Response predict_lang_product_get(barcode, server_type=server_type)

Predict the languages of the product

Return the most common languages present on the product images, based on word-level
language detection from product images.

Language detection is not performed on the fly, but is based on predictions of type
`image_lang` stored in the `prediction` table.


### Example


```python
import openapi_client
from openapi_client.models.predict_lang_product_get200_response import PredictLangProductGet200Response
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
    api_instance = openapi_client.PredictApi(api_client)
    barcode = 5410041040807 # int | The barcode of the product
    server_type = off # str | The server type (=project) to use, such as 'off' (Open Food Facts), 'obf' (Open Beauty Facts),... (optional) (default to off)

    try:
        # Predict the languages of the product
        api_response = api_instance.predict_lang_product_get(barcode, server_type=server_type)
        print("The response of PredictApi->predict_lang_product_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PredictApi->predict_lang_product_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **barcode** | **int**| The barcode of the product | 
 **server_type** | **str**| The server type (&#x3D;project) to use, such as &#39;off&#39; (Open Food Facts), &#39;obf&#39; (Open Beauty Facts),... | [optional] [default to off]

### Return type

[**PredictLangProductGet200Response**](PredictLangProductGet200Response.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The predicted languages, sorted by descending probability.  |  -  |
**400** | An HTTP 400 is returned if the provided parameters are invalid |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **predict_nutrition_get**
> PredictNutritionGet200Response predict_nutrition_get(image_url=image_url, ocr_url=ocr_url)

Extract nutritional information from an image

Predict nutritional information from a packaging image using the Nutri-Sight model.

The model takes an image and the OCR result (as a JSON file) obtained from Google Cloud Vision.
For more information about the model, see the
[Nutri-Sight documentation](https://openfoodfacts.github.io/robotoff/references/predictions/nutrient-extraction/).


### Example


```python
import openapi_client
from openapi_client.models.predict_nutrition_get200_response import PredictNutritionGet200Response
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
    api_instance = openapi_client.PredictApi(api_client)
    image_url = 'https://images.openfoodfacts.org/images/products/541/004/104/0807/3.jpg' # str | The URL of the input image (optional)
    ocr_url = 'https://images.openfoodfacts.org/images/products/541/004/104/0807/3.json' # str | The URL of the OCR JSON to use. The OCR must have been extracted using Google Cloud Vision, and be in the JSON format. (optional)

    try:
        # Extract nutritional information from an image
        api_response = api_instance.predict_nutrition_get(image_url=image_url, ocr_url=ocr_url)
        print("The response of PredictApi->predict_nutrition_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PredictApi->predict_nutrition_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **image_url** | **str**| The URL of the input image | [optional] 
 **ocr_url** | **str**| The URL of the OCR JSON to use. The OCR must have been extracted using Google Cloud Vision, and be in the JSON format. | [optional] 

### Return type

[**PredictNutritionGet200Response**](PredictNutritionGet200Response.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | the extracted nutritional information |  -  |
**400** | An HTTP 400 is returned if the provided parameters are invalid |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **predict_ocr_prediction_get**
> SuccessfulResponse predict_ocr_prediction_get(ocr_url, server_type=server_type, prediction_types=prediction_types)

Generate OCR predictions an OCR JSON

### Example


```python
import openapi_client
from openapi_client.models.successful_response import SuccessfulResponse
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
    api_instance = openapi_client.PredictApi(api_client)
    ocr_url = 'https://static.openfoodfacts.org/images/products/216/124/000/3089/1.json' # str | The URL of the OCR JSON to use for extraction
    server_type = off # str | The server type (=project) to use, such as 'off' (Open Food Facts), 'obf' (Open Beauty Facts),... (optional) (default to off)
    prediction_types = 'category,label' # str | a comma-separated list of prediction types to use for extraction. If not provided, we use the default: set of OCR prediction types (see `DEFAULT_OCR_PREDICTION_TYPES` variable in Robotoff codebase)  (optional)

    try:
        # Generate OCR predictions an OCR JSON
        api_response = api_instance.predict_ocr_prediction_get(ocr_url, server_type=server_type, prediction_types=prediction_types)
        print("The response of PredictApi->predict_ocr_prediction_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PredictApi->predict_ocr_prediction_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **ocr_url** | **str**| The URL of the OCR JSON to use for extraction | 
 **server_type** | **str**| The server type (&#x3D;project) to use, such as &#39;off&#39; (Open Food Facts), &#39;obf&#39; (Open Beauty Facts),... | [optional] [default to off]
 **prediction_types** | **str**| a comma-separated list of prediction types to use for extraction. If not provided, we use the default: set of OCR prediction types (see &#x60;DEFAULT_OCR_PREDICTION_TYPES&#x60; variable in Robotoff codebase)  | [optional] 

### Return type

[**SuccessfulResponse**](SuccessfulResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | the extracted predictions |  -  |
**400** | An HTTP 400 is returned if the provided parameters are invalid |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

