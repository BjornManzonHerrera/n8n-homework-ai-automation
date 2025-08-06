#!/usr/bin/env python3
"""Simple test script for the /generate endpoint"""
import requests
import json

def test_generate_endpoint():
    """Test the /generate endpoint with a sample assignment"""
    
    # Test data
    test_assignment = {
        "name": "Climate Change Essay",
        "description": "Write a 500-word essay about the impact of climate change on global ecosystems"
    }
    
    try:
        # Make request to local server
        response = requests.post("http://localhost:7860/generate", json=test_assignment)
        
        if response.status_code == 200:
            result = response.json()
            print("✅ Success! Response:")
            print(f"Header: {result.get('header', 'Missing')}")
            print(f"Body length: {len(result.get('body', ''))} characters")
            print(f"Body preview: {result.get('body', '')[:200]}...")
            return True
        else:
            print(f"❌ Error {response.status_code}: {response.text}")
            return False
            
    except requests.exceptions.ConnectionError:
        print("❌ Connection error - make sure the server is running on localhost:7860")
        return False
    except Exception as e:
        print(f"❌ Error: {e}")
        return False

if __name__ == "__main__":
    test_generate_endpoint()