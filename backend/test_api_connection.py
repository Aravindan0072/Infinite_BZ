import requests
import json

# User provided
EVENT_ID = "1545967904619"  # NOTE: This ID might be old/invalid, we might need a fresh one from our recent scrape if this 404s
# But let's try user's ID first.
TOKEN = "T6WRADHDNPM5S4VYLFR5"

def test_api():
    headers = {"Authorization": f"Bearer {TOKEN}"}
    
    # 1. Test Single Event Details
    print(f"--- Testing Event Details for ID {EVENT_ID} ---")
    url = f"https://www.eventbriteapi.com/v3/events/{EVENT_ID}/"
    params = {
        "expand": "venue,ticket_classes" # expanded ticket_classes to check pricing
    }
    
    try:
        response = requests.get(url, headers=headers, params=params)
        print(f"Status Code: {response.status_code}")
        if response.status_code == 200:
            data = response.json()
            print("Success!")
            print(f"Title: {data.get('name', {}).get('text')}")
            print(f"Start: {data.get('start', {}).get('local')}")
            print(f"End: {data.get('end', {}).get('local')}")
            
            # Check tickets for 'free' status
            tickets = data.get('ticket_classes', [])
            is_free = False
            min_price = "N/A"
            if tickets:
                print(f"Found {len(tickets)} ticket classes.")
                for t in tickets:
                    print(f" - {t.get('name')}: {t.get('cost', {}).get('display')} (Free: {t.get('free')})")
                    if t.get('free'):
                        is_free = True
            print(f"Is Free Event: {is_free}")
            
        else:
            print(f"Error: {response.text}")
    except Exception as e:
        print(f"Exception: {e}")

    # 2. Test Search (Organization events or Public Search)
    # Note: Public search via API is deprecated/restricted for some tokens, but let's check organizations API or generic
    print("\n--- Testing Organization List (To see permissions) ---")
    try:
        org_url = "https://www.eventbriteapi.com/v3/users/me/organizations/"
        resp = requests.get(org_url, headers=headers)
        print(f"Org Status: {resp.status_code}")
        if resp.status_code == 200:
            print("Org Access: OK")
            print(resp.json())
        else:
             print("Org Access: Denied/Failed")
    except Exception as e:
        print(f"Exception: {e}")

if __name__ == "__main__":
    test_api()
