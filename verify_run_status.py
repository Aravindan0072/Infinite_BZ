import requests
import sys

def check_url(url, name):
    try:
        response = requests.get(url, timeout=5)
        print(f"[{name}] Status: {response.status_code}")
        return True
    except Exception as e:
        print(f"[{name}] Failed: {e}")
        return False

if __name__ == "__main__":
    backend_ok = check_url("http://127.0.0.1:8000", "Backend") # Assuming root returns something or 404, but connection works
    frontend_ok = check_url("http://localhost:5174", "Frontend")
    
    if backend_ok and frontend_ok:
        print("SUCCESS: Both services appear running.")
    else:
        print("WARNING: Some services might be down.")
