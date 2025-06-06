import jpype

from ....common.interface.ras.ras import RasInterface
from ....common.schemas.request import ConnectionInfo


def get_connection_info(req: ConnectionInfo):
    try:
        rac = RasInterface(req=req)
        rac_data = rac.java_get_connection_info_short(connection_id=req.connection_id)
        rac.close()
    except Exception as ex:
        return {
            "error": 1,
            "message": f"Произошла ошибка при получении данных из RAS. Текст ошибки: {ex}",
            "data": []
        }
    try:
        SimpleDateFormat = jpype.JClass('java.text.SimpleDateFormat')
        sdf = SimpleDateFormat("yyyy-MM-dd HH:mm:ss")
        result: dict = {
            "application": rac_data.getApplication(),
            "blocked_by_ls": rac_data.getBlockedByLs(),
            "connected_at": sdf.format(rac_data.getConnectedAt()),
            "conn_id": rac_data.getConnId(),
            "host": rac_data.getHost(),
            "infobase_connection_id": rac_data.getInfoBaseConnectionId(),
            "infobase_id": rac_data.getInfoBaseId(),
            "session_number": rac_data.getSessionNumber(),
            "working_process_id": rac_data.getWorkingProcessId()
        }
    except Exception as ex:
        return {
            "error": 1,
            "message": f"Произошла ошибка при обработке данных. Текст ошибки: {ex}",
            "data": {}
        }

    return {
        "error": 0,
        "message": "",
        "data": result
    }
