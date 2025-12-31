from datetime import timedelta
import secrets
from fastapi import APIRouter, Depends, HTTPException, status
from fastapi.security import OAuth2PasswordRequestForm
from sqlalchemy.future import select
from sqlalchemy.ext.asyncio import AsyncSession
from google.oauth2 import id_token
from google.auth.transport import requests

from app.core.database import get_session
from app.models.schemas import User, UserCreate, UserRead, Token, GoogleToken
from app.auth import (
    get_password_hash,
    verify_password,
    create_access_token,
    ACCESS_TOKEN_EXPIRE_MINUTES,
    get_current_user
)

router = APIRouter(prefix="/auth", tags=["Authentication"])

GOOGLE_CLIENT_ID = "616951204268-dsfdjvqp7mfn41gingbs7oqntp8f4f5g.apps.googleusercontent.com"

@router.post("/register", response_model=UserRead)
async def register(user: UserCreate, session: AsyncSession = Depends(get_session)):
    # Check if user already exists
    statement = select(User).where(User.email == user.email)
    result = await session.execute(statement)
    existing_user = result.scalars().first()
    
    if existing_user:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Email already registered"
        )
    
    # Create new user
    hashed_pwd = get_password_hash(user.password)
    db_user = User(
        email=user.email,
        full_name=user.full_name,
        hashed_password=hashed_pwd,
        is_active=True
    )
    session.add(db_user)
    await session.commit()
    await session.refresh(db_user)
    return db_user

@router.post("/login", response_model=Token)
async def login(form_data: OAuth2PasswordRequestForm = Depends(), session: AsyncSession = Depends(get_session)):
    # Authenticate User
    statement = select(User).where(User.email == form_data.username) # OAuth2 form uses 'username' for the email field
    result = await session.execute(statement)
    user = result.scalars().first()
    
    if not user or not verify_password(form_data.password, user.hashed_password):
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Incorrect email or password",
            headers={"WWW-Authenticate": "Bearer"},
        )
    
    # Create Token
    access_token_expires = timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)
    access_token = create_access_token(
        data={"sub": user.email}, expires_delta=access_token_expires
    )
    return {"access_token": access_token, "token_type": "bearer"}

@router.post("/google", response_model=Token)
async def google_login(token_data: GoogleToken, session: AsyncSession = Depends(get_session)):
    try:
        # Verify the token
        idinfo = id_token.verify_oauth2_token(
            token_data.token, 
            requests.Request(), 
            GOOGLE_CLIENT_ID
        )

        email = idinfo.get("email")
        if not email:
            raise HTTPException(status_code=400, detail="Invalid Google Token: No email found")
        
        # Check if user exists
        statement = select(User).where(User.email == email)
        result = await session.execute(statement)
        user = result.scalars().first()

        if not user:
            # Create new user with random password
            random_password = secrets.token_urlsafe(16)
            hashed_pwd = get_password_hash(random_password)
            user = User(
                email=email,
                full_name=idinfo.get("name"),
                hashed_password=hashed_pwd,
                is_active=True
            )
            session.add(user)
            await session.commit()
            await session.refresh(user)
        
        # Create JWT Token
        access_token_expires = timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)
        access_token = create_access_token(
            data={"sub": user.email}, expires_delta=access_token_expires
        )
        return {"access_token": access_token, "token_type": "bearer"}

    except ValueError as e:
        # Invalid token
        raise HTTPException(status_code=401, detail=f"Invalid Google Token: {str(e)}")

@router.get("/me", response_model=UserRead)
async def read_users_me(current_user: User = Depends(get_current_user)):
    return current_user
