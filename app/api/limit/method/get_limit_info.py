from ....common.interface.ras.ras import RasInterface
from ....common.schemas.request import ResourceConsumptionLimitInfo


def get_limit_info(req: ResourceConsumptionLimitInfo):
    try:
        rac = RasInterface(req=req)
        rac_data = rac.java_get_resource_consumption_limit_info(limit_name=req.limit_name)
        rac.close()
    except Exception as ex:
        return {
            "error": 1,
            "message": f"Произошла ошибка при получении данных из RAS. Текст ошибки: {ex}",
            "data": []
        }
    try:
        result: dict = {
            "action": rac_data.getAction(),
            "active_session_count": rac_data.getActiveSessionCount(),
            "calls": rac_data.getCalls(),
            "counter": rac_data.getCounter(),
            "cpu_time": rac_data.getCpuTime(),
            "dbms_bytes": rac_data.getDbmsBytes(),
            "description": rac_data.getDescription(),
            "duration": rac_data.getDuration(),
            "duration_dbms": rac_data.getDurationDbms(),
            "duration_service": rac_data.getDurationService(),
            "memory": rac_data.getMemory(),
            "message": rac_data.getMessage(),
            "name": rac_data.getName(),
            "read_bytes": rac_data.getReadBytes(),
            "session_count": rac_data.getSessionCount(),
            "write_bytes": rac_data.getWriteBytes()
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
