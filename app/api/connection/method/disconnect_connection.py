from ....common.interface.ras.ras import RasInterface
from ....common.schemas.request import ConnectionInfoDis


def disconnect_connection(req: ConnectionInfoDis):
    try:
        rac = RasInterface(req=req)
        admins_list = rac.diconnect_connection(req.process_id, req.connection_id)
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
