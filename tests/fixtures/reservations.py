from datetime import datetime, timedelta

import pytest
from sqlalchemy.ext.asyncio import AsyncSession

from schemas.reservation import Reservation
from schemas.table import Table


@pytest.fixture
async def test_reservation(session: AsyncSession, test_table_one: Table):
    """Фикстура тестового бронирования"""
    reservation = Reservation(
        table_id=test_table_one.id,
        customer_name="Никита Литвинков",
        reservation_time=datetime.now(),
        duration_minutes=120
    )
    session.add(reservation)
    await session.commit()
    await session.refresh(reservation)
    return reservation
