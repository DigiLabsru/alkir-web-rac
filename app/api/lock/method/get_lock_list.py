import jpype

from ....common.interface.ras.ras import RasInterface
from ....common.schemas.request import BaseRequest


def get_lock_list(req: BaseRequest):
    try:
        rac = RasInterface(req=req)
        SimpleDateFormat = jpype.JClass('java.text.SimpleDateFormat')
        sdf = SimpleDateFormat("yyyy-MM-dd HH:mm:ss")
        rac_data = rac.java_get_locks()
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
                    "connection_id": one_data.getConnectionId().toString(),
                    "lock_descr": one_data.getLockDescr(),
                    "locked_at": sdf.format(one_data.getLockedAt()),
                    "object": one_data.getObject().toString(),
                    "sid": one_data.getSid().toString()
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
