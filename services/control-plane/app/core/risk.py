import networkx as nx

def _change_magnitude(intent: dict) -> float:
    s = intent.get("storage", {})
    cap = int(s.get("capacity_tb", 0))
    tier = s.get("performance_tier", "warm")
    proto = s.get("protocol", "")
    score = min(40.0, cap / 20.0)  # 800TB -> 40
    if tier == "hot":
        score += 10
    if proto.upper() in {"NVME-OF", "NVME_O_F", "NVME"}:
        score += 10
    return min(score, 60.0)

def _blast_radius(intent: dict) -> float:
    # simple dependency fan-out model; swap with Neo4j later
    deps = intent.get("dependencies", []) or []
    G = nx.DiGraph()
    root = "change"
    for d in deps:
        G.add_edge(root, d)
    # assume each dep fans out to 2 downstream services (stub)
    for d in deps:
        G.add_edge(d, f"{d}-downstream-1")
        G.add_edge(d, f"{d}-downstream-2")
    return min(30.0, float(len(nx.descendants(G, root))))

def score_risk(intent: dict, policy: dict) -> dict:
    weights = policy.get("risk_weights", {})
    cm = _change_magnitude(intent) * float(weights.get("change_magnitude", 1.0))
    br = _blast_radius(intent) * float(weights.get("dependency_blast_radius", 1.2))
    base = cm + br

    crit = intent.get("criticality", "MEDIUM")
    mult = float(weights.get("criticality_multiplier", {}).get(crit, 1.0))
    score = min(100, int(base * mult))

    level = "LOW" if score < 30 else "MEDIUM" if score < 60 else "HIGH"
    if crit == "MISSION_CRITICAL":
        level = "HIGH"

    approval = policy.get("approval_tiers", {}).get(crit, "TEAM_LEAD")
    return {
        "risk_score": score,
        "risk_level": level,
        "blast_radius": int(br),
        "approval_required": approval,
        "explain": {
            "change_magnitude": cm,
            "blast_radius": br,
            "criticality_multiplier": mult
        }
    }
