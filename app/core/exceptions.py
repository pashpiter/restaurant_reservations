from http import HTTPStatus

from fastapi import HTTPException


class NoTables(HTTPException):
    def __init__(self, message: str):
        super().__init__(HTTPStatus.BAD_REQUEST, message)


class NoObjWithId(HTTPException):
    def __init__(self, message: str):
        super().__init__(HTTPStatus.BAD_REQUEST, message)


class NoReservations(HTTPException):
    def __init__(self, message: str):
        super().__init__(HTTPStatus.BAD_REQUEST, message)


class ReservationConflict(HTTPException):
    def __init__(self, message: str):
        super().__init__(HTTPStatus.BAD_REQUEST, message)
