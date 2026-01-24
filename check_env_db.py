import asyncio
import os
from dotenv import load_dotenv
from sqlalchemy.ext.asyncio import create_async_engine
from sqlalchemy.sql import text

# Load environment variables from backend/.env
load_dotenv("backend/.env")

DATABASE_URL = os.getenv("DATABASE_URL")

async def check():
    if not DATABASE_URL:
        print("❌ DATABASE_URL not found in backend/.env")
        return
    
    # Ensure asyncpg is used
    url = DATABASE_URL
    if url.startswith("postgresql://"):
        url = url.replace("postgresql://", "postgresql+asyncpg://")
        
    print(f"Testing connection to: {url}")
    engine = create_async_engine(url)
    try:
        async with engine.connect() as conn:
            await conn.execute(text("SELECT 1"))
            print("✅ Database Connected Successfully!")
    except Exception as e:
        print(f"DATABASE CONNECTION ERROR: {e}")

if __name__ == "__main__":
    asyncio.run(check())
