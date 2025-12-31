from fastapi import APIRouter, Depends, HTTPException, BackgroundTasks
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.future import select
from typing import List

from app.core.database import get_session
from app.models.schemas import Event, UserRegistration
from app.services.scraper import scrape_events_playwright # Async import

router = APIRouter()

# --- 1. SYNC (Admin Only / Debug) ---
@router.post("/sync")
async def sync_events(city: str = "chennai", session: AsyncSession = Depends(get_session)):
    """
    Triggers the Playwright Scraper
    """
    print(f"Starting Sync for {city}...")
    try:
        print("Calling scraper function...")
        events_data = await scrape_events_playwright(city)
        print("Scraper returned.")
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
    
    saved_count = 0
    for data in events_data:
        # Check duplicates via eventbrite_id
        stmt = select(Event).where(Event.eventbrite_id == data["eventbrite_id"])
        result = await session.execute(stmt)
        existing = result.scalars().first()
        
        if not existing:
            new_event = Event(**data)
            session.add(new_event)
            saved_count += 1
            
    await session.commit()
    return {"status": "success", "added": saved_count, "total_found": len(events_data)}

# --- 2. PUBLIC EVENTS API ---
@router.get("/events", response_model=List[Event])
async def list_events(
    city: str = None, 
    category: str = None, 
    session: AsyncSession = Depends(get_session)
):
    """
    Returns events with optional filtering.
    """
    query = select(Event).order_by(Event.start_time)
    
    if city:
        query = query.where(Event.venue_name.ilike(f"%{city}%"))
    # Category filter would require a column or parsing raw_data
        
    result = await session.execute(query)
    events = result.scalars().all()
    return events

# --- 3. TRACKING ---
@router.post("/track-click")
async def track_click(registration: UserRegistration, session: AsyncSession = Depends(get_session)):
    """
    Logs a user clicking 'Register'. 
    NOTE: This is just counting intent, not actual API registration.
    """
    # Force server-side timestamp to ensure valid datetime object
    from datetime import datetime
    registration.registered_at = datetime.now()
    
    session.add(registration)
    await session.commit()
    await session.refresh(registration)
    return {"status": "tracked", "id": registration.id}
