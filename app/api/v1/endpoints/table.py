from fastapi import APIRouter, Depends
from sqlalchemy.ext.asyncio import AsyncSession

from api.v1.validators import is_one_table
from db.database import get_session
from db.crud.table import table_crud
from schemas.table import TableCreate, TableRead

router = APIRouter(prefix='/tables')


@router.get('/')
async def get_all_tables(
    session: AsyncSession = Depends(get_session)
) -> list[TableRead]:
    tables = await table_crud.get_all(session)
    await is_tables(tables)
    return tables


@router.post('/')
async def create_table(
    table_create: TableCreate,
    session: AsyncSession = Depends(get_session)
) -> TableRead:
    table = await table_crud.create(session, table_create.model_dump())
    return table


@router.delete('/{table_id}')
async def delete_table(
    table_id: int,
    session: AsyncSession = Depends(get_session)
) -> None:
    await table_crud.delete(session, table_id)
