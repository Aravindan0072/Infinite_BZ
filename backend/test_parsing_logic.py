from bs4 import BeautifulSoup
from datetime import datetime

# HTML snippet based on what we found + user report
html_content = """
<div class="card">
    <h3>A 2-day Practical Bootcamp</h3>
    <a class="event-card-link" href="/e/123" data-event-paid-status="paid">Link</a>
    <p>Fri, Jan 23 • 7:30 PM GMT+5:30</p>
    <div class="price">From $321.96</div>
</div>
<div class="card">
    <h3>Free Event</h3>
    <a class="event-card-link" href="/e/456" data-event-paid-status="free">Link</a>
    <p>Thu, Feb 14 • 10:00 AM</p>
    <div class="price">Free</div>
</div>
"""

def test_parsing():
    soup = BeautifulSoup(html_content, "html.parser")
    cards = soup.select("div.card")
    
    print(f"Found {len(cards)} cards")
    
    for i, card in enumerate(cards):
        print(f"--- Card {i+1} ---")
        
        # 1. Title
        title = card.select_one("h3").get_text(strip=True)
        print(f"Title: {title}")
        
        # 2. Date Parsing Logic (Copied from scraper.py)
        date_tag = card.select_one("p")
        date_str = date_tag.get_text(strip=True)
        print(f"Raw Date: {date_str}")
        
        start_time = datetime.now()
        if date_str:
            try:
                clean_date_str = date_str.split("GMT")[0].strip()
                current_year = datetime.now().year
                parsed_date = datetime.strptime(f"{current_year} {clean_date_str}", "%Y %a, %b %d • %I:%M %p")
                
                # If date is in past (e.g. Jan 1 when today is Dec 28), it's probably next year
                if parsed_date < datetime.now():
                    parsed_date = parsed_date.replace(year=current_year + 1)
                
                start_time = parsed_date
                print(f"Parsed Start Time: {start_time}")
            except Exception as e:
                print(f"Date parsing failed: {e}")

        # 3. Free Logic (Copied from scraper.py)
        link_tag = card.select_one("a")
        is_free = False
        paid_status = link_tag.get("data-event-paid-status")
        if paid_status and paid_status.lower() == "free":
            is_free = True
        else:
            if "free" in card.get_text().lower() and "from" not in card.get_text().lower():
                is_free = True
        
        print(f"Is Free: {is_free}")

if __name__ == "__main__":
    test_parsing()
