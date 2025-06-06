from ....common.interface.ras.ras import RasInterface
from ....common.schemas.request import SecurityProfileDropInfo


def get_profile_virtual_directories_list(req: SecurityProfileDropInfo):
    try:
        rac = RasInterface(req=req)
        rac_data = rac.java_get_security_profile_virtual_directories(sp_name=req.sp_name)
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
                    "alias": one_data.getAlias(),
                    "allowed_read": one_data.getAllowedRead(),
                    "allowed_write": one_data.	getAllowedWrite(),
                    "descr": one_data.getDescr(),
                    "physical_path": one_data.getPhysicalPath(),
                    "sp_name": one_data.getSPName()
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
