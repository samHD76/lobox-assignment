import requests
import time
import statistics
import signal
import sys

# Variables to store response times
response_times = []

def signal_handler(sig, frame):
    print("\nStopping and calculating statistics...")
    if response_times:
        print(f"total number of Read requests send : {counter}")
        print(f"Min response time: {min(response_times):.4f} s")
        print(f"Max response time: {max(response_times):.4f} s")
        print(f"Mean response time: {statistics.mean(response_times):.4f} s")
    else:
        print("No requests were made.")
    sys.exit(0)

# Set up Ctrl+C handler
signal.signal(signal.SIGINT, signal_handler)

url = "http://localhost:8000/"

print("Sending requests to http://localhost:8000/ at 10 requests/second. Press Ctrl+C to stop.")
counter = 3
try:
    while True:
        start_time = time.time()
        try:
            counter += 1
            print(counter)
            response = requests.get(url)
            elapsed = time.time() - start_time
            response_times.append(elapsed)
        except requests.RequestException as e:
            print(f"Request failed: {e}")
        # Sleep to maintain 100 requests per second
        time.sleep(max(0, 0.01 - (time.time() - start_time)))
except KeyboardInterrupt:
    signal_handler(None, None)
