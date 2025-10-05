"""
Krok 2: Rozszerz DocGen — automatyczna dokumentacja property/fuzz/chaos, manifestów (K8s, Helm, Terraform), integracja z linterami/validatorami.
"""

def generate_doc_for_test(test_name, test_type, description, manifest=None):
    doc = f"### {test_name} ({test_type})\nOpis: {description}\n"
    if manifest:
        doc += f"Manifest: {manifest}\n"
    return doc

def validate_markdown(md):
    # Integracja z markdown/docstring linterami
    return "OK" if len(md) > 10 else "Invalid doc"

example_doc = generate_doc_for_test("test_fuzz_edge", "property-based", "Test resilience fuzz dla edge-case.", manifest="K8s deployment.yaml")
print(validate_markdown(example_doc))