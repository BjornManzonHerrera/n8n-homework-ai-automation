import os
import json
import glob
from dotenv import dotenv_values

def rotate_keys():
    """
    Finds all .env.account* files, gathers all GEMINI_API_KEYs from them,
    and rotates to the next available key by updating the index in current_key.json.
    """
    env_files = glob.glob('.env.account*')
    
    if not env_files:
        print("No .env.account* files found.")
        if os.path.exists('.env'):
            env_files.append('.env')
        else:
            print("No .env file found either.")
            return

    all_keys = []
    print(f"Reading keys from: {', '.join(env_files)}")
    for file in env_files:
        env_vars = dotenv_values(dotenv_path=file)
        keys_in_file = [v for k, v in env_vars.items() if k.startswith("GEMINI_API_KEY")]
        all_keys.extend(keys_in_file)

    if not all_keys:
        print("No variables starting with 'GEMINI_API_KEY' found in any of the .env files.")
        return

    try:
        with open('current_key.json', 'r') as f:
            data = json.load(f)
            current_key_index = data.get('key_index', 0)
    except (FileNotFoundError, json.JSONDecodeError):
        current_key_index = 0

    next_key_index = (current_key_index + 1) % len(all_keys)

    with open('current_key.json', 'w') as f:
        json.dump({'key_index': next_key_index}, f)
    
    print(f"Found a total of {len(all_keys)} keys.")
    print(f"Rotated to key index: {next_key_index}")

if __name__ == "__main__":
    rotate_keys()