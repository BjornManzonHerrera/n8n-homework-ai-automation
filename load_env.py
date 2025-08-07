import os
import json

def get_current_env_file():
    try:
        with open('current_key.json', 'r') as f:
            data = json.load(f)
            key_index = data.get('key_index', 0)
    except (FileNotFoundError, json.JSONDecodeError):
        key_index = 0

    if key_index == 0:
        return '.env'
    else:
        return f'.env.account{key_index}'

if __name__ == "__main__":
    env_file = get_current_env_file()
    if os.path.exists(env_file):
        with open(env_file, 'r') as f:
            for line in f:
                if line.strip() and not line.startswith('#'):
                    key, value = line.strip().split('=', 1)
                    print(f'set {key}={value}')
