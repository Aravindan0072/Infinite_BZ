import requests
import json

EVENTBRITE_API_TOKEN = "T6WRADHDNPM5S4VYLFR5"
EVENT_ID = "1978745812993"

def fetch_raw_data():
    url = f"https://www.eventbriteapi.com/v3/events/{EVENT_ID}/"
    headers = {"Authorization": f"Bearer {EVENTBRITE_API_TOKEN}"}
    params = {"expand": "venue,ticket_classes,organizer"}
    
    response = requests.get(url, headers=headers, params=params)
    if response.status_code == 200:
        data = response.json()
        print(json.dumps(data, indent=2))
        
        print("-" * 50)
        print(f"Name: {data.get('name', {}).get('text')}")
        print(f"Online Event Flag: {data.get('online_event')}")
        venue = data.get('venue', {})
        print(f"Venue Name: {venue.get('name')}")
        print(f"Address: {venue.get('address')}")
    else:
        print(f"Error: {response.status_code} - {response.text}")

if __name__ == "__main__":
    fetch_raw_data()
