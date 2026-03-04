import yaml, time, os

POLICY = os.getenv("SDSP_POLICY_PATH", "/app/policy/tiering.yaml")

def load():
    with open(POLICY, "r") as f:
        return yaml.safe_load(f)

def decide(workload: str, age_days: int, p: dict):
    rules = (p.get("rules", {}) or {}).get(workload, {"archive_after_days": 30})
    if age_days < 7:
        return "hot"
    if age_days < rules["archive_after_days"]:
        return "warm"
    return "cold"

if __name__ == "__main__":
    p = load()
    for w in ["telemetry","manufacturing","simulation"]:
        for age in [1, 10, 40, 120]:
            print(w, age, "->", decide(w, age, p))
    # service stub
    while True:
        time.sleep(60)
