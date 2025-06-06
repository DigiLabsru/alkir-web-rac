from ....common.interface.ras.ras import RasInterface
from ....common.schemas.request import NewWorkingServer


def update_server(req: NewWorkingServer):
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
        rac.java_update_working_server(property=req)
        rac.close()
    except Exception as ex:
        return {
            "error": 1,
            "message": f"Произошла ошибка при получении данных из RAS. Текст ошибки: {ex}",
            "data": []
        }
    return {
        "error": 0,
        "message": f"Данные рабочего сервера {req.name} c ID {req.server_id} в кластере {req.cluster_id} обновлены успешно",
        "data": ""
    }
