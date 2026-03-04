from prometheus_client import Counter, Histogram

REQUESTS = Counter("sdsp_requests_total", "Total SDSP intent apply requests")
LATENCY = Histogram("sdsp_request_latency_seconds", "Latency of intent processing")
