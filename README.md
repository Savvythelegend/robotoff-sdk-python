# Robotoff Python SDK

[![OpenAPI Docs](https://img.shields.io/badge/docs-openapi-blue)](https://openfoodfacts.github.io/robotoff/references/api/)

This repository provides an auto-generated Python SDK for [Robotoff](https://github.com/openfoodfacts/robotoff), based on its [OpenAPI specification](https://openfoodfacts.github.io/robotoff/references/api/).

The SDK enables developers to interact with Robotoff's machine learning-powered product question/answer engine and related APIs with minimal setup.

---

## Installation

To install the SDK locally:

```bash
pip install .
````

---

## Example Usage

### 1. Get Popular Questions

```python
from robotoff_sdk.api.questions import get_popular_questions
from robotoff_sdk import Configuration, ApiClient

configuration = Configuration()
with ApiClient(configuration) as api_client:
    response = get_popular_questions()
    print(response.body)
```

---

### 2. Fetch Annotations for a Product

```python
from robotoff_sdk.api.annotations import get_annotations
from robotoff_sdk import Configuration, ApiClient

configuration = Configuration()
with ApiClient(configuration) as api_client:
    response = get_annotations(barcode="1234567890123")
    for annotation in response.body.get('annotations', []):
        print("Annotation:", annotation)
```

---

### 3. Get Insights for a Product

```python
from robotoff_sdk.api.insight import get_insights
from robotoff_sdk import Configuration, ApiClient

configuration = Configuration()
with ApiClient(configuration) as api_client:
    response = get_insights(barcode="1234567890123")
    for insight in response.body.get('insights', []):
        print("Insight:", insight)
```

> For more usage patterns, refer to the `examples/` directory.

---

## Available APIs

This SDK exposes all public Robotoff APIs via:

* `robotoff_sdk.api.questions`
* `robotoff_sdk.api.annotations`
* `robotoff_sdk.api.insight`
* `robotoff_sdk.api.predictions`

Each endpoint is mapped to a simple Python function, ready to use.

---

## Project Structure

```bash
robotoff-sdk-python/
├── examples/
├── robotoff_sdk/
├── openapi.json
├── openapitools.json
├── pyproject.toml
├── README.md
└── LICENSE
```

---

## Development & Contribution

This is an initial prototype generated using [OpenAPI Generator](https://openapi-generator.tech/).
Future improvements may include tests, CI/CD, type stubs, and integration into the main Open Food Facts SDK ecosystem.

If you'd like to contribute:

* Fork the repository
* Use `openapi-generator` to regenerate as needed
* Submit a PR with clear changes

---

## License

This SDK is distributed under the terms of the [GNU Affero General Public License v3.0](LICENSE), in alignment with the Robotoff project.

If using or distributing this code, please ensure compliance with AGPL-3.0 terms, especially when used over a network.

---

## Acknowledgements

This SDK is based on the public OpenAPI specification provided by [Robotoff](https://github.com/openfoodfacts/robotoff), part of the [Open Food Facts](https://openfoodfacts.org) project.

Generated using [OpenAPI Generator](https://openapi-generator.tech/).
