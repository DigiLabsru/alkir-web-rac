from ....common.interface.ras.ras import RasInterface
from ....common.schemas.request import NewAssigmentRuleInfo


def update_rule(req: NewAssigmentRuleInfo):
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
        rac.java_update_resource_assignment_rule(property=req)
        rac.close()
    except Exception as ex:
        return {
            "error": 1,
            "message": f"Произошла ошибка при получении данных из RAS. Текст ошибки: {ex}",
            "data": []
        }
    return {
        "error": 0,
        "message": f"Данные требования назначения c ID {req.rule_id} в кластере {req.cluster_id} обновлены успешно",
        "data": ""
    }
