from typing import AsyncGenerator, Optional
from contextlib import asynccontextmanager
from sqlmodel.ext.asyncio.session import AsyncSession
from sqlmodel import SQLModel
from sqlalchemy.ext.asyncio import create_async_engine, async_sessionmaker, AsyncEngine
from app.config import Settings
from app.models import inv
from app.models.inv import InvDB

async_engine: Optional[AsyncEngine] = None
async_session_maker: Optional[async_sessionmaker[AsyncSession]] = None

async def init_db(settings: Settings):
    global async_engine, async_session_maker
    async_engine = create_async_engine(settings.DATABASE_URL, echo=settings.DB_ECHO)
    async_session_maker = async_sessionmaker(async_engine, class_=AsyncSession, expire_on_commit=False)

    async with async_engine.begin() as conn:
        await conn.run_sync(SQLModel.metadata.create_all)


async def get_session() -> AsyncGenerator[AsyncSession, None]:
    async with async_session_maker() as session:
        yield session


# @asynccontextmanager
# async def get_session() -> AsyncGenerator[AsyncSession, None]:
#     if not async_session_maker:
#         raise RuntimeError("Database not initialized")
#     async with async_session_maker() as session:
#         yield session

async def close_db():
    global async_engine
    if async_engine:
        await async_engine.dispose()
