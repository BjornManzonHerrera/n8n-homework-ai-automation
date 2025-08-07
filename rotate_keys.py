import os
import json
import glob
from dotenv import dotenv_values

def rotate_keys():
    """
    Finds all .env.account* files, gathers all GEMINI_API_KEYs from them,
    and rotates to the next available key by updating the index in current_key.json.
    """
    # Find all files matching the .env.account* pattern
    env_files = glob.glob('.env.account*')
    
    if not env_files:
        print("No .env.account* files found.")
        # As a fallback, check for a single .env file
        if os.path.exists('.env'):
            env_files.append('.env')
        else:
            print("No .env file found either.")
            return

    all_keys = []
    print(f"Reading keys from: {', '.join(env_files)}")
    for file in env_files:
        # Load key-value pairs from the file without modifying the environment
        env_vars = dotenv_values(dotenv_path=file)
        # Find all keys in this file that start with GEMINI_API_KEY_
        keys_in_file = [v for k, v in env_vars.items() if k.startswith("GEMINI_API_KEY_")]
        all_keys.extend(keys_in_file)

    if not all_keys:
        print("No variables starting with 'GEMINI_API_KEY_' found in any of the .env files.")
        return

    # Get the current key index from the file
    try:
        with open('current_key.json', 'r') as f:
            data = json.load(f)
            current_key_index = data.get('key_index', 0)
    except (FileNotFoundError, json.JSONDecodeError):
        current_key_index = 0

    # Increment the index, and wrap around if we reach the end
    next_key_index = (current_key_index + 1) % len(all_keys)

    # Save the new index back to the file
    import os
import json
<<<<<<< HEAD
=======
import glob
>>>>>>> 7936c0f (fix: include git-ignored files in .env search)
from dotenv import dotenv_values

def rotate_keys():
    """
    Finds all .env.account* files, gathers all GEMINI_API_KEYs from them,
    and rotates to the next available key by updating the index in current_key.json.
    """
<<<<<<< HEAD
    env_files = []
    i = 1
    while True:
        # Manually check for .env.account files
        filename = f'.env.account{i}'
        if os.path.exists(filename):
            env_files.append(filename)
            i += 1
        else:
            break

    if not env_files:
        print("No .env.account* files found.")
=======
    # Find all files matching the .env.account* pattern, including git-ignored files
    env_files = glob.glob('.env.account*', include_gitignored=True)
    
    if not env_files:
        print("No .env.account* files found.")
        # As a fallback, check for a single .env file
>>>>>>> 7936c0f (fix: include git-ignored files in .env search)
        if os.path.exists('.env'):
            env_files.append('.env')
        else:
            print("No .env file found either.")
            return

    all_keys = []
    print(f"Reading keys from: {', '.join(env_files)}")
    for file in env_files:
<<<<<<< HEAD
        env_vars = dotenv_values(dotenv_path=file)
=======
        # Load key-value pairs from the file without modifying the environment
        env_vars = dotenv_values(dotenv_path=file)
        # Find all keys in this file that start with GEMINI_API_KEY
>>>>>>> 7936c0f (fix: include git-ignored files in .env search)
        keys_in_file = [v for k, v in env_vars.items() if k.startswith("GEMINI_API_KEY")]
        all_keys.extend(keys_in_file)

    if not all_keys:
        print("No variables starting with 'GEMINI_API_KEY' found in any of the .env files.")
        return

<<<<<<< HEAD
=======
    # Get the current key index from the file
>>>>>>> 7936c0f (fix: include git-ignored files in .env search)
    try:
        with open('current_key.json', 'r') as f:
            data = json.load(f)
            current_key_index = data.get('key_index', 0)
    except (FileNotFoundError, json.JSONDecodeError):
        current_key_index = 0

<<<<<<< HEAD
    next_key_index = (current_key_index + 1) % len(all_keys)

=======
    # Increment the index, and wrap around if we reach the end
    next_key_index = (current_key_index + 1) % len(all_keys)

    # Save the new index back to the file
>>>>>>> 7936c0f (fix: include git-ignored files in .env search)
    with open('current_key.json', 'w') as f:
        json.dump({'key_index': next_key_index}, f)
    
    print(f"Found a total of {len(all_keys)} keys.")
    print(f"Rotated to key index: {next_key_index}")

if __name__ == "__main__":
    rotate_keys()
    
    print(f"Found a total of {len(all_keys)} keys.")
    print(f"Rotated to key index: {next_key_index}")

if __name__ == "__main__":
    rotate_keys()