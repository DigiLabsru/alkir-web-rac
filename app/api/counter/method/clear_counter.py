from ....common.interface.ras.ras import RasInterface
from ....common.schemas.request import ResourceConsumptionCounterValueInfo


def clear_counter(req: ResourceConsumptionCounterValueInfo):
    try:
        rac = RasInterface(req=req)
        rac.java_clear_resource_consumption_counter_accumulated_values(counter_name=req.counter_name, object_name=req.object_name)
        rac.close()
    except Exception as ex:
        return {
            "error": 1,
            "message": f"Произошла ошибка при получении данных из RAS. Текст ошибки: {ex}",
            "data": []
        }
    return {
        "error": 0,
        "message": f"Данные счетчика с именем {req.counter_name} и объекта {req.object_name} в кластере {req.cluster_id} очищены успешно",
        "data": ""
    }
