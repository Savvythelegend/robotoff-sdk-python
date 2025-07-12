# Robotoff Python SDK

Auto-generated Python SDK for [Robotoff](https://github.com/openfoodfacts/robotoff) using its [OpenAPI specification](https://openfoodfacts.github.io/robotoff/references/api/).

This SDK lets developers easily interact with Robotoff's machine learning-powered product question/answer engine.

## 📦 Installation

```bash
pip install .
```

## 🚀 Quick Examples

### Get Popular Questions
```python
from robotoff_sdk.api.questions import get_popular_questions
from robotoff_sdk import Configuration, ApiClient

configuration = Configuration()
with ApiClient(configuration) as api_client:
    response = get_popular_questions()
    print(response.body)
```

### Fetch Annotations for a Product
```python
from robotoff_sdk.api.annotations import get_annotations
from robotoff_sdk import Configuration, ApiClient

configuration = Configuration()
with ApiClient(configuration) as api_client:
    response = get_annotations(barcode="1234567890123")
    for annotation in response.body.get('annotations', []):
        print(f"[📝] Annotation: {annotation}")
```

### Get Insights for a Product
```python
from robotoff_sdk.api.insight import get_insights
from robotoff_sdk import Configuration, ApiClient

configuration = Configuration()
with ApiClient(configuration) as api_client:
    response = get_insights(barcode="1234567890123")
    for insight in response.body.get('insights', []):
        print(f"[💡] Insight: {insight}")
```

See the `examples/` directory for more usage patterns.

## 🧪 Available APIs

* Questions API
* Annotations API
* Insight API
* Predictions API

More available under `robotoff_sdk.api.*`

## 🔗 License

This SDK is licensed under the [AGPL-3.0 License](LICENSE) in alignment with Robotoff. 