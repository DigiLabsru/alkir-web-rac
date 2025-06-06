from ....common.interface.ras.ras import RasInterface
from ....common.schemas.request import NewResourceConsumptionLimit


def update_limit(req: NewResourceConsumptionLimit):
    try:
        rac = RasInterface(req=req)
        rac_data = rac.java_get_resource_consumption_limits()
        find_flag: bool = False
        for one_data in rac_data:
            if one_data.getName() == req.name:
                find_flag = True
        if find_flag is False:
            return {
                "error": 0,
                "message": f"Ограничение с именем {req.name} в кластере {req.cluster_id} не найден",
                "data": ""
            }
        rac.java_update_resource_consumption_limit(property=req)
        rac.close()
    except Exception as ex:
        return {
            "error": 1,
            "message": f"Произошла ошибка при получении данных из RAS. Текст ошибки: {ex}",
            "data": []
        }
    return {
        "error": 0,
        "message": f"Данные ограничения с именем {req.name} в кластере {req.cluster_id} обновлены успешно",
        "data": ""
    }
