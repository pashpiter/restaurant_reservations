from sqlalchemy.ext.asyncio import AsyncSession, create_async_engine
from sqlalchemy.orm import sessionmaker

from core.config import settings

async_engine = create_async_engine(
    settings.postgres.postgres_url, echo=settings.app.debug
)

async_session_factory = sessionmaker(
    async_engine,
    class_=AsyncSession,
    expire_on_commit=False,
)


async def get_session():
    '''Async Session с БД'''
    async with async_session_factory() as session:
        yield session
