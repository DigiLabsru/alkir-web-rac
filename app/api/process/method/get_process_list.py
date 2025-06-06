import jpype

from ....common.interface.ras.ras import RasInterface
from ....common.schemas.request import BaseRequest
from .prometheus_metrics import labels_list, metrics_list


def get_process_list(req: BaseRequest, prometheus: bool = False):
    try:
        rac = RasInterface(req=req)
        SimpleDateFormat = jpype.JClass('java.text.SimpleDateFormat')
        sdf = SimpleDateFormat("yyyy-MM-dd HH:mm:ss")
        rac_data = rac.java_get_working_processes()
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
            licenses = []
            java_licenses = one_data.getLicense()
            for i in range(0, java_licenses.size()):
                licenses.append({
                    "lic_full_name": java_licenses[i].getFullName(),
                    "lic_full_presentation": java_licenses[i].getFullPresentation(),
                    "lic_license_type": java_licenses[i].getLicenseType(),
                    "lic_max_users_all": java_licenses[i].getMaxUsersAll(),
                    "lic_max_users_cur": java_licenses[i].getMaxUsersCur(),
                    "lic_rmngr_address": java_licenses[i].getRmngrAddress(),
                    "lic_rmngr_pid": java_licenses[i].getRmngrPid(),
                    "lic_rmngr_port": java_licenses[i].getRmngrPort(),
                    "lic_series": java_licenses[i].getSeries(),
                    "lic_short_presentation": java_licenses[i].getShortPresentation(),
                    "lic_issued_by_server": java_licenses[i].isIssuedByServer(),
                    "lic_net": java_licenses[i].isNet()
                })
            result_data = {
                "available_perfomance": one_data.getAvailablePerfomance(),
                "avg_back_call_time": one_data.getAvgBackCallTime(),
                "avg_call_time": one_data.getAvgCallTime(),
                "avg_db_call_time": one_data.getAvgDBCallTime(),
                "avg_lock_call_time": one_data.getAvgLockCallTime(),
                "avg_server_call_time": one_data.getAvgServerCallTime(),
                "avg_threads": one_data.getAvgThreads(),
                "capacity": one_data.getCapacity(),
                "connections": one_data.getConnections(),
                "host_name": one_data.getHostName(),
                "licenses": licenses,
                "main_port": one_data.getMainPort(),
                "memory_excess_time": one_data.getMemoryExcessTime(),
                "memory_size": one_data.getMemorySize(),
                "pid": one_data.getPid(),
                "running": one_data.getRunning(),
                "selection_size": one_data.getSelectionSize(),
                "started_at": sdf.format(one_data.getStartedAt()),
                "use": one_data.getUse(),
                "working_process_id": one_data.getWorkingProcessId().toString(),
                "is_enable": one_data.isEnable(),
                "is_reserve": one_data.isReserve()
            }
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
            "data": {}
        }
