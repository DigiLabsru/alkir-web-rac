from ....common.interface.ras.ras import RasInterface
from ....common.schemas.request import TerminateSession


def terminate_session(req: TerminateSession):
    try:
        rac = RasInterface(req=req)
        rac.java_terminate_session(sid=req.session_id, message=req.message)
        rac.close()
        return {
            "error": 0,
            "message": "Сессия была успешно завершена",
            "data": ""
        }
    except Exception as ex:
        return {
            "error": 1,
            "message": f"Произошла ошибка при получении данных из RAS. Текст ошибки: {ex}",
            "data": ""
        }
