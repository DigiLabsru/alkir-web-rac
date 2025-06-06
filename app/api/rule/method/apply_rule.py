from ....common.interface.ras.ras import RasInterface
from ....common.schemas.request import ApplyAssignmentRules


def apply_rule(req: ApplyAssignmentRules) -> dict:
    try:
        rac = RasInterface(req=req)
        rac.java_apply_assignment_rules(full=req.full)
        rac.close()
    except Exception as ex:
        return {
            "error": 1,
            "message": f"Произошла ошибка при получении данных из RAS. Текст ошибки: {ex}",
            "data": []
        }
    return {
        "error": 0,
        "message": f"Требования назначения с режимом {req.full} обновлены успешно",
        "data": ""
    }
