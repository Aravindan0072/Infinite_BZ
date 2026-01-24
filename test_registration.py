import requests
import json

def test_registration():
    url = "http://localhost:8000/api/v1/auth/register"
    payload = {
        "email": "test@example.com",
        "password": "password123",
        "full_name": "Test User",
        "is_active": False
    }
    
    print(f"Sending request to {url} with payload: {json.dumps(payload, indent=2)}")
    response = requests.post(url, json=payload)
    
    print(f"Status Code: {response.status_code}")
    try:
        print(f"Response Body: {json.dumps(response.json(), indent=2)}")
    except:
        print(f"Response Body: {response.text}")

if __name__ == "__main__":
    test_registration()
