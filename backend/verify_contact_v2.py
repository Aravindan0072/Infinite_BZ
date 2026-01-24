import requests

url = "http://localhost:8000/api/v1/contact"
data = {
    "first_name": "Test",
    "last_name": "User",
    "email": "test@example.com",
    "message": "Hello"
}

try:
    response = requests.post(url, json=data)
    print(f"Status: {response.status_code}")
    if response.status_code == 200:
        print("Response:", response.json())
    else:
        print("Error:", response.text)
except Exception as e:
    print("Exception:", e)
