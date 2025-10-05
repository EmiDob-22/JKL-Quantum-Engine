# Runbook: ML Deployment Failure

## Detection
- Alert: Inference API returns 500/model loading error.
- Prometheus: Model loading latency spike.

## Steps
1. Check deployment logs (kubectl logs inference-service).
2. Validate model artifact presence (ls /models/).
3. If missing, restore from MLflow registry (mlflow artifacts download).
4. Restart deployment (kubectl rollout restart).
5. Test with smoke-test (scripts/deployment/smoke-tests.sh).
6. Escalate if persistent (notify ML team, SRE).

## Prevention
- Monitor artifact registry sync.
- Automate artifact validation pre-deployment.