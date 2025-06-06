from ....common.interface.ras.ras import RasInterface
from ....common.schemas.request import RemoveAdmin


def remove_agent_admin(req: RemoveAdmin):
    try:
        rac = RasInterface(req=req)
        admins_list = rac.java_get_agent_admins()
        login_find_flsg: bool = False
        for one_admin in admins_list:
            if one_admin.getName() == req.remove_admin_name:
                login_find_flsg = True
        if login_find_flsg is False:
            return {
                "error": 1,
                "message": f"Администратор агента с именем {req.remove_admin_name} в списку существующих не найден",
                "data": ""
            }
        rac.java_unreg_agent_admin(remove_admin_name=req.remove_admin_name)
        admins_list = rac.java_get_agent_admins()
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
            "message": f"Администратор агента {req.remove_admin_name} успешно удален",
            "data": ""
        }
        for one_admin in admins_list:
            if one_admin.getName() == req.remove_admin_name:
                result: dict = {
                    "error": 1,
                    "message": f"При проверке в списке существующих администраторов агента найден удаляемый пользователь {req.remove_admin_name}",
                    "data": ""
                }
        return result
    except Exception as ex:
        return {
            "error": 1,
            "message": f"Произошла ошибка при обработке данных. Текст ошибки: {ex}",
            "data": ""
        }
