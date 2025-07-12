from robotoff_sdk.api.annotations import get_annotations
from robotoff_sdk import Configuration, ApiClient

configuration = Configuration()
with ApiClient(configuration) as api_client:
    # Replace 'barcode' with a real product barcode if needed
    response = get_annotations(barcode="1234567890123")
    for annotation in response.body.get('annotations', []):
        print(f"[📝] Annotation: {annotation}") 