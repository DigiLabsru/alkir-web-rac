import jpype

from ....common.interface.ras.ras import RasInterface
from ....common.schemas.request import ConnectionList


def get_connection_list(req: ConnectionList):
    try:
        rac = RasInterface(req=req)
        rac_data = rac.java_get_infobase_connections(process_id=req.process_id)
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
            SimpleDateFormat = jpype.JClass('java.text.SimpleDateFormat')
            sdf = SimpleDateFormat("yyyy-MM-dd HH:mm:ss")
            result.append(
                {
                    "app_id": one_data.getAppId(),
                    "blocked_by_dbms": one_data.getBlockedByDbms(),
                    "bytes_all": one_data.getBytesAll(),
                    "bytes_last_5min": one_data.getBytesLast5Min(),
                    "calls_all": one_data.getCallsAll(),
                    "calls_last_5min": one_data.getCallsLast5Min(),
                    "connected_at": sdf.format(one_data.getConnectedAt()),
                    "conn_id": one_data.getConnId(),
                    "db_conn_mode": one_data.getDbConnMode(),
                    "dbmsBytes_all": one_data.getDbmsBytesAll(),
                    "dbmsBytes_last_5min": one_data.getDbmsBytesLast5Min(),
                    "dbProc_Info": one_data.getDbProcInfo(),
                    "dbProc_took": one_data.getDbProcTook(),
                    "dbProc_took_at": sdf.format(one_data.getDbProcTookAt()),
                    "duration_all": one_data.getDurationAll(),
                    "duration_all_Dbms": one_data.getDurationAllDbms(),
                    "duration_current": one_data.getDurationCurrent(),
                    "duration_current_Dbms": one_data.getDurationCurrentDbms(),
                    "duration_last_5min": one_data.getDurationLast5Min(),
                    "duration_last_5min_Dbms": one_data.getDurationLast5MinDbms(),
                    "host_name": one_data.getHostName(),
                    "ibConn_mode": one_data.getIbConnMode(),
                    "infoBase_connection_Id": one_data.getInfoBaseConnectionId(),
                    "memory_current": one_data.getMemoryCurrent(),
                    "memory_last_5min": one_data.getMemoryLast5Min(),
                    "memory_total": one_data.getMemoryTotal(),
                    "read_bytes_current": one_data.getReadBytesCurrent(),
                    "read_bytes_last_5min": one_data.getReadBytesLast5Min(),
                    "read_bytes_total": one_data.getReadBytesTotal(),
                    "thread_mode": one_data.getThreadMode(),
                    "user_name": one_data.getUserName(),
                    "write_bytes_current": one_data.getWriteBytesCurrent(),
                    "write_bytes_last_5min": one_data.getWriteBytesLast5Min(),
                    "write_bytes_total": one_data.getWriteBytesTotal()
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
