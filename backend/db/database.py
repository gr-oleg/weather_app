from motor import motor_asyncio

from backend.config import settings


client = motor_asyncio.AsyncIOMotorClient(settings)
