import json
import requests
import time
import sys

def get_ngrok_url(retries=10, delay=2):
    for i in range(retries):
        try:
            response = requests.get("http://127.0.0.1:4040/api/tunnels")
            if response.status_code == 200:
                tunnels = response.json()["tunnels"]
                for tunnel in tunnels:
                    if tunnel["proto"] == "https":
                        return tunnel["public_url"]
                if tunnels:
                    return tunnels[0]["public_url"]
        except requests.ConnectionError:
            if i < retries - 1:
                time.sleep(delay)
            else:
                raise
    return None

if __name__ == "__main__":
    url = get_ngrok_url()
    if url:
        print(url)
        sys.exit(0)
    else:
        sys.exit(1)
