from core.exceptions import NoObj

NO_OBJ_WITH_ID = 'Нет объекта с таким ID'


async def is_obj(obj) -> None:
    '''Проверяет на наличие хоть одного объекта'''
    if not obj:
        raise NoObj(NO_OBJ_WITH_ID)
