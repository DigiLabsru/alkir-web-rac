from ....common.interface.ras.ras import RasInterface
from ....common.schemas.request import BaseRequest


def get_cluster_info(req: BaseRequest):
    try:
        rac = RasInterface(req=req)
        cluster_info = rac.java_get_cluster_info()
        platform_version = rac.java_get_agent_version()
        rac.close()
    except Exception as ex:
        return {
            "error": 1,
            "message": f"Произошла ошибка при получении данных из RAS. Текст ошибки: {ex}",
            "data": []
        }
    try:
        result: dict = {
            "cluster_id": cluster_info.getClusterId().toString(),
            "expiration_timeout": cluster_info.getExpirationTimeout(),
            "host_name": cluster_info.getHostName(),
            "life_time_limit": cluster_info.getLifeTimeLimit(),
            "main_port": cluster_info.getMainPort(),
            "max_memory_size": cluster_info.getMaxMemorySize(),
            "max_memory_time_limit": cluster_info.getMaxMemoryTimeLimit(),
            "name": cluster_info.getName(),
            "security_level": cluster_info.getSecurityLevel(),
            "session_fault_tolerance_level": cluster_info.getSessionFaultToleranceLevel(),
            "load_balancing_mode": cluster_info.getLoadBalancingMode(),
            "cluster_recycling_errors_count_threshold": cluster_info.getClusterRecyclingErrorsCountThreshold(),
            "cluster_recycling_kill_by_memory_with_dump": cluster_info.isClusterRecyclingKillByMemoryWithDump(),
            "cluster_recycling_kill_problem_processes": cluster_info.isClusterRecyclingKillProblemProcesses(),
            "platform_version": platform_version
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
