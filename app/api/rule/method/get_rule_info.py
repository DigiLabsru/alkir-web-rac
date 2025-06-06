from ....common.interface.ras.ras import RasInterface
from ....common.schemas.request import AssigmentRuleInfo


def get_rule_info(req: AssigmentRuleInfo):
    try:
        rac = RasInterface(req=req)
        rac_data = rac.java_get_assignment_rule_info(server_id=req.server_id, rule_id=req.rule_id)
        rac.close()
    except Exception as ex:
        return {
            "error": 1,
            "message": f"Произошла ошибка при получении данных из RAS. Текст ошибки: {ex}",
            "data": []
        }
    try:
        result: dict = {
            "application_ext": rac_data.getApplicationExt(),
            "assignment_rule_id": rac_data.getAssignmentRuleId().toString(),
            "infobase_name": rac_data.getInfoBaseName(),
            "object_type": rac_data.getObjectType(),
            "priority": rac_data.getPriority(),
            "rule_type": rac_data.getRuleType()
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
