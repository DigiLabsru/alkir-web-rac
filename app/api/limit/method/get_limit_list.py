from ....common.interface.ras.ras import RasInterface
from ....common.schemas.request import BaseRequest


def get_limit_list(req: BaseRequest):
    try:
        rac = RasInterface(req=req)
        rac_data = rac.java_get_resource_consumption_limits()
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
            result.append(
                {
                    "action": one_data.getAction(),
                    "active_session_count": one_data.getActiveSessionCount(),
                    "calls": one_data.getCalls(),
                    "counter": one_data.getCounter(),
                    "cpu_time": one_data.getCpuTime(),
                    "dbms_bytes": one_data.getDbmsBytes(),
                    "description": one_data.getDescription(),
                    "duration": one_data.getDuration(),
                    "duration_dbms": one_data.getDurationDbms(),
                    "duration_service": one_data.getDurationService(),
                    "memory": one_data.getMemory(),
                    "message": one_data.getMessage(),
                    "name": one_data.getName(),
                    "read_bytes": one_data.getReadBytes(),
                    "session_count": one_data.getSessionCount(),
                    "write_bytes": one_data.getWriteBytes()
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
