import jpype

from ....common.interface.ras.ras import RasInterface
from ....common.schemas.request import ResourceConsumptionCounterValueInfo


def get_counter_values_list(req: ResourceConsumptionCounterValueInfo):
    try:
        rac = RasInterface(req=req)
        SimpleDateFormat = jpype.JClass('java.text.SimpleDateFormat')
        sdf = SimpleDateFormat("yyyy-MM-dd HH:mm:ss")
        rac_data = rac.java_get_resource_consumption_counter_values(counter_name=req.counter_name, object_name=req.object_name)
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
                    "active_session_count": one_data.getActiveSessionCount(),
                    "calls": one_data.getCalls(),
                    "collection_time": one_data.getCollectionTime(),
                    "cpu_time": one_data.getCpuTime(),
                    "dbms_dytes": one_data.getDbmsBytes(),
                    "duration": one_data.getDuration(),
                    "duration_dbms": one_data.getDurationDbms(),
                    "duration_service": one_data.getDurationService(),
                    "memory": one_data.getMemory(),
                    "object": one_data.getObject(),
                    "read_bytes": one_data.getReadBytes(),
                    "session_count": one_data.getSessionCount(),
                    "time": sdf.format(one_data.getTime()),
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
