from core.exceptions import NoTables, NoReservations
from schemas.reservation import Reservation
from schemas.table import Table

NO_TABLES = 'Нет ни одного стола'
NO_RESERVATIONS = 'Нет ни одной брони'


async def is_one_table(tables: list[Table]) -> None:
    if not tables:
        raise NoTables(NO_TABLES)


async def is_one_reservation(reservations: list[Reservation]) -> None:
    if not reservations:
        raise NoReservations(NO_RESERVATIONS)
