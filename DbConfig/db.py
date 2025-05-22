import os
from motor.motor_asyncio import AsyncIOMotorClient
from dotenv import load_dotenv

load_dotenv()

MONGODB_URI = os.getenv("MONGODB_URI")
client = AsyncIOMotorClient(MONGODB_URI)

db = client["fastapi"]
product_collection = db["products"]
person_collection=db['information']
register_collection=db['register']