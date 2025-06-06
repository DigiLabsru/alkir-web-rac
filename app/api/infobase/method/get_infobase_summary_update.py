from ....common.interface.ras.ras import RasInterface
from ....common.schemas.request import InfoBaseSummaryUpdate


def get_infobase_summary_update(req: InfoBaseSummaryUpdate):
    try:
        rac = RasInterface(req=req)
        rac.java_update_infobase_short(new_ib_descr=req.new_ib_descr)
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
