from ....common.interface.ras.ras import RasInterface
from ....common.schemas.request import InfoBase


def get_infobase_summary_list(req: InfoBase):
    try:
        rac = RasInterface(req=req)
        infobases_list = rac.java_get_infobases_short()
        rac.close()
    except Exception as ex:
        return {
            "error": 1,
            "message": f"Произошла ошибка при получении данных из RAS. Текст ошибки: {ex}",
            "data": ""
        }
    try:
        result: list = []
        for one_base in infobases_list:
            result.append(
                {
                    "name": one_base.getName(),
                    "infobase_id": one_base.getInfoBaseId().toString(),
                    "description": one_base.getDescr()
                }
            )
    except Exception as ex:
        return {
            "error": 1,
            "message": f"Произошла ошибка при обработке данных. Текст ошибки: {ex}",
            "data": []
        }

    return {
        "error": 0,
        "message": "",
        "data": result
    }
