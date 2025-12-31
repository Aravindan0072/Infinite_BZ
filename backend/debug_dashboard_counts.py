import asyncio
from sqlalchemy.future import select
from sqlalchemy import func
from app.core.database import init_db, get_session
from app.models.schemas import User, Event

async def check_counts():
    await init_db()
    async for session in get_session():
        # Check Users
        result_users = await session.execute(select(func.count(User.id)))
        total_users = result_users.scalar()
        
        # Check Events
        result_events = await session.execute(select(func.count(Event.id)))
        total_events = result_events.scalar()

        print(f"DEBUG: Total Users in DB: {total_users}")
        print(f"DEBUG: Total Events in DB: {total_events}")

        # List Users
        result_user_list = await session.execute(select(User))
        users = result_user_list.scalars().all()
        print("\n--- Users List ---")
        for u in users:
            print(f"ID: {u.id}, Email: {u.email}")
            
        break

if __name__ == "__main__":
    asyncio.run(check_counts())
