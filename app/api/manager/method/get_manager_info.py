from ....common.interface.ras.ras import RasInterface
from ....common.schemas.request import ClusterManagerInfo


def get_manager_info(req: ClusterManagerInfo):
    try:
        rac = RasInterface(req=req)
        rac_data = rac.java_get_cluster_manager_info(cluster_manager_id=req.manager_id)
        rac.close()
    except Exception as ex:
        return {
            "error": 1,
            "message": f"Произошла ошибка при получении данных из RAS. Текст ошибки: {ex}",
            "data": []
        }
    try:
        result: dict = {
            "manager_id": rac_data.getClusterManagerId().toString(),
            "description": rac_data.getDescr(),
            "host_name": rac_data.getHostName(),
            "main_manager": rac_data.getMainManager(),
            "main_port": rac_data.getMainPort(),
            "pid": rac_data.getPid()
        }
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
