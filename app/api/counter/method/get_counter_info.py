from ....common.interface.ras.ras import RasInterface
from ....common.schemas.request import ResourceConsumptionCounterInfo


def get_counter_info(req: ResourceConsumptionCounterInfo):
    try:
        rac = RasInterface(req=req)
        rac_data = rac.java_get_resource_consumption_counter_info(server_id=req.counter_name)
        rac.close()
    except Exception as ex:
        return {
            "error": 1,
            "message": f"Произошла ошибка при получении данных из RAS. Текст ошибки: {ex}",
            "data": []
        }
    try:
        result: dict = {
            "collection_time": rac_data.getCollectionTime(),
            "description": rac_data.getDescription(),
            "filter_type": rac_data.getFilterType(),
            "filter_value": rac_data.getFilterValue(),
            "group": rac_data.getGroup(),
            "name": rac_data.getName(),
            "is_analyze_active_session_count": rac_data.is_analyzeActiveSessionCount(),
            "is_analyze_calls": rac_data.is_analyzeCalls(),
            "is_analyze_cpu_time": rac_data.is_analyzeCpuTime(),
            "is_analyze_dbms_bytes": rac_data.is_analyzeDbmsBytes(),
            "is_analyze_duration": rac_data.is_analyzeDuration(),
            "is_analyze_duration_dbms": rac_data.is_analyzeDurationDbms(),
            "is_analyze_duration_service": rac_data.is_analyzeDurationService(),
            "is_analyze_memory": rac_data.is_analyzeMemory(),
            "is_analyze_read_bytes": rac_data.is_analyzeReadBytes(),
            "is_analyze_session_count": rac_data.is_analyzeSessionCount(),
            "is_analyze_write_bytes": rac_data.is_analyzeWriteBytes()
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
