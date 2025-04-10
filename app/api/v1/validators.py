from core.exceptions import NoTables

NO_TABLES = 'Нет ни одного стола'


async def is_tables(tables):
    if not tables:
        raise NoTables(NO_TABLES)
