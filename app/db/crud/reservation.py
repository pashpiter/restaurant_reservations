from datetime import datetime

from sqlalchemy.engine import Result
from sqlalchemy.ext.asyncio import AsyncSession
from sqlmodel import select, func

from db.crud.base import CRUDBase
from schemas.reservation import Reservation


class CRUDReservation(CRUDBase):

    async def find_conflicting_reservations(
            self,
            session: AsyncSession,
            start: datetime,
            end: datetime,
            table_id: int
    ) -> list[Reservation | None]:
        stmt = (
            select(Reservation)
            .where(Reservation.table_id == table_id)
            .where(
                (start < Reservation.reservation_time + func.make_interval(
                    0, 0, 0, 0, 0, Reservation.duration_minutes, 0
                )) &
                (end > Reservation.reservation_time)
            )
            .order_by(Reservation.reservation_time)
        )
        results: Result = await session.execute(stmt)
        return results.scalars().all()


reservation_crud = CRUDReservation(Reservation)
