from ....common.interface.ras.ras import RasInterface
from ....common.schemas.request import AssigmentRuleInfo


def remove_rule(req: AssigmentRuleInfo):
    try:
        rac = RasInterface(req=req)
        rac_data = rac.java_get_assignment_rules(server_id=req.server_id)
        find_flag: bool = False
        for one_data in rac_data:
            if one_data.getAssignmentRuleId().toString() == req.rule_id:
                find_flag = True
        if find_flag is False:
            return {
                "error": 0,
                "message": f"Требование назначения с ID {req.rule_id} в кластере {req.cluster_id} не найден",
                "data": ""
            }
        rac.java_unreg_assignment_rule(server_id=req.server_id, rule_id=req.rule_id)
        rac_data = rac.java_get_assignment_rules(server_id=req.server_id)
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
            "message": f"Требование назначения с ID {req.rule_id} в кластере {req.cluster_id} удален успешно",
            "data": ""
        }
        for one_data in rac_data:
            if one_data.getAssignmentRuleId().toString() == req.rule_id:
                result: dict = {
                    "error": 1,
                    "message": f"При проверке в списке существующих требований назначения найдено требование с ID {req.rule_id} в кластере {req.cluster_id}",
                    "data": ""
                }
    except Exception as ex:
        return {
            "error": 1,
            "message": f"Произошла ошибка при обработке данных. Текст ошибки: {ex}",
            "data": ""
        }
    return result
