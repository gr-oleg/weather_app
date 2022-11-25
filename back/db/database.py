from motor import motor_asyncio

from back.config import settings


client = motor_asyncio.AsyncIOMotorClient(settings)
