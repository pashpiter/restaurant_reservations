from http import HTTPStatus

from fastapi import HTTPException


class NoTables(HTTPException):
    def __init__(self, message: str):
        super().__init__(HTTPStatus.NO_CONTENT, message)


class NoObjWithId(HTTPException):
    def __init__(self, message: str):
        super().__init__(HTTPStatus.NO_CONTENT, message)