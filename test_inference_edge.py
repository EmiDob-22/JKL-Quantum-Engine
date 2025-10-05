import pytest
from src.services.inference import run_inference, load_model

def test_model_loading_failure(monkeypatch):
    def fake_loader(): raise FileNotFoundError("model not found")
    monkeypatch.setattr("src.services.inference.load_model", fake_loader)
    with pytest.raises(FileNotFoundError):
        load_model()

def test_inference_input_drift(monkeypatch):
    def fake_model(x): raise ValueError("input drift detected")
    monkeypatch.setattr("src.services.inference.run_inference", fake_model)
    with pytest.raises(ValueError):
        run_inference({"feature": "unexpected_value"})