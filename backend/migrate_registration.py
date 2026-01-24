
import asyncio
from sqlalchemy.future import select
from sqlalchemy import text
from app.core.database import engine, init_db
from app.models.schemas import SQLModel

async def add_missing_columns():
    async with engine.begin() as conn:
        print("Checking for missing columns in 'userregistration' table...")
        
        # Add confirmation_id
        try:
            await conn.execute(text("ALTER TABLE userregistration ADD COLUMN confirmation_id VARCHAR"))
            print("ADDED: confirmation_id")
        except Exception as e:
            print(f"SKIPPING: confirmation_id (likely exists) - {e}")
            
        # Add status
        try:
            await conn.execute(text("ALTER TABLE userregistration ADD COLUMN status VARCHAR DEFAULT 'PENDING'"))
            print("ADDED: status")
        except Exception as e:
            print(f"SKIPPING: status (likely exists) - {e}")

        # Add ticket_class_id
        try:
            await conn.execute(text("ALTER TABLE userregistration ADD COLUMN ticket_class_id INTEGER"))
            print("ADDED: ticket_class_id")
        except Exception as e:
            print(f"SKIPPING: ticket_class_id (likely exists) - {e}")

        # Add raw_data
        try:
            # Note: JSONB might need special handling on SQLite (TEXT), but Postgres supports it.
            # Using JSONB for Postgres
            await conn.execute(text("ALTER TABLE userregistration ADD COLUMN raw_data JSONB DEFAULT '{}'"))
            print("ADDED: raw_data")
        except Exception as e:
            # Fallback for SQLite or if exists
            try:
                await conn.execute(text("ALTER TABLE userregistration ADD COLUMN raw_data TEXT DEFAULT '{}'"))
                print("ADDED: raw_data (as TEXT for SQLite fallback)")
            except:
                print(f"SKIPPING: raw_data (likely exists) - {e}")

    print("Migration complete.")

if __name__ == "__main__":
    import sys
    # Fix for Windows loop policy
    if sys.platform == 'win32':
        asyncio.set_event_loop_policy(asyncio.WindowsProactorEventLoopPolicy())
        
    asyncio.run(add_missing_columns())
