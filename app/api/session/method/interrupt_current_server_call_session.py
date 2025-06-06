from ....common.interface.ras.ras import RasInterface
from ....common.schemas.request import TerminateSession


def interrupt_current_server_call_session(req: TerminateSession):
    try:
        rac = RasInterface(req=req)
        rac.java_interrupt_current_server_call(sid=req.session_id, message=req.message)
        rac.close()
        return {
            "error": 0,
            "message": "Текущий серверный вызов был успешно прерван",
            "data": ""
        }
    except Exception as ex:
        return {
            "error": 1,
            "message": f"Произошла ошибка при получении данных из RAS. Текст ошибки: {ex}",
            "data": ""
        }
