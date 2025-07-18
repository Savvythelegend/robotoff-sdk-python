# coding: utf-8

# flake8: noqa

"""
    API Reference

    Robotoff provides a simple API allowing consumers to fetch predictions and annotate them.  All endpoints must be prefixed with `/api/v1`. The full URL is `https://robotoff.openfoodfacts.org/api/v1/{endpoint}`. 

    The version of the OpenAPI document: 1.0
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


__version__ = "1.0.0"

# Define package exports
__all__ = [
    "ANNApi",
    "BatchJobApi",
    "ImagePredictionsApi",
    "ImagesApi",
    "InsightsApi",
    "LogosApi",
    "PredictApi",
    "PredictionsApi",
    "QuestionsApi",
    "ApiResponse",
    "ApiClient",
    "Configuration",
    "OpenApiException",
    "ApiTypeError",
    "ApiValueError",
    "ApiKeyError",
    "ApiAttributeError",
    "ApiException",
    "ImagePredictionsGet200Response",
    "ImagesLogosGet200Response",
    "ImagesLogosSearchGet200Response",
    "InsightSearchResult",
    "InsightsGet200Response",
    "InsightsRandomGet200Response",
    "LogoANNSearchResponse",
    "LogoANNSearchResponseResultsInner",
    "PredictCategoryPost200Response",
    "PredictCategoryPost200ResponseNeuralInner",
    "PredictCategoryPostRequest",
    "PredictCategoryPostRequestAnyOf",
    "PredictCategoryPostRequestAnyOf1",
    "PredictCategoryPostRequestAnyOf1Product",
    "PredictCategoryPostRequestAnyOf1ProductNutriments",
    "PredictLangGet200Response",
    "PredictLangGet200ResponsePredictionsInner",
    "PredictLangProductGet200Response",
    "PredictLangProductGet200ResponseCountsInner",
    "PredictLangProductGet200ResponsePercentInner",
    "PredictNutritionGet200Response",
    "PredictNutritionGet200ResponsePredictionsInner",
    "PredictNutritionGet200ResponsePredictionsInnerEntities",
    "Prediction",
    "PredictionsGet200Response",
    "QuestionsBarcodeGet200Response",
    "QuestionsGet200Response",
    "QuestionsUnansweredGet200Response",
    "QuestionsUnansweredGet200ResponseQuestionsInner",
    "ServerDomainParameter",
    "SuccessfulResponse",
]

# import apis into sdk package
from openapi_client.api.ann_api import ANNApi as ANNApi
from openapi_client.api.batch_job_api import BatchJobApi as BatchJobApi
from openapi_client.api.image_predictions_api import ImagePredictionsApi as ImagePredictionsApi
from openapi_client.api.images_api import ImagesApi as ImagesApi
from openapi_client.api.insights_api import InsightsApi as InsightsApi
from openapi_client.api.logos_api import LogosApi as LogosApi
from openapi_client.api.predict_api import PredictApi as PredictApi
from openapi_client.api.predictions_api import PredictionsApi as PredictionsApi
from openapi_client.api.questions_api import QuestionsApi as QuestionsApi

# import ApiClient
from openapi_client.api_response import ApiResponse as ApiResponse
from openapi_client.api_client import ApiClient as ApiClient
from openapi_client.configuration import Configuration as Configuration
from openapi_client.exceptions import OpenApiException as OpenApiException
from openapi_client.exceptions import ApiTypeError as ApiTypeError
from openapi_client.exceptions import ApiValueError as ApiValueError
from openapi_client.exceptions import ApiKeyError as ApiKeyError
from openapi_client.exceptions import ApiAttributeError as ApiAttributeError
from openapi_client.exceptions import ApiException as ApiException

# import models into sdk package
from openapi_client.models.image_predictions_get200_response import ImagePredictionsGet200Response as ImagePredictionsGet200Response
from openapi_client.models.images_logos_get200_response import ImagesLogosGet200Response as ImagesLogosGet200Response
from openapi_client.models.images_logos_search_get200_response import ImagesLogosSearchGet200Response as ImagesLogosSearchGet200Response
from openapi_client.models.insight_search_result import InsightSearchResult as InsightSearchResult
from openapi_client.models.insights_get200_response import InsightsGet200Response as InsightsGet200Response
from openapi_client.models.insights_random_get200_response import InsightsRandomGet200Response as InsightsRandomGet200Response
from openapi_client.models.logo_ann_search_response import LogoANNSearchResponse as LogoANNSearchResponse
from openapi_client.models.logo_ann_search_response_results_inner import LogoANNSearchResponseResultsInner as LogoANNSearchResponseResultsInner
from openapi_client.models.predict_category_post200_response import PredictCategoryPost200Response as PredictCategoryPost200Response
from openapi_client.models.predict_category_post200_response_neural_inner import PredictCategoryPost200ResponseNeuralInner as PredictCategoryPost200ResponseNeuralInner
from openapi_client.models.predict_category_post_request import PredictCategoryPostRequest as PredictCategoryPostRequest
from openapi_client.models.predict_category_post_request_any_of import PredictCategoryPostRequestAnyOf as PredictCategoryPostRequestAnyOf
from openapi_client.models.predict_category_post_request_any_of1 import PredictCategoryPostRequestAnyOf1 as PredictCategoryPostRequestAnyOf1
from openapi_client.models.predict_category_post_request_any_of1_product import PredictCategoryPostRequestAnyOf1Product as PredictCategoryPostRequestAnyOf1Product
from openapi_client.models.predict_category_post_request_any_of1_product_nutriments import PredictCategoryPostRequestAnyOf1ProductNutriments as PredictCategoryPostRequestAnyOf1ProductNutriments
from openapi_client.models.predict_lang_get200_response import PredictLangGet200Response as PredictLangGet200Response
from openapi_client.models.predict_lang_get200_response_predictions_inner import PredictLangGet200ResponsePredictionsInner as PredictLangGet200ResponsePredictionsInner
from openapi_client.models.predict_lang_product_get200_response import PredictLangProductGet200Response as PredictLangProductGet200Response
from openapi_client.models.predict_lang_product_get200_response_counts_inner import PredictLangProductGet200ResponseCountsInner as PredictLangProductGet200ResponseCountsInner
from openapi_client.models.predict_lang_product_get200_response_percent_inner import PredictLangProductGet200ResponsePercentInner as PredictLangProductGet200ResponsePercentInner
from openapi_client.models.predict_nutrition_get200_response import PredictNutritionGet200Response as PredictNutritionGet200Response
from openapi_client.models.predict_nutrition_get200_response_predictions_inner import PredictNutritionGet200ResponsePredictionsInner as PredictNutritionGet200ResponsePredictionsInner
from openapi_client.models.predict_nutrition_get200_response_predictions_inner_entities import PredictNutritionGet200ResponsePredictionsInnerEntities as PredictNutritionGet200ResponsePredictionsInnerEntities
from openapi_client.models.prediction import Prediction as Prediction
from openapi_client.models.predictions_get200_response import PredictionsGet200Response as PredictionsGet200Response
from openapi_client.models.questions_barcode_get200_response import QuestionsBarcodeGet200Response as QuestionsBarcodeGet200Response
from openapi_client.models.questions_get200_response import QuestionsGet200Response as QuestionsGet200Response
from openapi_client.models.questions_unanswered_get200_response import QuestionsUnansweredGet200Response as QuestionsUnansweredGet200Response
from openapi_client.models.questions_unanswered_get200_response_questions_inner import QuestionsUnansweredGet200ResponseQuestionsInner as QuestionsUnansweredGet200ResponseQuestionsInner
from openapi_client.models.server_domain_parameter import ServerDomainParameter as ServerDomainParameter
from openapi_client.models.successful_response import SuccessfulResponse as SuccessfulResponse
