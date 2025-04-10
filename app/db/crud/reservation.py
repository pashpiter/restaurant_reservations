from db.crud.base import CRUDBase
from schemas.reservation import Reservation


class CRUDReservation(CRUDBase):
    pass


reservation_crud = CRUDReservation(Reservation)
