from ....common.interface.ras.ras import RasInterface
from ....common.schemas.request import DeleteInfoBase


def drop_infobase(req: DeleteInfoBase):
    try:
        find_base_flag: bool = False
        rac = RasInterface(req=req)
        for one_base in rac.java_get_infobases_short():
            if one_base.getName() == req.ib_name:
                find_base_flag = True
        if find_base_flag is False:
            return {
                "error": 1,
                "message": f"Информационная база {req.ib_name} не найдена, удаление невозможно",
                "data": ""
            }
        rac.java_drop_infobase(infobase_creation_mode=req.infobase_creation_mode)
        rac.close()
        return {
            "error": 0,
            "message": "Удаление информационной базы прошло успешно",
            "data": ""
        }
    except Exception as ex:
        return {
            "error": 1,
            "message": f"Произошла ошибка при получении данных из RAS. Текст ошибки: {ex}",
            "data": ""
        }
