import requests

TOKEN = "T6WRADHDNPM5S4VYLFR5"
BASE_URL = "https://www.eventbriteapi.com/v3"

def test_search_api():
    url = f"{BASE_URL}/events/search/"
    headers = {"Authorization": f"Bearer {TOKEN}"}
    params = {
        "q": "business",
        "location.address": "chennai",
        "content_filter": "all" 
    }
    
    print(f"Testing Scrape-Free Search: {url}")
    try:
        resp = requests.get(url, headers=headers, params=params)
        print(f"Status: {resp.status_code}")
        if resp.status_code == 200:
            data = resp.json()
            events = data.get('events', [])
            print(f"Success! Found {len(events)} events via API.")
            if events:
                print(f"sample: {events[0].get('name', {}).get('text')}")
        else:
            print("Search API Failed.")
            print(resp.text)
            
    except Exception as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    test_search_api()
