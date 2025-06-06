from ....common.interface.ras.ras import RasInterface
from ....common.schemas.request import NewResourceConsumptionLimit


def create_new_limit(req: NewResourceConsumptionLimit):
    try:
        rac = RasInterface(req=req)
        rac_data = rac.java_get_resource_consumption_limits()
        for one_data in rac_data:
            if one_data.getName() == req.name:
                return {
                    "error": 0,
                    "message": f"Ограничение с именем {req.name} в кластере {req.cluster_id} уже существует",
                    "data": ""
                }
        new_object = rac.java_reg_resource_consumption_limit(property=req)
        rac_data = rac.java_get_resource_consumption_limits()
        rac.close()
    except Exception as ex:
        return {
            "error": 1,
            "message": f"Произошла ошибка при получении данных из RAS. Текст ошибки: {ex}",
            "data": {}
        }
    try:
        result: dict = {
            "error": 1,
            "message": f"При проверке в списке существующих ограничений создаваемое ограничение с именем {req.name} в кластере {req.cluster_id} не найдено",
            "data": ""
        }
        for one_data in rac_data:
            if one_data.getName() == req.name:
                result: dict = {
                    "error": 0,
                    "message": f"Новое ограничение с именем {req.name} создано успешно",
                    "data": {"new_object": new_object}
                }
    except Exception as ex:
        return {
            "error": 1,
            "message": f"Произошла ошибка при обработке данных. Текст ошибки: {ex}",
            "data": {}
        }
    return result
