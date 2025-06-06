from ....common.interface.ras.ras import RasInterface
from ....common.schemas.request import NewCluster


def update_cluster(req: NewCluster):
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
        rac.java_update_cluster(cluster_property=req)
        rac.close()
    except Exception as ex:
        return {
            "error": 1,
            "message": f"Произошла ошибка при получении данных из RAS. Текст ошибки: {ex}",
            "data": []
        }
    return {
        "error": 0,
        "message": f"Данные кластера {req.name} c ID {req.cluster_id} обновлены успешно",
        "data": ""
    }
