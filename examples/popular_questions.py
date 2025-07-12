from robotoff_sdk.api.questions import get_popular_questions
from robotoff_sdk import Configuration, ApiClient

# Optional: configure base URL if needed
configuration = Configuration()
# configuration.host = 'https://robotoff.openfoodfacts.org/api/v1'

with ApiClient(configuration) as api_client:
    # Fetch the most popular product-related questions
    response = get_popular_questions()
    for q in response.body.get('questions', []):
        print(f"[🔍] Question: {q['question']}") 