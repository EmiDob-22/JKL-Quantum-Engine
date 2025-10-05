from typing import List, Any

def ensemble_inference(models: List[Any], input_data: dict) -> dict:
    """
    Quantum-inspired ensemble observer.
    Runs parallel inference, aggregates via voting/collapse.
    """
    results = []
    for model in models:
        try:
            results.append(model.predict(input_data))
        except Exception as e:
            results.append(None)
    # Collapse: majority voting, ignore None
    valid_results = [r for r in results if r is not None]
    if not valid_results:
        raise ValueError("All observers failed")
    output = max(set(valid_results), key=valid_results.count)
    return {"ensemble_result": output, "observers": len(models), "input": input_data}