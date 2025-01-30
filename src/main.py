from prometheus_client import start_http_server, Counter

REQUESTS_COUNT = Counter('requests_total', 'Total number of requests')

def main():
    start_http_server(8000)  # Expose metrics on port 8000
    while True:
        # Simulate processing
        REQUESTS_COUNT.inc()
