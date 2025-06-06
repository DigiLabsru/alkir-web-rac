from ....common.interface.ras.ras import RasInterface
from ....common.schemas.request import WorkingServerInfo


def get_rule_list(req: WorkingServerInfo):
    try:
        rac = RasInterface(req=req)
        rac_data = rac.java_get_assignment_rules(server_id=req.server_id)
        rac.close()
    except Exception as ex:
        return {
            "error": 1,
            "message": f"Произошла ошибка при получении данных из RAS. Текст ошибки: {ex}",
            "data": []
        }
    try:
        result: list = []
        for one_data in rac_data:
            result.append(
                {
                    "application_ext": one_data.getApplicationExt(),
                    "assignment_rule_id": one_data.getAssignmentRuleId().toString(),
                    "infobase_name": one_data.getInfoBaseName(),
                    "object_type": one_data.getObjectType(),
                    "priority": one_data.getPriority(),
                    "rule_type": one_data.getRuleType()
                }
            )
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
