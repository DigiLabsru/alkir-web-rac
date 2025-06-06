from ....common.interface.ras.ras import RasInterface
from ....common.schemas.request import BaseRequest


def get_manager_list(req: BaseRequest):
    try:
        rac = RasInterface(req=req)
        rac_data = rac.java_get_cluster_managers()
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
                    "manager_id": one_data.getClusterManagerId().toString(),
                    "description": one_data.getDescr(),
                    "host_name": one_data.getHostName(),
                    "main_manager": one_data.getMainManager(),
                    "main_port": one_data.getMainPort(),
                    "pid": one_data.getPid()
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
