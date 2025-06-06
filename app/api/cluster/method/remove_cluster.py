from ....common.interface.ras.ras import RasInterface
from ....common.schemas.request import BaseRequest


def remove_cluster(req: BaseRequest):
    try:
        rac = RasInterface(req=req)
        cluster_list = rac.java_get_clusters()
        cluster_find_flag: bool = False
        for one_cluster in cluster_list:
            if one_cluster.getClusterId().toString() == req.cluster_id:
                cluster_find_flag = True
        if cluster_find_flag is False:
            return {
                "error": 0,
                "message": f"Кластера с ID {req.cluster_id} не найден",
                "data": ""
            }
        rac.java_unreg_cluster()
        cluster_list = rac.java_get_clusters()
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
            "message": f"Кластер с ID {req.cluster_id} удален успешно",
            "data": ""
        }
        for one_cluster in cluster_list:
            if one_cluster.getClusterId().toString() == req.cluster_id:
                result: dict = {
                    "error": 1,
                    "message": f"При проверке в списке существующих кластеров найден удаляемый кластер и ID {req.cluster_id}",
                    "data": ""
                }
    except Exception as ex:
        return {
            "error": 1,
            "message": f"Произошла ошибка при обработке данных. Текст ошибки: {ex}",
            "data": ""
        }
    return result
