from fastapi import APIRouter, Depends
from sqlalchemy.ext.asyncio import AsyncSession

from db.database import get_session
from schemas.table import Table, TableCreate, TableRead

router = APIRouter(prefix='/tables')


@router.get('/')
async def get_all_tables(
    session: AsyncSession = Depends(get_session)
) -> list[Table]:
    pass


@router.post('/')
async def create_table(
    table_create: TableCreate,
    session: AsyncSession = Depends(get_session)
) -> TableRead:
    pass


@router.delete('/{table_id}')
async def delete_table(
    table_id: int,
    session: AsyncSession = Depends(get_session)
) -> None:
    pass
