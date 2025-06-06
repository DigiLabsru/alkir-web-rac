from ....common.interface.ras.ras import RasInterface
from ....common.schemas.request import SecurityProfileDropInfo


def get_profile_internet_resource_list(req: SecurityProfileDropInfo):
    try:
        rac = RasInterface(req=req)
        rac_data = rac.java_get_security_profile_internet_resources(sp_name=req.sp_name)
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
                    "address": one_data.getAddress(),
                    "descr": one_data.getDescr(),
                    "name": one_data.getName(),
                    "port": one_data.getPort(),
                    "protocol": one_data.getProtocol(),
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
