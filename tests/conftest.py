import asyncio
from pathlib import Path

import pytest
import pytest_asyncio
from httpx import ASGITransport, AsyncClient
from sqlalchemy.ext.asyncio import (AsyncSession, async_sessionmaker,
                                    create_async_engine)
from sqlalchemy_utils import create_database, database_exists, drop_database
from sqlmodel import SQLModel, text

from core.config import settings
from db.database import get_session
from main import app
from schemas.reservation import Reservation
from schemas.table import Table

ALEMBIC_INI_PATH = str(Path(__file__).parent.parent / 'app' / 'alembic.ini')
ASYNC_TEST_DB_URL = settings.postgres.postgres_url + '_test'
SYNC_TEST_DB_URL = ASYNC_TEST_DB_URL.replace('+asyncpg', '')


@pytest.fixture(scope="session")
def event_loop():
    loop = asyncio.get_event_loop_policy().get_event_loop()
    yield loop


@pytest.fixture(scope="session")
def setup_test_db():
    if not database_exists(SYNC_TEST_DB_URL):
        create_database(SYNC_TEST_DB_URL)
    yield
    if database_exists(SYNC_TEST_DB_URL):
        drop_database(SYNC_TEST_DB_URL)


@pytest_asyncio.fixture(name='session', scope='session')
async def session_fixture(setup_test_db):
    '''Фикстура для сессии'''
    engine = create_async_engine(ASYNC_TEST_DB_URL)
    async with engine.begin() as conn:
        await conn.run_sync(SQLModel.metadata.create_all)
    session = async_sessionmaker(engine, expire_on_commit=False)
    async with session() as s:
        yield s
    async with engine.begin() as conn:
        await conn.run_sync(SQLModel.metadata.drop_all)
    await engine.dispose()


@pytest_asyncio.fixture(name='client', scope='session')
async def client_fixture(session: AsyncSession):
    '''Клиентская фикстура'''
    def get_session_override():
        return session
    app.dependency_overrides[get_session] = get_session_override
    async with AsyncClient(
        transport=ASGITransport(app=app), base_url="http://test"
    ) as client:
        yield client
    app.dependency_overrides.clear()


@pytest.fixture(autouse=True)
async def clean_tables(session: AsyncSession):
    """Автоматическая очистка таблиц перед каждым тестом"""
    await session.execute(text('TRUNCATE TABLE "table" CASCADE'))
    await session.commit()


pytest_plugins = [
    "tests.fixtures.tables",
    "tests.fixtures.reservations"
]
