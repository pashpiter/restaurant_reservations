from sqlmodel import Field, SQLModel


class TableBase(SQLModel):
    name: str = Field(
        description='Название стола',
        schema_extra={'example': 'Table 1'}
    )
    seats: int = Field(
        description='Количество мест за столом'
    )
    location: str = Field(
        description='Располодение стола',
        schema_extra={'example': 'Зал у окна'}
    )


class Table(TableBase):
    id: int | None = Field(
        default=None, primary_key=True
    )


class TableCreate(TableBase):
    pass


class TableRead(TableBase):
    pass
