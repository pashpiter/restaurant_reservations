import pytest
from sqlalchemy.ext.asyncio import AsyncSession

from schemas.table import Table


@pytest.fixture(scope='function')
async def test_table_one(session: AsyncSession):
    """Фикстура тестового стола"""
    table = Table(
        name='Table1',
        seats=2,
        location='Балкон'
    )
    session.add(table)
    await session.commit()
    await session.refresh(table)
    return table


@pytest.fixture(scope='function')
async def test_table_two(session: AsyncSession):
    """Фикстура тестового стола"""
    table = Table(
        name='Table2',
        seats=4,
        location='Зал'
    )
    session.add(table)
    await session.commit()
    await session.refresh(table)
    return table
