from ....common.interface.ras.ras import RasInterface
from ....common.schemas.request import NewCluster


def create_new_cluster(req: NewCluster):
    try:
        rac = RasInterface(req=req, its_get_clusters=True)
        cluster_list = rac.java_get_clusters()
        for one_cluster in cluster_list:
            if one_cluster.getName() == req.name and one_cluster.getMainPort() == req.main_port:
                return {
                    "error": 0,
                    "message": f"Кластера с именем {req.name} основным портом {req.main_port} уже существует",
                    "data": ""
                }
        new_cluster_id = rac.java_reg_cluster(cluster_property=req)
        cluster_list = rac.java_get_clusters()
        rac.close()
    except Exception as ex:
        return {
            "error": 1,
            "message": f"Произошла ошибка при получении данных из RAS. Текст ошибки: {ex}",
            "data": {}
        }
    try:
        result: dict = {
            "error": 1,
            "message": f"При проверке в списке существующих кластеров создаваемый кластер с именем {req.name} и ID {new_cluster_id} не найден",
            "data": ""
        }
        for one_cluster in cluster_list:
            if one_cluster.getClusterId() == new_cluster_id:
                result: dict = {
                    "error": 0,
                    "message": f"Новый кластер с именем {req.name} и ID {new_cluster_id} создан успешно",
                    "data": {"cluster_id": new_cluster_id.toString()}
                }
    except Exception as ex:
        return {
            "error": 1,
            "message": f"Произошла ошибка при обработке данных. Текст ошибки: {ex}",
            "data": {}
        }
    return result
