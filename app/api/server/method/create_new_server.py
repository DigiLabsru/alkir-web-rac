from ....common.interface.ras.ras import RasInterface
from ....common.schemas.request import NewWorkingServer


def create_new_server(req: NewWorkingServer):
    try:
        rac = RasInterface(req=req)
        server_list = rac.java_get_working_servers()
        for one_server in server_list:
            if one_server.getName() == req.name:
                return {
                    "error": 0,
                    "message": f"Рабочий сервер с именем {req.name} в кластере {req.cluster_id} уже существует",
                    "data": ""
                }
        new_server_id = rac.java_reg_working_server(property=req)
        server_list = rac.java_get_working_servers()
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
            "message": f"При проверке в списке существующих рабочих серверов создаваемый сервер с именем {req.name} и ID {new_server_id} не найден",
            "data": ""
        }
        for one_server in server_list:
            if one_server.getWorkingServerId().toString() == req.server_id:
                result: dict = {
                    "error": 0,
                    "message": f"Новый рабочий сервер с именем {req.name} и ID {new_server_id} создан успешно",
                    "data": {"new_server_id": new_server_id.toString()}
                }
    except Exception as ex:
        return {
            "error": 1,
            "message": f"Произошла ошибка при обработке данных. Текст ошибки: {ex}",
            "data": {}
        }
    return result
