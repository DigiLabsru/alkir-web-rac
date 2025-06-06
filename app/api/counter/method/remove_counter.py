from ....common.interface.ras.ras import RasInterface
from ....common.schemas.request import ResourceConsumptionCounterInfo


def remove_counter(req: ResourceConsumptionCounterInfo):
    try:
        rac = RasInterface(req=req)
        rac_data = rac.java_get_resource_consumption_counters()
        find_flag: bool = False
        for one_data in rac_data:
            if one_data.getName() == req.counter_name:
                find_flag = True
        if find_flag is False:
            return {
                "error": 0,
                "message": f"Cчетчик с именем {req.counter_name} в кластере {req.cluster_id} не найден",
                "data": ""
            }
        rac.java_unreg_resource_consumption_counter(counter_name=req.counter_name)
        rac_data = rac.java_get_resource_consumption_counters()
        rac.close()
    except Exception as ex:
        return {
            "error": 1,
            "message": f"Произошла ошибка при получении данных из RAS. Текст ошибки: {ex}",
            "data": ""
        }
    try:
        result: dict = {
            "error": 0,
            "message": f"Cчетчик с именем {req.counter_name} в кластере {req.cluster_id} удален успешно",
            "data": ""
        }
        for one_data in rac_data:
            if one_data.getName() == req.counter_name:
                result: dict = {
                    "error": 1,
                    "message": f"При проверке в списке существующих счетчиков найден удаляемый счетчик с именем {req.counter_name} в кластере {req.cluster_id}",
                    "data": ""
                }
    except Exception as ex:
        return {
            "error": 1,
            "message": f"Произошла ошибка при обработке данных. Текст ошибки: {ex}",
            "data": ""
        }
    return result
