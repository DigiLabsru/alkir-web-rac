from ....common.interface.ras.ras import RasInterface
from ....common.schemas.request import SecurityProfileDropInfoExt


def remove_profile_add_in(req: SecurityProfileDropInfoExt):
    try:
        rac = RasInterface(req=req)
        rac_data = rac.java_get_security_profile_add_ins(sp_name=req.sp_name)
        find_flag: bool = False
        for one_data in rac_data:
            if one_data.getSPName() == req.sp_name:
                find_flag = True
        if find_flag is False:
            return {
                "error": 0,
                "message": f"Профиль безопасности с именем {req.sp_name} в кластере {req.cluster_id} не найден",
                "data": ""
            }
        rac.java_drop_security_profile_add_in(sp_name=req.sp_name, name=req.name)
        rac_data = rac.java_get_security_profile_add_ins(sp_name=req.sp_name)
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
            "message": f"Профиль безопасности с именем {req.sp_name} в кластере {req.cluster_id} удален успешно",
            "data": ""
        }
        for one_data in rac_data:
            if one_data.getSPName() == req.sp_name:
                result: dict = {
                    "error": 1,
                    "message": f"При проверке в списке существующих профилей безопасности найден профиль с именем {req.cluster_id} в кластере {req.cluster_id}",
                    "data": ""
                }
    except Exception as ex:
        return {
            "error": 1,
            "message": f"Произошла ошибка при обработке данных. Текст ошибки: {ex}",
            "data": ""
        }
    return result
