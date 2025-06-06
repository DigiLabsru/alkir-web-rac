import jpype

from ....common.interface.ras.ras import RasInterface
from ....common.schemas.request import ConnectionIBList


def get_connection_infobase(req: ConnectionIBList):
    try:
        rac = RasInterface(req=req)
        rac_data = rac.java_get_infobase_connections_short(infobase_id=req.infobase_id)
        rac.close()
    except Exception as ex:
        return {
            "error": 1,
            "message": f"Произошла ошибка при получении данных из RAS. Текст ошибки: {ex}",
            "data": []
        }
    try:
        result: list = []
        for one_data in rac_data:
            SimpleDateFormat = jpype.JClass('java.text.SimpleDateFormat')
            sdf = SimpleDateFormat("yyyy-MM-dd HH:mm:ss")
            result.append(
                {
                    "application": one_data.getApplication(),
                    "blocked_by_ls": one_data.getBlockedByLs(),
                    "connected_at": sdf.format(one_data.getConnectedAt()),
                    "conn_id": one_data.getConnId(),
                    "host": one_data.getHost(),
                    "infobase_connection_id": one_data.getInfoBaseConnectionId(),
                    "infobase_id": one_data.getInfoBaseId(),
                    "session_number": one_data.getSessionNumber(),
                    "working_process_id": one_data.getWorkingProcessId()
                }
            )
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
