import os
from dotenv import load_dotenv
from sqlalchemy import create_engine, inspect

# Load env from backend/.env because that's where the real DB url is
load_dotenv("backend/.env")

# Connect to your Real Database
database_url = os.getenv("DATABASE_URL")
if not database_url:
    print("Error: DATABASE_URL not found in backend/.env")
    exit(1)

engine = create_engine(database_url.replace("+asyncpg", ""))

inspector = inspect(engine)
# Check specifically for 'event' table as used in previous fixes
table_name = 'event'
if table_name not in inspector.get_table_names():
    print(f"Table '{table_name}' not found! Tables are: {inspector.get_table_names()}")
    # Fallback to 'events' if event is missing, just in case
    if 'events' in inspector.get_table_names():
        table_name = 'events'

print(f"\n📊 Columns in '{table_name}' table:")
columns = inspector.get_columns(table_name)
for col in columns:
    print(f"- {col['name']} ({col['type']})")
