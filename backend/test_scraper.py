import asyncio
import sys

# Force Proactor Loop for Playwright on Windows
if sys.platform == 'win32':
    asyncio.set_event_loop_policy(asyncio.WindowsProactorEventLoopPolicy())

from app.services.scraper import scrape_events_playwright

async def test():
    print("Testing scraper...")
    try:
        events = await scrape_events_playwright("chennai")
        print(f"Success! Found {len(events)} events.")
        for e in events:
            print(f"- {e['title']}")
    except Exception as e:
        print(f"FAILED: {e}")
        import traceback
        traceback.print_exc()

if __name__ == "__main__":
    asyncio.run(test())
