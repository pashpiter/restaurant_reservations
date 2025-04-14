from sqlmodel import Field, SQLModel


class TableBase(SQLModel):
    name: str = Field(
        description='Название стола',
        unique=True,
        schema_extra={'example': 'Table 1'}
    )
    seats: int = Field(
        description='Количество мест за столом',
        ge=1
    )
    location: str = Field(
        description='Расположение стола',
        schema_extra={'example': 'Зал у окна'}
    )


class Table(TableBase, table=True):
    id: int | None = Field(
        default=None, primary_key=True
    )


class TableCreate(TableBase):
    pass


class TableRead(TableBase):
    id: int
