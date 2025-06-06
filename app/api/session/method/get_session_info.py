import jpype

from ....common.interface.ras.ras import RasInterface
from ....common.schemas.request import SessionInfo
from .prometheus_metrics import labels_list, metrics_list


def get_session_info(req: SessionInfo, prometheus: bool = False):
    try:
        rac = RasInterface(req=req)
        session_info = rac.java_get_session_info(sid=req.session_id)
        rac.close()
    except Exception as ex:
        return {
            "error": 1,
            "message": f"Произошла ошибка при получении данных из RAS. Текст ошибки: {ex}",
            "data": ""
        }
    try:
        SimpleDateFormat = jpype.JClass('java.text.SimpleDateFormat')
        sdf = SimpleDateFormat("yyyy-MM-dd HH:mm:ss")
        license_list: dict = {}
        if session_info.getLicenses().size() > 0 and req.with_license is True:
            license_list["lic_full_name"] = session_info.getLicenses().get(0).getFullName()
            license_list["lic_full_presentation"] = session_info.getLicenses().get(0).getFullPresentation()
            license_list["lic_issued_by_server"] = session_info.getLicenses().get(0).isIssuedByServer()
            license_list["lic_license_type"] = session_info.getLicenses().get(0).getLicenseType()
            license_list["lic_max_users_all"] = session_info.getLicenses().get(0).getMaxUsersAll()
            license_list["lic_max_users_cur"] = session_info.getLicenses().get(0).getMaxUsersCur()
            license_list["lic_net"] = session_info.getLicenses().get(0).isNet()
            license_list["lic_rmngr_address"] = session_info.getLicenses().get(0).getRmngrAddress()
            license_list["lic_rmngr_pid"] = session_info.getLicenses().get(0).getRmngrPid()
            license_list["lic_rmngr_port"] = session_info.getLicenses().get(0).getRmngrPort()
            license_list["lic_series"] = session_info.getLicenses().get(0).getSeries()
            license_list["lic_short_presentation"] = session_info.getLicenses().get(0).getShortPresentation()

        result_data: dict = {
            "app_id": session_info.getAppId(),
            "blocked_by_dbms": session_info.getBlockedByDbms(),
            "blocked_by_ls": session_info.getBlockedByLs(),
            "bytes_all": session_info.getBytesAll(),
            "bytes_last_5_min": session_info.getBytesLast5Min(),
            "calls_all": session_info.getCallsAll(),
            "calls_last_5_min": session_info.getCallsLast5Min(),
            "client_ip_address": session_info.getClientIPAddress(),
            "connection_id": session_info.getConnectionId().toString(),
            "cpu_time_all": session_info.getCpuTimeAll(),
            "cpu_time_current": session_info.getCpuTimeCurrent(),
            "cpu_time_last_5_min": session_info.getCpuTimeLast5Min(),
            "current_service_name": session_info.getCurrentServiceName(),
            "data_separation": session_info.getDataSeparation(),
            "db_proc_info": session_info.getDbProcInfo(),
            "db_proc_took": session_info.getDbProcTook(),
            "db_proc_took_at": sdf.format(session_info.getDbProcTookAt()),
            "dbms_bytes_all": session_info.getDbmsBytesAll(),
            "dbms_bytes_last_5_min": session_info.getDbmsBytesLast5Min(),
            "duration_all": session_info.getDurationAll(),
            "duration_all_dbms": session_info.getDurationAllDbms(),
            "duration_all_service": session_info.getDurationAllService(),
            "duration_current": session_info.getDurationCurrent(),
            "duration_current_dbms": session_info.getDurationCurrentDbms(),
            "duration_current_service": session_info.getDurationCurrentService(),
            "duration_last_5_min": session_info.getDurationLast5Min(),
            "duration_last_5_min_dbms": session_info.getDurationLast5MinDbms(),
            "duration_last_5_min_service": session_info.getDurationLast5MinService(),
            "hibernate": session_info.getHibernate(),
            "hibernate_session_termination_time": session_info.getHibernateSessionTerminationTime(),
            "host": session_info.getHost(),
            "infobase_id": session_info.getInfoBaseId().toString(),
            "last_active_at": sdf.format(session_info.getLastActiveAt()),
            "locale": session_info.getLocale(),
            "memory_current": session_info.getMemoryCurrent(),
            "memory_last_5_min": session_info.getMemoryLast5Min(),
            "memory_total": session_info.getMemoryTotal(),
            "passive_session_hibernate_time": session_info.getPassiveSessionHibernateTime(),
            "read_bytes_current": session_info.getReadBytesCurrent(),
            "read_bytes_last_5_min": session_info.getReadBytesLast5Min(),
            "read_bytes_total": session_info.getReadBytesTotal(),
            "session_id": session_info.getSessionId(),
            "sid": session_info.getSid().toString(),
            "started_at": sdf.format(session_info.getStartedAt()),
            "user_name": session_info.getUserName(),
            "working_process_id": session_info.getWorkingProcessId().toString(),
            "write_bytes_current": session_info.getWriteBytesCurrent(),
            "write_bytes_last_5_min": session_info.getWriteBytesLast5Min(),
            "write_bytes_total": session_info.getWriteBytesTotal(),
            "licenses": license_list
        }
        if prometheus is True:
            metrics_string: list = []
            labels_string: str = ", ".join([f'{label}="{result_data.get(label, None)}"' for label in labels_list])
            for metric in metrics_list:
                metrics_string.append(
                    f'{metric.lower()}{{{labels_string}}} {result_data[metric]}'
                )
        if prometheus is False:
            return {
                "error": 0,
                "message": "",
                "data": result_data
            }
        else:
            return "\n".join(metrics_string)
    except Exception as ex:
        return {
            "error": 1,
            "message": f"Произошла ошибка при обработке данных. Текст ошибки: {ex}",
            "data": []
        }
