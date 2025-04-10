from fastapi import APIRouter, Depends
from sqlalchemy.ext.asyncio import AsyncSession

from db.database import get_session
from schemas.reservation import Reservation, ReservationCreate, ReservationRead

router = APIRouter(prefix='/reservations')


@router.get('/')
async def get_all_reservations(
    session: AsyncSession = Depends(get_session)
) -> list[Reservation]:
    pass


@router.post('/')
async def create_reservation(
    reservation_create: ReservationCreate,
    session: AsyncSession = Depends(get_session)
) -> ReservationRead:
    pass


@router.delete('/{reservation_id}')
async def delete_reservation(
    reservation_id: int,
    session: AsyncSession = Depends(get_session)
) -> None:
    pass
