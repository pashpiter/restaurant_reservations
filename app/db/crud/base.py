from sqlalchemy.engine import Result
from sqlalchemy.ext.asyncio import AsyncSession
from sqlmodel import select

from schemas.table import Table
from schemas.reservation import Reservation


class CRUDBase:
    def __init__(self, model: Reservation | Table):
        self.model = model

    async def create(
            self, session: AsyncSession, obj_in: dict
    ) -> Reservation | Table:
        db_obj = self.model(**obj_in)
        session.add(db_obj)
        await session.commit()
        await session.refresh(db_obj)
        return db_obj

    async def get(
            self, session: AsyncSession, id: int
    ) -> Reservation | Table:
        stmt = select(self.model).where(self.model.id == id)
        result: Result = await session.execute(stmt)
        return result.scalars().first()

    async def get_all(
            self, session: AsyncSession
    ) -> list[Reservation | Table]:
        stmt = select(self.model)
        result: Result = await session.execute(stmt)
        return result.scalars().all()

    async def delete(
            self, session: AsyncSession, id: int
    ) -> None:
        db_obj = await self.get(session, id)
        if db_obj:
            await session.delete(db_obj)
            await session.commit()
