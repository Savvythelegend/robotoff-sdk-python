# coding: utf-8

"""
    API Reference

    Robotoff provides a simple API allowing consumers to fetch predictions and annotate them.  All endpoints must be prefixed with `/api/v1`. The full URL is `https://robotoff.openfoodfacts.org/api/v1/{endpoint}`. 

    The version of the OpenAPI document: 1.0
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from openapi_client.api.predict_api import PredictApi


class TestPredictApi(unittest.TestCase):
    """PredictApi unit test stubs"""

    def setUp(self) -> None:
        self.api = PredictApi()

    def tearDown(self) -> None:
        pass

    def test_predict_category_post(self) -> None:
        """Test case for predict_category_post

        Predict categories for a product
        """
        pass

    def test_predict_lang_get(self) -> None:
        """Test case for predict_lang_get

        Predict the language of a text
        """
        pass

    def test_predict_lang_product_get(self) -> None:
        """Test case for predict_lang_product_get

        Predict the languages of the product
        """
        pass

    def test_predict_nutrition_get(self) -> None:
        """Test case for predict_nutrition_get

        Extract nutritional information from an image
        """
        pass

    def test_predict_ocr_prediction_get(self) -> None:
        """Test case for predict_ocr_prediction_get

        Generate OCR predictions an OCR JSON
        """
        pass


if __name__ == '__main__':
    unittest.main()
