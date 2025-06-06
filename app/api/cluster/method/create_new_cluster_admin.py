from ....common.interface.ras.ras import RasInterface
from ....common.schemas.request import NewAdmin


def create_new_cluster_admin(req: NewAdmin):
    try:
        rac = RasInterface(req=req)
        admins_list = rac.java_get_cluster_admins()
        for one_admin in admins_list:
            if one_admin.getName() == req.new_admin_name:
                return {
                    "error": 0,
                    "message": f"Администратор кластера с именем {req.new_admin_name} уже существует",
                    "data": ""
                }
        rac.java_reg_cluster_admin(agent_admin_property=req)
        if rac.cluster_admin == '':
            rac.cluster_admin = req.new_admin_name
            rac.cluster_pwd = req.new_admin_password
        admins_list = rac.java_get_cluster_admins()
        rac.close()
    except Exception as ex:
        return {
            "error": 1,
            "message": f"Произошла ошибка при получении данных из RAS. Текст ошибки: {ex}",
            "data": []
        }
    try:
        result: dict = {
            "error": 1,
            "message": f"При проверке в списке существующих администраторов кластера создаваемый пользователь {req.new_admin_name} не найден",
            "data": ""
        }
        for one_admin in admins_list:
            if one_admin.getName() == req.new_admin_name:
                result: dict = {
                    "error": 0,
                    "message": f"Новый администратор кластера {req.new_admin_name} создан успешно",
                    "data": ""
                }
    except Exception as ex:
        return {
            "error": 1,
            "message": f"Произошла ошибка при обработке данных. Текст ошибки: {ex}",
            "data": []
        }

    return result
