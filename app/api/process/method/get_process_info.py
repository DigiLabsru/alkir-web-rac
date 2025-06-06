import jpype

from ....common.interface.ras.ras import RasInterface
from ....common.schemas.request import WorkingProcessInfo


def get_process_info(req: WorkingProcessInfo):
    try:
        rac = RasInterface(req=req)
        SimpleDateFormat = jpype.JClass('java.text.SimpleDateFormat')
        sdf = SimpleDateFormat("yyyy-MM-dd HH:mm:ss")
        rac_data = rac.java_get_working_process_info(process_id=req.process_id)
        rac.close()
    except Exception as ex:
        return {
            "error": 1,
            "message": f"Произошла ошибка при получении данных из RAS. Текст ошибки: {ex}",
            "data": []
        }
    try:
        licenses = []
        java_licenses = rac_data.getLicense()
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
        result: dict = {
            "available_perfomance": rac_data.getAvailablePerfomance(),
            "avg_back_call_time": rac_data.getAvgBackCallTime(),
            "avg_call_time": rac_data.getAvgCallTime(),
            "avg_db_call_time": rac_data.getAvgDBCallTime(),
            "avg_lock_call_time": rac_data.getAvgLockCallTime(),
            "avg_server_call_time": rac_data.getAvgServerCallTime(),
            "avg_threads": rac_data.getAvgThreads(),
            "capacity": rac_data.getCapacity(),
            "connections": rac_data.getConnections(),
            "host_name": rac_data.getHostName(),
            "licenses": licenses,
            "main_port": rac_data.getMainPort(),
            "memory_excess_time": rac_data.getMemoryExcessTime(),
            "memory_size": rac_data.getMemorySize(),
            "pid": rac_data.getPid(),
            "running": rac_data.getRunning(),
            "selection_size": rac_data.getSelectionSize(),
            "started_at": sdf.format(rac_data.getStartedAt()),
            "use": rac_data.getUse(),
            "working_process_id": rac_data.getWorkingProcessId().toString(),
            "is_enable": rac_data.isEnable(),
            "is_reserve": rac_data.isReserve()
        }
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
