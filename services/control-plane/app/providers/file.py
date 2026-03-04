def provision_file(intent: dict) -> dict:
    s = intent["storage"]
    return {
        "backend": "file",
        "protocol": s.get("protocol", "NFS"),
        "export": f"/exports/{intent['tenant']}/{intent['workload']}",
        "replication": s.get("replication", 2),
        "capacity_tb": s.get("capacity_tb"),
        "status": "provisioned (stub)"
    }
