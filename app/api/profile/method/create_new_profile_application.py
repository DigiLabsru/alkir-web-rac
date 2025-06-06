from ....common.interface.ras.ras import RasInterface
from ....common.schemas.request import NewSecurityProfileApplication


def create_new_profile_application(req: NewSecurityProfileApplication):
    try:
        rac = RasInterface(req=req)
        rac_data = rac.java_get_security_profile_applications(sp_name=req.sp_name)
        for one_data in rac_data:
            if one_data.getSPName() == req.sp_name:
                return {
                    "error": 0,
                    "message": f"Профиль безопасности с именем {req.sp_name} в кластере {req.cluster_id} уже существует",
                    "data": ""
                }
        new_object = rac.java_create_security_profile_application(property=req)
        rac_data = rac.java_get_security_profile_applications(sp_name=req.sp_name)
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
            "message": f"При проверке в списке существующих профилей безопасности создаваемый профиль с именем {req.sp_name} не найден",
            "data": ""
        }
        for one_data in rac_data:
            if one_data.getSPName() == req.sp_name:
                result: dict = {
                    "error": 0,
                    "message": f"Новый профиль безопасности с именем {req.sp_name} создан успешно",
                    "data": {"new_object": new_object}
                }
    except Exception as ex:
        return {
            "error": 1,
            "message": f"Произошла ошибка при обработке данных. Текст ошибки: {ex}",
            "data": {}
        }
    return result
