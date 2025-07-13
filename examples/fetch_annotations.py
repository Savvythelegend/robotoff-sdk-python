# examples/annotations.py
import argparse
from robotoff_sdk.openapi_client.api import ann_api
from robotoff_sdk import Configuration, ApiClient

parser = argparse.ArgumentParser()
parser.add_argument("--barcode", type=str, required=True)
args = parser.parse_args()

config = Configuration()
with ApiClient(config) as api_client:
    res = get_annotations(barcode=args.barcode)
    print(res.body)
