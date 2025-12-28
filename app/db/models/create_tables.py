import asyncio
from sqlmodel import SQLModel
from sqlalchemy.ext.asyncio import create_async_engine, AsyncEngine
from app.models.mini import User, Group  # import your models
from app.config import Settings
settings = Settings() 

# --------------------------
# Database URL
# --------------------------

async def create_tables():
    engine: AsyncEngine = create_async_engine(settings.DATABASE_URL, echo=True)
    async with engine.begin() as conn:
        await conn.run_sync(SQLModel.metadata.create_all)
    await engine.dispose()
    print("Tables created successfully!")

if __name__ == "__main__":
    asyncio.run(create_tables())
