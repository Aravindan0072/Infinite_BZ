from sqlalchemy import create_engine, text
from sqlalchemy.orm import sessionmaker

DATABASE_URL = "postgresql://postgres:password@localhost/events_hub"

def check_db():
    engine = create_engine(DATABASE_URL)
    with engine.connect() as conn:
        result = conn.execute(text("SELECT count(*) FROM user"))
        print(f"Users Count (SQL): {result.scalar()}")
        
        result_events = conn.execute(text("SELECT count(*) FROM event"))
        print(f"Events Count (SQL): {result_events.scalar()}")

if __name__ == "__main__":
    check_db()
