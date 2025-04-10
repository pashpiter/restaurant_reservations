from datetime import datetime

from sqlmodel import Field, SQLModel, Relationship

from schemas.table import Table


class ReservationBase(SQLModel):
    customer_name: str = Field(
        description='Имя заказчика'
    )
    reservation_time: datetime = Field(
        description='Время начала брони'
    )
    duration_minutes: int = Field(
        description='Продолжительность брони в минутах'
    )


class Reservation(ReservationBase, table=True):
    id: int | None = Field(
        default=None, primary_key=True
    )
    table_id: int = Field(
        foreign_key='table.id'
    )

    table: Table = Relationship(
        sa_relationship_kwargs={'lazy': 'joined'}
    )


class ReservationCreate(ReservationBase):
    pass


class ReservationRead(ReservationBase):
    pass
