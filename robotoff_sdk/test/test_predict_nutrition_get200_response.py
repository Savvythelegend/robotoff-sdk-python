# coding: utf-8

"""
    API Reference

    Robotoff provides a simple API allowing consumers to fetch predictions and annotate them.  All endpoints must be prefixed with `/api/v1`. The full URL is `https://robotoff.openfoodfacts.org/api/v1/{endpoint}`. 

    The version of the OpenAPI document: 1.0
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from openapi_client.models.predict_nutrition_get200_response import PredictNutritionGet200Response

class TestPredictNutritionGet200Response(unittest.TestCase):
    """PredictNutritionGet200Response unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> PredictNutritionGet200Response:
        """Test PredictNutritionGet200Response
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `PredictNutritionGet200Response`
        """
        model = PredictNutritionGet200Response()
        if include_optional:
            return PredictNutritionGet200Response(
                predictions = [
                    openapi_client.models._predict_nutrition_get_200_response_predictions_inner._predict_nutrition_get_200_response_predictions_inner(
                        nutrients = openapi_client.models.nutrients.nutrients(), 
                        entities = openapi_client.models._predict_nutrition_get_200_response_predictions_inner_entities._predict_nutrition_get_200_response_predictions_inner_entities(
                            aggregated = [
                                None
                                ], 
                            postprocessed = [
                                None
                                ], 
                            raw = [
                                None
                                ], ), )
                    ]
            )
        else:
            return PredictNutritionGet200Response(
        )
        """

    def testPredictNutritionGet200Response(self):
        """Test PredictNutritionGet200Response"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
