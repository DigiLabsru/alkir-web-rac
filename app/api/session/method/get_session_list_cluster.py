import jpype

from ....common.interface.ras.ras import RasInterface
from ....common.schemas.request import SessionClusterList
from .prometheus_metrics import labels_list, metrics_list


def get_session_list_cluster(req: SessionClusterList, prometheus: bool = False):
    try:
        rac = RasInterface(req=req)
        session_all = rac.java_get_sessions()
        rac.close()
    except Exception as ex:
        return {
            "error": 1,
            "message": f"Произошла ошибка при получении данных из RAS. Текст ошибки: {ex}",
            "data": ""
        }
    try:
        result: list = []
        SimpleDateFormat = jpype.JClass('java.text.SimpleDateFormat')
        sdf = SimpleDateFormat("yyyy-MM-dd HH:mm:ss")
        for one_session in session_all:
            license_list: dict = {}
            if one_session.getLicenses().size() > 0 and req.with_license is True:
                license_list["lic_full_name"] = one_session.getLicenses().get(0).getFullName()
                license_list["lic_full_presentation"] = one_session.getLicenses().get(0).getFullPresentation()
                license_list["lic_issued_by_server"] = one_session.getLicenses().get(0).isIssuedByServer()
                license_list["lic_license_type"] = one_session.getLicenses().get(0).getLicenseType()
                license_list["lic_max_users_all"] = one_session.getLicenses().get(0).getMaxUsersAll()
                license_list["lic_max_users_cur"] = one_session.getLicenses().get(0).getMaxUsersCur()
                license_list["lic_net"] = one_session.getLicenses().get(0).isNet()
                license_list["lic_rmngr_address"] = one_session.getLicenses().get(0).getRmngrAddress()
                license_list["lic_rmngr_pid"] = one_session.getLicenses().get(0).getRmngrPid()
                license_list["lic_rmngr_port"] = one_session.getLicenses().get(0).getRmngrPort()
                license_list["lic_series"] = one_session.getLicenses().get(0).getSeries()
                license_list["lic_short_presentation"] = one_session.getLicenses().get(0).getShortPresentation()

            result_data: dict = {
                "app_id": one_session.getAppId(),
                "blocked_by_dbms": one_session.getBlockedByDbms(),
                "blocked_by_ls": one_session.getBlockedByLs(),
                "bytes_all": one_session.getBytesAll(),
                "bytes_last_5_min": one_session.getBytesLast5Min(),
                "calls_all": one_session.getCallsAll(),
                "calls_last_5_min": one_session.getCallsLast5Min(),
                "client_ip_address": one_session.getClientIPAddress(),
                "connection_id": one_session.getConnectionId().toString(),
                "cpu_time_all": one_session.getCpuTimeAll(),
                "cpu_time_current": one_session.getCpuTimeCurrent(),
                "cpu_time_last_5_min": one_session.getCpuTimeLast5Min(),
                "current_service_name": one_session.getCurrentServiceName(),
                "data_separation": one_session.getDataSeparation(),
                "db_proc_info": one_session.getDbProcInfo(),
                "db_proc_took": one_session.getDbProcTook(),
                "db_proc_took_at": sdf.format(one_session.getDbProcTookAt()),
                "dbms_bytes_all": one_session.getDbmsBytesAll(),
                "dbms_bytes_last_5_min": one_session.getDbmsBytesLast5Min(),
                "duration_all": one_session.getDurationAll(),
                "duration_all_dbms": one_session.getDurationAllDbms(),
                "duration_all_service": one_session.getDurationAllService(),
                "duration_current": one_session.getDurationCurrent(),
                "duration_current_dbms": one_session.getDurationCurrentDbms(),
                "duration_current_service": one_session.getDurationCurrentService(),
                "duration_last_5_min": one_session.getDurationLast5Min(),
                "duration_last_5_min_dbms": one_session.getDurationLast5MinDbms(),
                "duration_last_5_min_service": one_session.getDurationLast5MinService(),
                "hibernate": one_session.getHibernate(),
                "hibernate_session_termination_time": one_session.getHibernateSessionTerminationTime(),
                "host": one_session.getHost(),
                "infobase_id": one_session.getInfoBaseId().toString(),
                "last_active_at": sdf.format(one_session.getLastActiveAt()),
                "locale": one_session.getLocale(),
                "memory_current": one_session.getMemoryCurrent(),
                "memory_last_5_min": one_session.getMemoryLast5Min(),
                "memory_total": one_session.getMemoryTotal(),
                "passive_session_hibernate_time": one_session.getPassiveSessionHibernateTime(),
                "read_bytes_current": one_session.getReadBytesCurrent(),
                "read_bytes_last_5_min": one_session.getReadBytesLast5Min(),
                "read_bytes_total": one_session.getReadBytesTotal(),
                "session_id": one_session.getSessionId(),
                "sid": one_session.getSid().toString(),
                "started_at": sdf.format(one_session.getStartedAt()),
                "user_name": one_session.getUserName(),
                "working_process_id": one_session.getWorkingProcessId().toString(),
                "write_bytes_current": one_session.getWriteBytesCurrent(),
                "write_bytes_last_5_min": one_session.getWriteBytesLast5Min(),
                "write_bytes_total": one_session.getWriteBytesTotal()
            } | license_list
            if prometheus is True:
                metrics_string: list = []
                labels_string: str = ", ".join([f'{label}="{result_data.get(label, None)}"' for label in labels_list])
                for metric in metrics_list:
                    metrics_string.append(
                        f'{metric.lower()}{{{labels_string}}} {result_data[metric]}'
                    )
                result.append("\n".join(metrics_string))
            else:
                result.append(result_data)
        if prometheus is False:
            return {
                "error": 0,
                "message": "",
                "data": result
            }
        else:
            return "\n".join(result)
    except Exception as ex:
        return {
            "error": 1,
            "message": f"Произошла ошибка при обработке данных. Текст ошибки: {ex}",
            "data": []
        }
