from ....common.interface.ras.ras import RasInterface
from ....common.schemas.request import InfobaseProperty


def create_infobase(req: InfobaseProperty):
    try:
        rac = RasInterface(req=req)
        new_infobase_id = rac.java_create_infobase(new_infabase=req)
        rac.close()
        return {
            "error": 0,
            "message": "Обновление информации для информационной базы прошло успешно",
            "data": new_infobase_id.toString()
        }
    except Exception as ex:
        return {
            "error": 1,
            "message": f"Произошла ошибка при получении данных из RAS. Текст ошибки: {ex}",
            "data": ""
        }
