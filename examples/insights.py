# examples/insights.py
import argparse
from robotoff_sdk.openapi_client.configuration import Configuration
from robotoff_sdk.openapi_client.api_client import ApiClient
from robotoff_sdk.openapi_client.api.insights_api import InsightsApi

def get_insights(barcode):
    configuration = Configuration()
    with ApiClient(configuration) as api_client:
        api = InsightsApi(api_client)
        try:
            response = api.insights_get(barcode=int(barcode))
            print("\n[INSIGHTS]\n")
            for insight in response.insights or []:
                print(f"- {insight.type or 'unknown'}: {insight.value} (ID: {insight.id})")
        except Exception as e:
            print(f"[ERROR] {e}")

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--barcode", required=True, type=int)
    args = parser.parse_args()
    get_insights(args.barcode)