import asyncio
from app.core.database import init_db, get_session
from app.models.schemas import User, UserCreate
from app.auth import get_password_hash
from sqlalchemy.future import select

async def debug_auth():
    print("1. Initializing DB...")
    await init_db()
    
    print("2. Hashing Password...")
    try:
        pwd = get_password_hash("testpassword")
        print(f"   Success: {pwd[:10]}...")
    except Exception as e:
        print(f"   FATAL ERROR hashing password: {e}")
        return

    print("3. Attempting to Create User in DB...")
    try:
        async for session in get_session():
            # Check if exists
            stmt = select(User).where(User.email == "test@test.com")
            res = await session.execute(stmt)
            existing = res.scalars().first()
            
            if existing:
                print("   User already exists (Table exists!).")
            else:
                user = User(
                    email="test@test.com",
                    hashed_password=pwd,
                    full_name="Test User",
                    is_active=True
                )
                session.add(user)
                await session.commit()
                print("   User created successfully!")
            break
    except Exception as e:
        print(f"   FATAL ERROR accessing DB: {e}")
        import traceback
        traceback.print_exc()

if __name__ == "__main__":
    asyncio.run(debug_auth())
