from ....common.interface.ras.ras import RasInterface
from ....common.schemas.request import BaseRequest


def get_service_list(req: BaseRequest):
    try:
        rac = RasInterface(req=req)
        rac_data = rac.java_get_cluster_service_all()
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
            cluster_manager_ids = []
            java_cluster_manager_ids = one_data.getClusterManagerIds()
            for i in range(0, java_cluster_manager_ids.size()):
                cluster_manager_ids.append(java_cluster_manager_ids[i].toString())
            result.append(
                {
                    "cluster_manager_ids": cluster_manager_ids,
                    "description": one_data.getDescr(),
                    "main_only": one_data.getMainOnly(),
                    "name": one_data.getName()
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
