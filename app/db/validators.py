from core.exceptions import NoObjWithId

NO_OBJ_WITH_ID = 'Нет объекта с таким ID'


async def is_obj(obj) -> None:
    if not obj:
        raise NoObjWithId(NO_OBJ_WITH_ID)
