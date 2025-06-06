from ....common.interface.ras.ras import RasInterface
from ....common.schemas.request import NewResourceConsumptionCounter


def create_new_counter(req: NewResourceConsumptionCounter):
    try:
        rac = RasInterface(req=req)
        rac_data = rac.java_get_resource_consumption_counters()
        for one_data in rac_data:
            if one_data.getName() == req.name:
                return {
                    "error": 0,
                    "message": f"Cчетчик с именем {req.name} в кластере {req.cluster_id} уже существует",
                    "data": ""
                }
        new_object = rac.java_reg_resource_consumption_counter(property=req)
        rac_data = rac.java_get_resource_consumption_counters()
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
            "message": f"При проверке в списке существующих счетчиков создаваемый счетчик с именем {req.name} не найден",
            "data": ""
        }
        for one_data in rac_data:
            if one_data.getName() == req.name:
                result: dict = {
                    "error": 0,
                    "message": f"Новый счетчик с именем {req.name} создан успешно",
                    "data": {"new_object": new_object}
                }
    except Exception as ex:
        return {
            "error": 1,
            "message": f"Произошла ошибка при обработке данных. Текст ошибки: {ex}",
            "data": {}
        }
    return result
