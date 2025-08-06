import os
import time
import json
from dotenv import load_dotenv
from google.cloud import monitoring_v3
from google.oauth2 import service_account

# Configuration for multiple projects
PROJECT_IDS = ["gemini-api-account-1", "civil-tube-468205-a0", "gemini-monitor-3"]  # Replace with your project IDs
ENV_FILES = [".env.account1", ".env.account2", ".env.account3"]
CREDENTIALS_PATHS = [
    "credentials_account1.json",
    "credentials_account2.json",
    "credentials_account3.json"
]
CURRENT_ACCOUNT_INDEX = 0
USAGE_THRESHOLD = 900  # Switch keys at 90% of 1,000 requests/day
MAIN_ENV_FILE = ".env"

def get_api_usage(credentials_path, project_index):
    """Query Google Cloud Monitoring API for Gemini CLI usage."""
    try:
        credentials = service_account.Credentials.from_service_account_file(credentials_path)
        client = monitoring_v3.MetricServiceClient(credentials=credentials)
        project_name = f"projects/{PROJECT_IDS[project_index]}"
        query = (
            f'metric.type="api.googleapis.com/requests" AND '
            f'resource.labels.api_key=~".*"'
        )
        interval = monitoring_v3.TimeInterval()
        now = time.time()
        interval.end_time.seconds = int(now)
        interval.start_time.seconds = int(now - 24 * 3600)  # Last 24 hours
        results = client.list_time_series(
            request={
                "name": project_name,
                "filter": query,
                "interval": interval,
                "view": monitoring_v3.ListTimeSeriesRequest.TimeSeriesView.FULL
            }
        )
        total_requests = 0
        for result in results:
            for point in result.points:
                total_requests += point.value.int64_value
        return total_requests
    except Exception as e:
        print(f"Error checking usage for {PROJECT_IDS[project_index]}: {e}")
        return 0  # Fallback to avoid blocking

def switch_api_key():
    """Switch to the next API key and update environment."""
    global CURRENT_ACCOUNT_INDEX
    CURRENT_ACCOUNT_INDEX = (CURRENT_ACCOUNT_INDEX + 1) % len(ENV_FILES)
    load_dotenv(ENV_FILES[CURRENT_ACCOUNT_INDEX])
    new_key = os.getenv("GEMINI_API_KEY")
    if not new_key:
        raise ValueError(f"No GEMINI_API_KEY found in {ENV_FILES[CURRENT_ACCOUNT_INDEX]}")
    os.environ["GOOGLE_API_KEY"] = new_key
    print(f"Switched to API key from {ENV_FILES[CURRENT_ACCOUNT_INDEX]} (Project: {PROJECT_IDS[CURRENT_ACCOUNT_INDEX]})")
    with open("current_key.json", "w") as f:
        json.dump({"current_env": ENV_FILES[CURRENT_ACCOUNT_INDEX], "project_id": PROJECT_IDS[CURRENT_ACCOUNT_INDEX]}, f)
    # Update main .env file
    with open(MAIN_ENV_FILE, "w") as f:
        f.write(f"GEMINI_API_KEY={new_key}\n")
        for key, value in os.environ.items():
            if key in ["CANVAS_API_KEY", "GOOGLE_OAUTH_CLIENT_ID", "GOOGLE_OAUTH_CLIENT_SECRET", 
                       "DISCORD_BOT_TOKEN", "HUGGINGFACE_API_KEY", "NGROK_AUTH_TOKEN"]:
                f.write(f"{key}={value}\n")

def check_and_rotate_keys():
    """Check usage and rotate keys if threshold is reached."""
    usage = get_api_usage(CREDENTIALS_PATHS[CURRENT_ACCOUNT_INDEX], CURRENT_ACCOUNT_INDEX)
    print(f"Current API usage for {PROJECT_IDS[CURRENT_ACCOUNT_INDEX]}: {usage} requests")
    if usage >= USAGE_THRESHOLD:
        print(f"Usage threshold ({USAGE_THRESHOLD}) reached. Rotating API key...")
        switch_api_key()
    else:
        print("Usage within limits. No rotation needed.")

def load_current_key():
    """Load the last used API key from persistent storage."""
    global CURRENT_ACCOUNT_INDEX
    try:
        with open("current_key.json", "r") as f:
            data = json.load(f)
            current_env = data["current_env"]
            CURRENT_ACCOUNT_INDEX = ENV_FILES.index(current_env)
            load_dotenv(current_env)
            os.environ["GOOGLE_API_KEY"] = os.getenv("GEMINI_API_KEY")
            print(f"Loaded API key from {current_env} (Project: {data['project_id']})")
    except (FileNotFoundError, ValueError):
        print("No previous key found. Using first account.")
        load_dotenv(ENV_FILES[0])
        os.environ["GOOGLE_API_KEY"] = os.getenv("GEMINI_API_KEY")
        with open("current_key.json", "w") as f:
            json.dump({"current_env": ENV_FILES[0], "project_id": PROJECT_IDS[0]}, f)

if __name__ == "__main__":
    # Load current key on startup
    load_current_key()
    # Check usage and rotate if needed
    check_and_rotate_keys()
    # Run periodically (every hour)
    while True:
        time.sleep(3600)  # Check every hour
        check_and_rotate_keys()
