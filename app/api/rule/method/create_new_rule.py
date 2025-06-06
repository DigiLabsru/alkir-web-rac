from ....common.interface.ras.ras import RasInterface
from ....common.schemas.request import NewAssigmentRuleInfo


def create_new_rule(req: NewAssigmentRuleInfo):
    try:
        rac = RasInterface(req=req)
        rac_data = rac.java_get_assignment_rules(server_id=req.server_id)
        for one_data in rac_data:
            if one_data.getAssignmentRuleId().toString() == req.rule_id:
                return {
                    "error": 0,
                    "message": f"Требование назначения с ID {req.rule_id} в кластере {req.cluster_id} уже существует",
                    "data": ""
                }
        new_object = rac.java_reg_resource_assignment_rule(property=req)
        rac_data = rac.java_get_assignment_rules(server_id=req.server_id)
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
            "message": f"При проверке в списке существующих требований назначения создаваемое требование с ID {req.rule_id} не найдено",
            "data": ""
        }
        for one_data in rac_data:
            if one_data.getAssignmentRuleId().toString() == req.rule_id:
                result: dict = {
                    "error": 0,
                    "message": f"Новое требование назначения с ID {req.rule_id} создан успешно",
                    "data": {"new_object": new_object}
                }
    except Exception as ex:
        return {
            "error": 1,
            "message": f"Произошла ошибка при обработке данных. Текст ошибки: {ex}",
            "data": {}
        }
    return result
