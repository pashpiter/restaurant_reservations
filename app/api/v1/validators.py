from datetime import timedelta

from core.exceptions import NoReservations, NoTables, ReservationConflict
from schemas.reservation import Reservation
from schemas.table import Table

NO_TABLES = 'Нет ни одного стола'
NO_RESERVATIONS = 'Нет ни одной брони'
RESERVATATION_CONFLICT = 'Cтолик занят c {} до {}'


async def is_one_table(tables: list[Table | None]) -> None:
    if not tables:
        raise NoTables(NO_TABLES)


async def is_one_reservation(reservations: list[Reservation | None]) -> None:
    if not reservations:
        raise NoReservations(NO_RESERVATIONS)


async def is_reservation_conflict(
        reservations: list[Reservation | None]
) -> None:
    if reservations:
        raise ReservationConflict(
            [
                RESERVATATION_CONFLICT.format(
                    r.reservation_time,
                    r.reservation_time + timedelta(minutes=r.duration_minutes)
                ) for r in reservations
            ]
        )
