from datetime import timedelta

from sqlalchemy.ext.asyncio import AsyncSession

from api.v1.validators import is_reservation_conflict
from db.crud.reservation import reservation_crud
from schemas.reservation import ReservationCreate


async def check_conflicts(
        session: AsyncSession, new_reservation: ReservationCreate
) -> None:
    start_time = new_reservation.reservation_time
    end_time = start_time + timedelta(
        minutes=new_reservation.duration_minutes
    )
    conflicts = await reservation_crud.find_conflicting_reservations(
        session, start_time, end_time, new_reservation.table_id
    )
    await is_reservation_conflict(conflicts)
