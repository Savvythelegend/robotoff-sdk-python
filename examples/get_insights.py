from robotoff_sdk.api.insight import get_insights
from robotoff_sdk import Configuration, ApiClient

configuration = Configuration()
with ApiClient(configuration) as api_client:
    # Replace 'barcode' with a real product barcode if needed
    response = get_insights(barcode="1234567890123")
    for insight in response.body.get('insights', []):
        print(f"[💡] Insight: {insight}") 