def provision_block(intent: dict) -> dict:
    s = intent["storage"]
    return {
        "backend": "block",
        "protocol": s.get("protocol", "iSCSI"),
        "pool": f"{intent['tenant']}-{intent['workload']}-blk",
        "replication": s.get("replication", 2),
        "capacity_tb": s.get("capacity_tb"),
        "status": "provisioned (stub)"
    }
