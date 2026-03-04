import os, json, hashlib
from datetime import datetime

AUDIT_PATH = os.getenv("SDSP_AUDIT_PATH", "/app/audit/audit.jsonl")
_prev_hash = None

def audit_append(record: dict) -> str:
    global _prev_hash
    envelope = {
        "ts": datetime.utcnow().isoformat() + "Z",
        "prev_hash": _prev_hash,
        "record": record
    }
    raw = json.dumps(envelope, sort_keys=True).encode("utf-8")
    h = hashlib.sha256(raw).hexdigest()
    envelope["hash"] = h

    with open(AUDIT_PATH, "a", encoding="utf-8") as f:
        f.write(json.dumps(envelope) + "\n")
    _prev_hash = h
    return h
