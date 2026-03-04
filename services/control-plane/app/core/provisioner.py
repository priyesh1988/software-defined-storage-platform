from app.providers.block import provision_block
from app.providers.file import provision_file
from app.providers.object import provision_object

def provision(intent: dict) -> dict:
    stype = (intent.get("storage", {}) or {}).get("type", "file")
    if stype == "block":
        return provision_block(intent)
    if stype == "object":
        return provision_object(intent)
    return provision_file(intent)
