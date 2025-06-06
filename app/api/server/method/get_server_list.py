from ....common.interface.ras.ras import RasInterface
from ....common.schemas.request import BaseRequest


def get_server_list(req: BaseRequest):
    try:
        rac = RasInterface(req=req)
        rac_data = rac.java_get_working_servers()
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
            port_ranges = []
            java_port_ranges = one_data.getPortRanges()
            for i in range(0, java_port_ranges.size()):
                port_ranges.append({
                    "hight_bound": java_port_ranges[i].getHighBound(),
                    "low_bound": java_port_ranges[i].getLowBound()
                })
            result.append(
                {
                    "cluster_main_port": one_data.getClusterMainPort(),
                    "connections_per_working_process_limit": one_data.getConnectionsPerWorkingProcessLimit(),
                    "critical_processes_total_memory": one_data.getCriticalProcessesTotalMemory(),
                    "host_name": one_data.getHostName(),
                    "infobases_per_working_process_limit": one_data.getInfoBasesPerWorkingProcessLimit(),
                    "main_port": one_data.getMainPort(),
                    "name": one_data.getName(),
                    "port_ranges": port_ranges,
                    "safe_call_memory_limit": one_data.getSafeCallMemoryLimit(),
                    "safe_working_processes_memory_limit": one_data.getSafeWorkingProcessesMemoryLimit(),
                    "temporary_allowed_processes_total_memory": one_data.getTemporaryAllowedProcessesTotalMemory(),
                    "temporary_allowed_processes_total_memory_time_limit": one_data.getTemporaryAllowedProcessesTotalMemoryTimeLimit(),
                    "working_process_memory_limit": one_data.getWorkingProcessMemoryLimit(),
                    "working_server_id": one_data.getWorkingServerId().toString(),
                    "is_dedicated_managers": one_data.isDedicatedManagers(),
                    "is_main_server": one_data.isMainServer()
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
