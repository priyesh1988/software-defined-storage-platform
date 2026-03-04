def provision_object(intent: dict) -> dict:
    s = intent["storage"]
    return {
        "backend": "object",
        "protocol": s.get("protocol", "S3"),
        "bucket": f"{intent['tenant']}-{intent['workload']}".replace("_","-"),
        "replication": s.get("replication", 2),
        "capacity_tb": s.get("capacity_tb"),
        "status": "provisioned (stub)"
    }
