import json, os, time
from app.core.policy import load_policy, enforce_policy
from app.core.risk import score_risk
from app.core.provisioner import provision
from app.core.audit import audit_append
from app.core.metrics import REQUESTS, LATENCY

def apply_intent(payload: dict):
    start = time.time()
    policy = load_policy()
    enforced = enforce_policy(payload, policy)
    risk = score_risk(enforced, policy)
    result = provision(enforced)
    out = {
        "intent": enforced,
        "risk": risk,
        "provisioning": result,
        "approval_required": risk["approval_required"]
    }
    audit_append(out)
    REQUESTS.inc()
    LATENCY.observe(time.time() - start)
    return out
