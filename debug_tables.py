import os
from dotenv import load_dotenv
from sqlalchemy import create_engine, inspect, text

load_dotenv("backend/.env")

database_url = os.getenv("DATABASE_URL")
if database_url and "+asyncpg" in database_url:
    database_url = database_url.replace("+asyncpg", "")

engine = create_engine(database_url)
inspector = inspect(engine)
print(f"Tables in DB: {inspector.get_table_names()}")

with engine.connect() as conn:
    print("\n--- Checking for Chennai Events ---")
    result = conn.execute(text("SELECT id, title, city FROM event WHERE city ILIKE '%%Chennai%%' LIMIT 5"))
    events = result.fetchall()
    if not events:
        print("No events found for 'Chennai'.")
    else:
        for e in events:
            print(e)
