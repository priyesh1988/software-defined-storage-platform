import os, yaml

def load_policy():
    path = os.getenv("SDSP_POLICY_PATH", "/app/.sdsp/policy.yaml")
    with open(path, "r") as f:
        return yaml.safe_load(f)

def enforce_policy(intent: dict, policy: dict) -> dict:
    # enforce minimum replication based on criticality
    crit = intent.get("criticality", "MEDIUM")
    min_rep = policy["min_replication_by_criticality"].get(crit, 2)
    intent.setdefault("storage", {})
    intent["storage"]["replication"] = max(intent["storage"].get("replication", 2), min_rep)

    # enforce encryption flag
    intent.setdefault("extra", {})
    intent["extra"]["encryption_required"] = bool(policy.get("encryption_required", True))
    return intent
