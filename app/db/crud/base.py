from sqlalchemy.engine import Result
from sqlalchemy.ext.asyncio import AsyncSession
from sqlmodel import select

from db.validators import is_obj
from schemas.reservation import Reservation
from schemas.table import Table


class CRUDBase:
    def __init__(self, model: Reservation | Table):
        self.model = model

    async def create(
            self, session: AsyncSession, obj_in: dict
    ) -> Reservation | Table:
        '''Создает новую запись в базе данных'''
        db_obj = self.model(**obj_in)
        session.add(db_obj)
        await session.commit()
        await session.refresh(db_obj)
        return db_obj

    async def get(
            self, session: AsyncSession, id: int
    ) -> Reservation | Table:
        '''Получение объекта из базы данных по ID'''
        stmt = select(self.model).where(self.model.id == id)
        result: Result = await session.execute(stmt)
        return result.scalars().first()

    async def get_all(
            self, session: AsyncSession
    ) -> list[Reservation] | list[Table]:
        '''Получение всех объектов модели мз базы данных'''
        stmt = select(self.model)
        result: Result = await session.execute(stmt)
        return result.scalars().all()

    async def delete(
            self, session: AsyncSession, id: int
    ) -> None:
        '''Удаление объекта из базы данных по ID'''
        db_obj = await self.get(session, id)
        await is_obj(db_obj)
        await session.delete(db_obj)
        await session.commit()
