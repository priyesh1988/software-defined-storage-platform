import os, time, random, httpx

CONTROL = os.getenv("SDSP_CONTROL_PLANE", "http://localhost:8000")

def sample():
    return {
        "tenant": "mission-control",
        "workload": "telemetry",
        "criticality": "MISSION_CRITICAL",
        "storage": {
            "type": "block",
            "performance_tier": "hot",
            "capacity_tb": 200,
            "replication": 3,
            "protocol": "NVMe-oF"
        },
        "dependencies": ["telemetry-bus", "flight-analytics"],
        "extra": {"telemetry_rate_mbps": random.randint(500, 2500)}
    }

while True:
    intent = sample()
    try:
        r = httpx.post(f"{CONTROL}/v1/intents/apply", json=intent, timeout=5.0)
        print("intent applied:", r.status_code, r.json().get("risk", {}).get("risk_score"))
    except Exception as e:
        print("control plane not ready:", e)
    time.sleep(5)
