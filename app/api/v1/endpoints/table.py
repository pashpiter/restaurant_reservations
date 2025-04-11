from http import HTTPStatus

from fastapi import APIRouter, Depends
from sqlalchemy.ext.asyncio import AsyncSession

from api.v1.validators import is_one_obj
from db.crud.table import table_crud
from db.database import get_session
from schemas.table import TableCreate, TableRead

router = APIRouter(prefix='/tables')


@router.get('/')
async def get_all_tables(
    session: AsyncSession = Depends(get_session)
) -> list[TableRead]:
    '''Возвращает все существующие столы'''
    tables = await table_crud.get_all(session)
    await is_one_obj(tables)
    return tables


@router.post('/')
async def create_table(
    table_create: TableCreate,
    session: AsyncSession = Depends(get_session)
) -> TableRead:
    '''Создает новый стол'''
    table = await table_crud.create(session, table_create.model_dump())
    return table


@router.delete('/{table_id}', status_code=HTTPStatus.NO_CONTENT)
async def delete_table(
    table_id: int,
    session: AsyncSession = Depends(get_session)
) -> None:
    '''Удаляет стол по table_id'''
    await table_crud.delete(session, table_id)
