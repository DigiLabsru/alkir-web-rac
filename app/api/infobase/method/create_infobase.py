from ....common.interface.ras.ras import RasInterface
from ....common.schemas.request import InfobaseProperty


def create_infobase(req: InfobaseProperty):
    try:
        missing_property: list = []
        if req.dbms_type is None:
            missing_property.append('тип базы данных в СУБД (dbms_type)')
        if req.db_name is None:
            missing_property.append('имя базы данных в СУБД (db_name)')
        if req.db_user is None:
            missing_property.append('логин в СУБД (db_user)')
        if req.db_password is None:
            missing_property.append('пароль в СУБД (db_password)')
        if req.db_server_name is None:
            missing_property.append('адрес сервера СУБД (db_server_name)')
        if req.name is None:
            missing_property.append('имя информационной базы (name)')
        if len(missing_property) != 0:
            return {
                "error": 1,
                "message": f"Пропущены обязательные параметры для создания информационной базы: {', '.join(missing_property)}",
                "data": ""
            }
        rac = RasInterface(req=req)
        new_infobase_id = rac.java_create_infobase(new_infabase=req)
        rac.close()
        return {
            "error": 0,
            "message": "Обновление информации для информационной базы прошло успешно",
            "data": new_infobase_id.toString()
        }
    except Exception as ex:
        return {
            "error": 1,
            "message": f"Произошла ошибка при получении данных из RAS. Текст ошибки: {ex}",
            "data": ""
        }
