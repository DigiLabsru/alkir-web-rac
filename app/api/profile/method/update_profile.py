from ....common.interface.ras.ras import RasInterface
from ....common.schemas.request import NewSecurityProfile


def update_profile(req: NewSecurityProfile):
    try:
        rac = RasInterface(req=req)
        rac_data = rac.java_get_security_profiles()
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
        rac.java_update_security_profile(property=req)
        rac.close()
    except Exception as ex:
        return {
            "error": 1,
            "message": f"Произошла ошибка при получении данных из RAS. Текст ошибки: {ex}",
            "data": []
        }
    return {
        "error": 0,
        "message": f"Профиль безопасности с именем {req.sp_name} в кластере {req.cluster_id} обновлен успешно",
        "data": ""
    }
