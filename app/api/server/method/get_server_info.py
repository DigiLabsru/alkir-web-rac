from ....common.interface.ras.ras import RasInterface
from ....common.schemas.request import WorkingServerInfo


def get_server_info(req: WorkingServerInfo):
    try:
        rac = RasInterface(req=req)
        rac_data = rac.java_get_working_server_info(server_id=req.server_id)
        rac.close()
    except Exception as ex:
        return {
            "error": 1,
            "message": f"Произошла ошибка при получении данных из RAS. Текст ошибки: {ex}",
            "data": []
        }
    try:
        port_ranges = []
        java_port_ranges = rac_data.getPortRanges()
        for i in range(0, java_port_ranges.size()):
            port_ranges.append({
                "hight_bound": java_port_ranges[i].getHighBound(),
                "low_bound": java_port_ranges[i].getLowBound()
            })
        result: dict = {
            "cluster_main_port": rac_data.getClusterMainPort(),
            "connections_per_working_process_limit": rac_data.getConnectionsPerWorkingProcessLimit(),
            "critical_processes_total_memory": rac_data.getCriticalProcessesTotalMemory(),
            "host_name": rac_data.getHostName(),
            "infobases_per_working_process_limit": rac_data.getInfoBasesPerWorkingProcessLimit(),
            "main_port": rac_data.getMainPort(),
            "name": rac_data.getName(),
            "port_ranges": port_ranges,
            "safe_call_memory_limit": rac_data.getSafeCallMemoryLimit(),
            "safe_working_processes_memory_limit": rac_data.getSafeWorkingProcessesMemoryLimit(),
            "temporary_allowed_processes_total_memory": rac_data.getTemporaryAllowedProcessesTotalMemory(),
            "temporary_allowed_processes_total_memory_time_limit": rac_data.getTemporaryAllowedProcessesTotalMemoryTimeLimit(),
            "working_process_memory_limit": rac_data.getWorkingProcessMemoryLimit(),
            "working_server_id": rac_data.getWorkingServerId().toString(),
            "is_dedicated_managers": rac_data.isDedicatedManagers(),
            "is_main_server": rac_data.isMainServer()
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
