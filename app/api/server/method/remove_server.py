from ....common.interface.ras.ras import RasInterface
from ....common.schemas.request import WorkingServerInfo


def remove_server(req: WorkingServerInfo):
    try:
        rac = RasInterface(req=req)
        server_list = rac.java_get_working_servers()
        server_find_flag: bool = False
        for one_server in server_list:
            if one_server.getClusterId().toString() == req.cluster_id and one_server.getWorkingServerId().toString() == req.server_id:
                server_find_flag = True
        if server_find_flag is False:
            return {
                "error": 0,
                "message": f"Рабочий сервер с ID {req.server_id} в кластере {req.cluster_id} не найден",
                "data": ""
            }
        rac.java_unreg_cluster(server_id=req.server_id)
        server_list = rac.java_get_working_servers()
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
            "message": f"Кластер с ID {req.cluster_id} в кластере {req.cluster_id} удален успешно",
            "data": ""
        }
        for one_server in server_list:
            if one_server.getClusterId().toString() == req.cluster_id and one_server.getWorkingServerId().toString() == req.server_id:
                result: dict = {
                    "error": 1,
                    "message": f"При проверке в списке существующих рабочих серверов найден удаляемый сервер и ID {req.server_id} в кластере {req.cluster_id}",
                    "data": ""
                }
    except Exception as ex:
        return {
            "error": 1,
            "message": f"Произошла ошибка при обработке данных. Текст ошибки: {ex}",
            "data": ""
        }
    return result
