import asyncio
import httpx
from sqlalchemy.ext.asyncio import create_async_engine
from sqlalchemy import text
import time

DATABASE_URL = "postgresql+asyncpg://python_user:55555@localhost:5432/events_hub"
BASE_URL = "http://localhost:8000/api/v1/auth"

async def verify_otp_flow():
    email = f"test_verify_{int(time.time())}@example.com"
    password = "password123"
    
    async with httpx.AsyncClient() as client:
        # 1. Register
        print(f"1. Registering user: {email}")
        reg_res = await client.post(f"{BASE_URL}/register", json={
            "email": email,
            "password": password,
            "full_name": "Verification Tester",
            "is_active": False
        })
        assert reg_res.status_code == 200, f"Registration failed: {reg_res.text}"
        
        # 2. Verify Inactive state in DB
        print("2. Verifying database state...")
        engine = create_async_engine(DATABASE_URL)
        async with engine.connect() as conn:
            result = await conn.execute(text("SELECT is_active, reset_otp FROM \"user\" WHERE email = :email"), {"email": email})
            user = result.fetchone()
            assert user is not None, "User not found in DB"
            assert user[0] == False, f"User should be inactive, but is_active={user[0]}"
            otp = user[1]
            assert otp is not None, "OTP not stored in DB"
            print(f"   Success: User is inactive. Found OTP: {otp}")
            
            # 3. Test Login (Should Fail)
            print("3. Testing login before verification...")
            login_res = await client.post(f"{BASE_URL}/login", data={"username": email, "password": password})
            assert login_res.status_code == 403, f"Login should have failed with 403, got {login_res.status_code}"
            print("   Success: Login blocked as expected.")
            
            # 4. Verify OTP
            print(f"4. Verifying OTP: {otp}")
            verify_res = await client.post(f"{BASE_URL}/verify-signup-otp", json={"email": email, "otp": otp})
            assert verify_res.status_code == 200, f"OTP verification failed: {verify_res.text}"
            print("   Success: OTP verified.")
            
            # 5. Verify Active state in DB
            print("5. Verifying user is now active in DB...")
            result = await conn.execute(text("SELECT is_active, reset_otp FROM \"user\" WHERE email = :email"), {"email": email})
            user = result.fetchone()
            assert user[0] == True, f"User should be active now, but is_active={user[0]}"
            assert user[1] is None, "OTP should be cleared after verification"
            print("   Success: User is now active.")
            
            # 6. Test Login (Should Succeed)
            print("6. Testing login after verification...")
            login_res = await client.post(f"{BASE_URL}/login", data={"username": email, "password": password})
            assert login_res.status_code == 200, f"Login failed after verification: {login_res.text}"
            print("   Success: Login successful.")
            
        await engine.dispose()
        print("\nALL OTP FLOW TESTS PASSED SUCCESSFULLY!")

if __name__ == "__main__":
    asyncio.run(verify_otp_flow())
