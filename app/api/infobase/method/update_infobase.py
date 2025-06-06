from ....common.interface.ras.ras import RasInterface
from ....common.schemas.request import UpdateInfobaseProperty


def update_infobase(req: UpdateInfobaseProperty):
    try:
        rac = RasInterface(req=req)
        rac.java_update_infobase(update_infabase_property=req)
        rac.close()
        return {
            "error": 0,
            "message": "Обновление информации для информационной базы прошло успешно",
            "data": ""
        }
    except Exception as ex:
        return {
            "error": 1,
            "message": f"Произошла ошибка при получении данных из RAS. Текст ошибки: {ex}",
            "data": ""
        }
