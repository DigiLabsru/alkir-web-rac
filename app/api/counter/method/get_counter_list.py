from ....common.interface.ras.ras import RasInterface
from ....common.schemas.request import BaseRequest


def get_counter_list(req: BaseRequest):
    try:
        rac = RasInterface(req=req)
        rac_data = rac.java_get_resource_consumption_counters()
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
                    "collection_time": one_data.getCollectionTime(),
                    "description": one_data.getDescription(),
                    "filter_type": one_data.getFilterType(),
                    "filter_value": one_data.getFilterValue(),
                    "group": one_data.getGroup(),
                    "name": one_data.getName(),
                    "is_analyze_active_session_count": one_data.is_analyzeActiveSessionCount(),
                    "is_analyze_calls": one_data.is_analyzeCalls(),
                    "is_analyze_cpu_time": one_data.is_analyzeCpuTime(),
                    "is_analyze_dbms_bytes": one_data.is_analyzeDbmsBytes(),
                    "is_analyze_duration": one_data.is_analyzeDuration(),
                    "is_analyze_duration_dbms": one_data.is_analyzeDurationDbms(),
                    "is_analyze_duration_service": one_data.is_analyzeDurationService(),
                    "is_analyze_memory": one_data.is_analyzeMemory(),
                    "is_analyze_read_bytes": one_data.is_analyzeReadBytes(),
                    "is_analyze_session_count": one_data.is_analyzeSessionCount(),
                    "is_analyze_write_bytes": one_data.is_analyzeWriteBytes()
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
