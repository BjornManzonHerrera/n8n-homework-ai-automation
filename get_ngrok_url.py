import json
import requests
import time
import sys

<<<<<<< HEAD
<<<<<<< HEAD
def get_ngrok_url(retries=10, delay=2):
=======
def get_ngrok_url(retries=20, delay=2):
>>>>>>> 0b300f8 (Fix: ngrok and rotate_keys issues, improved startup script)
=======
def get_ngrok_url(retries=10, delay=2):
>>>>>>> fa54b4b (Update: ngrok and startup script modifications)
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
<<<<<<< HEAD
<<<<<<< HEAD
        sys.exit(1)
=======
        sys.exit(1)
>>>>>>> 0b300f8 (Fix: ngrok and rotate_keys issues, improved startup script)
=======
        sys.exit(1)
>>>>>>> fa54b4b (Update: ngrok and startup script modifications)
