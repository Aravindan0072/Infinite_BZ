import asyncio
import sys

# Force Proactor Loop for Playwright on Windows
if sys.platform == 'win32':
    asyncio.set_event_loop_policy(asyncio.WindowsProactorEventLoopPolicy())

from sqlalchemy.future import select
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.asyncio import AsyncSession
from app.core.database import engine, init_db
from app.models.schemas import Event
from app.services.scraper import scrape_events_playwright

async def run_manual_ingestion():
    print("--- Starting Manual Ingestion ---")
    
    # 1. Initialize DB (ensure tables exist)
    await init_db()
    
    # 2. Run Scraper
    print("Running Hybrid Scraper...")
    events_data = await scrape_events_playwright("chennai")
    print(f"Scraper found {len(events_data)} events.")
    
    # 3. Save to DB
    print("Saving to Database...")
    async_session = sessionmaker(engine, class_=AsyncSession, expire_on_commit=False)
    
    async with async_session() as session:
        added_count = 0
        updated_count = 0
        
        for data in events_data:
            # Check duplicates
            statement = select(Event).where(Event.eventbrite_id == data["eventbrite_id"])
            result = await session.execute(statement)
            existing_event = result.scalars().first()
            
            if not existing_event:
                event = Event(**data)
                session.add(event)
                added_count += 1
            else:
                # OPTIONAL: Update existing events with new data (like corrected times)
                # Since the user wants to FIX existing data, we SHOULD update.
                existing_event.start_time = data['start_time']
                existing_event.end_time = data['end_time']
                existing_event.is_free = data['is_free']
                existing_event.title = data['title']
                existing_event.description = data['description']
                updated_count += 1
        
        await session.commit()
        print(f"DONE: Added {added_count} new events. Updated {updated_count} existing events.")

if __name__ == "__main__":
    asyncio.run(run_manual_ingestion())
