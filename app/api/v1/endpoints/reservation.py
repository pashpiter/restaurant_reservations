from http import HTTPStatus

from fastapi import APIRouter, Depends
from sqlalchemy.ext.asyncio import AsyncSession

from api.v1.utils import check_conflicts
from api.v1.validators import is_one_reservation
from db.crud.reservation import reservation_crud
from db.database import get_session
from schemas.reservation import Reservation, ReservationCreate, ReservationRead

router = APIRouter(prefix='/reservations')


@router.get('/')
async def get_all_reservations(
    session: AsyncSession = Depends(get_session)
) -> list[Reservation]:
    reservations: list[Reservation] = await reservation_crud.get_all(session)
    await is_one_reservation(reservations)
    return reservations


@router.post('/')
async def create_reservation(
    reservation_create: ReservationCreate,
    session: AsyncSession = Depends(get_session)
) -> ReservationRead:
    await check_conflicts(session, reservation_create)
    reservation = await reservation_crud.create(
        session, reservation_create.model_dump()
    )
    return reservation


@router.delete('/{reservation_id}', status_code=HTTPStatus.NO_CONTENT)
async def delete_reservation(
    reservation_id: int,
    session: AsyncSession = Depends(get_session)
) -> None:
    await reservation_crud.delete(session, reservation_id)
