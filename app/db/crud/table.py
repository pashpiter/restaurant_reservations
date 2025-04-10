from db.crud.base import CRUDBase
from schemas.table import Table


class CRUDTable(CRUDBase):
    pass


table_crud = CRUDTable(Table)
