from ....common.interface.ras.ras import RasInterface
from ....common.schemas.request import InfoBase


def get_infobase_summary_info(req: InfoBase):
    try:
        rac = RasInterface(req=req)
        infobase_list = rac.java_get_infobase_short_info()
        rac.close()
    except Exception as ex:
        return {
            "error": 1,
            "message": f"Произошла ошибка при получении данных из RAS. Текст ошибки: {ex}",
            "data": ""
        }
    try:
        return {
            "error": 0,
            "message": "",
            "data": {
                "name": infobase_list.getName(),
                "infobase_id": infobase_list.getInfoBaseId().toString(),
                "description": infobase_list.getDescr()
            }
        }
    except Exception as ex:
        return {
            "error": 1,
            "message": f"Произошла ошибка при обработке данных. Текст ошибки: {ex}",
            "data": []
        }
