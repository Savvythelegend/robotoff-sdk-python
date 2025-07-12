# openapi_client.BatchJobApi

All URIs are relative to *https://robotoff.openfoodfacts.org/api/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**batch_import_post**](BatchJobApi.md#batch_import_post) | **POST** /batch/import | Import batch processed data to the Robotoff database.


# **batch_import_post**
> batch_import_post(job_type)

Import batch processed data to the Robotoff database.

Trigger import of the batch processed data to the Robotoff database. A `BATCH_JOB_KEY` is expected in the authorization header. This endpoint is mainly used by the batch job once the job is finished.

### Example

* Bearer Authentication (batch_job_key):

```python
import openapi_client
from openapi_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://robotoff.openfoodfacts.org/api/v1
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "https://robotoff.openfoodfacts.org/api/v1"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization: batch_job_key
configuration = openapi_client.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with openapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = openapi_client.BatchJobApi(api_client)
    job_type = 'job_type_example' # str | The type of batch job launched.

    try:
        # Import batch processed data to the Robotoff database.
        api_instance.batch_import_post(job_type)
    except Exception as e:
        print("Exception when calling BatchJobApi->batch_import_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **job_type** | **str**| The type of batch job launched. | 

### Return type

void (empty response body)

### Authorization

[batch_job_key](../README.md#batch_job_key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Data successfully imported. |  -  |
**400** | An HTTP 400 is returned if the authentification key is invalid or if the job_type is not supported. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

