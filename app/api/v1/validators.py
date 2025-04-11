from datetime import datetime, timedelta

from core.exceptions import NoObj, ReservationConflict, PastTimeReservation
from schemas.reservation import Reservation
from schemas.table import Table

NO_OBJ = 'Нет ни одного объекта'
RESERVATATION_CONFLICT = 'Cтолик занят c {} до {}'
PAST_TIME_RESERVATION = 'Нельзя забронировать столик в прошлом'


async def is_one_obj(
        obj: list[Table] | list[Reservation] | list[None]
) -> None:
    '''Проверяет есть ли хоть один объект'''
    if not obj:
        raise NoObj(NO_OBJ)


async def is_reservation_conflict(
        reservations: list[Reservation | None]
) -> None:
    '''Проверяет на наличие пересечений существующих и новой брони'''
    if reservations:
        raise ReservationConflict(
            [
                RESERVATATION_CONFLICT.format(
                    r.reservation_time,
                    r.reservation_time + timedelta(minutes=r.duration_minutes)
                ) for r in reservations
            ]
        )


async def is_past_time(dt: datetime) -> None:
    if dt < datetime.now():
        raise PastTimeReservation(PAST_TIME_RESERVATION)
