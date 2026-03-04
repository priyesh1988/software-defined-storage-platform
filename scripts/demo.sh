#!/usr/bin/env bash
set -euo pipefail

echo "Starting SDSP..."
docker compose up -d --build
sleep 2
echo "Health:"
curl -s http://localhost:8000/health | jq . || curl -s http://localhost:8000/health
echo "Apply telemetry intent:"
curl -s -X POST http://localhost:8000/v1/intents/apply -H "Content-Type: application/json" -d @examples/intents/telemetry-hot-tier.json | head -c 800; echo
