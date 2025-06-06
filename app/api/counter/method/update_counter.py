from ....common.interface.ras.ras import RasInterface
from ....common.schemas.request import UpdateResourceConsumptionCounter


def update_counter(req: UpdateResourceConsumptionCounter):
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
        rac.java_update_resource_consumption_counter(property=req)
        rac.close()
    except Exception as ex:
        return {
            "error": 1,
            "message": f"Произошла ошибка при получении данных из RAS. Текст ошибки: {ex}",
            "data": []
        }
    return {
        "error": 0,
        "message": f"Данные счетчика с именем {req.counter_name} в кластере {req.cluster_id} обновлены успешно",
        "data": ""
    }
