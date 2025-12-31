import requests
import json

EVENTBRITE_API_TOKEN = "T6WRADHDNPM5S4VYLFR5"
EVENT_ID = "1978745812993"

def debug_organizer():
    url = f"https://www.eventbriteapi.com/v3/events/{EVENT_ID}/"
    headers = {"Authorization": f"Bearer {EVENTBRITE_API_TOKEN}"}
    params = {"expand": "organizer"}
    
    response = requests.get(url, headers=headers, params=params)
    if response.status_code == 200:
        data = response.json()
        organizer = data.get("organizer", {})
        print("ORGANIZER RAW DATE:")
        print(json.dumps(organizer, indent=2))
    else:
        print(f"Error: {response.status_code}")

if __name__ == "__main__":
    debug_organizer()
