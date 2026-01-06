import asyncio
from sqlalchemy import select
from app.core.database import get_session
from app.models.schemas import Event

async def check_data():
    async for session in get_session():
        # Get all events
        stmt = select(Event).limit(20)
        result = await session.execute(stmt)
        events = result.scalars().all()
        
        print("\n--- CHECKING EVENT DATA ---")
        for event in events:
            print(f"ID: {event.id}")
            print(f"  Title: {event.title}")
            print(f"  Desc Snippet: {event.description[:50] if event.description else 'None'}...")
            print(f"  URL: {event.url}")
            print(f"  Is Free: {event.is_free}")
            print(f"  Online: {event.online_event}")
            print("-" * 30)

        # Test Filter Logic Simulation
        print("\n--- TEST FILTER MATCHING ---")
        categories = {
            "startup": ["startup", "founder", "entrepreneur", "venture", "pitch"],
            "tech": ["tech", "software", "developer", "ai", "data", "code"],
            "business": ["business", "marketing", "sales", "finance", "network"]
        }
        
        for category, keywords in categories.items():
            print(f"Checking Category: {category.upper()}")
            matches = 0
            for event in events:
                text = (event.title + " " + (event.description or "")).lower()
                if any(kw in text for kw in keywords):
                    print(f"  [MATCH] {event.title}")
                    matches += 1
            if matches == 0:
                print("  No matches found in sample.")

if __name__ == "__main__":
    import asyncio
    asyncio.run(check_data())
