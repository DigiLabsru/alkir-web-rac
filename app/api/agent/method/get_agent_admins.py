from ....common.interface.ras.ras import RasInterface
from ....common.schemas.request import BaseRequest


def get_agent_admins(req: BaseRequest):
    try:
        rac = RasInterface(req=req)
        admins_list = rac.java_get_agent_admins()
        rac.close()
    except Exception as ex:
        return {
            "error": 1,
            "message": f"Произошла ошибка при получении данных из RAS. Текст ошибки: {ex}",
            "data": []
        }
    try:
        result: list = []
        for one_admin in admins_list:
            result.append(
                {
                    "name": one_admin.getName(),
                    "os_user": one_admin.getSysUserName(),
                    "enable_local_auth": one_admin.isPasswordAuthAllowed(),
                    "enable_os_auth": one_admin.isSysAuthAllowed(),
                    "description": one_admin.getDescr(),
                }
            )
    except Exception as ex:
        return {
            "error": 1,
            "message": f"Произошла ошибка при обработке данных. Текст ошибки: {ex}",
            "data": []
        }

    return {
        "error": 0,
        "message": "",
        "data": result
    }
