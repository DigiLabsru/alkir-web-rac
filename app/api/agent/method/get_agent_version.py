from ....common.interface.ras.ras import RasInterface
from ....common.schemas.request import BaseRequest


def get_agent_version(req: BaseRequest):
    try:
        rac = RasInterface(req=req)
        admins_list = rac.java_get_agent_version()
        rac.close()
        return {
            "error": 0,
            "message": "",
            "data": admins_list
        }
    except Exception as ex:
        return {
            "error": 1,
            "message": f"Произошла ошибка при получении данных из RAS. Текст ошибки: {ex}",
            "data": ""
        }
