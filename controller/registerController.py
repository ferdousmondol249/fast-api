from fastapi import HTTPException
from model.register import register_model
from DbConfig.db import register_collection
from passlib.context import CryptContext
from jose import jwt
from dotenv import load_dotenv
import os


load_dotenv()
pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

SECRET_KEY=os.getenv("TOKEN_SECRET_KEY")
ALGORITHM=os.getenv("ALGORITHM")
def create_access_token(data: dict):
    return jwt.encode(data, SECRET_KEY, algorithm=ALGORITHM)
async def registration_user(reg: register_model):
    try:
        existing_user = await register_collection.find_one({"email": reg.email})
        if existing_user:
            raise HTTPException(status_code=400, detail="User account already created, just login")

        hashed_password = pwd_context.hash(reg.password)

        reg_data = {
            "name": reg.name,
            "email": reg.email,
            "password": hashed_password
        }

        await register_collection.insert_one(reg_data)

        token = create_access_token({"sub": reg.email})
        
        return {
            "message": "User registration is successfully done",
            "data": {
                "name": reg.name,
                "email": reg.email
            },
            "token": token
        }

    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Registration failed: {str(e)}")
