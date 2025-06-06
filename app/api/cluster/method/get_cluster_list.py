from ....common.interface.ras.ras import RasInterface
from ....common.schemas.request import BaseRequest


def get_cluster_list(req: BaseRequest):
    try:
        rac = RasInterface(req=req, its_get_clusters=True)
        cluster_info = rac.java_get_clusters()
        platform_version = rac.java_get_agent_version()
        rac.close()
    except Exception as ex:
        return {
            "error": 1,
            "message": f"Произошла ошибка при получении данных из RAS. Текст ошибки: {ex}",
            "data": []
        }
    try:
        result: list = []
        for one_cluster in cluster_info:
            result.append(
                {
                    "cluster_id": one_cluster.getClusterId().toString(),
                    "expiration_timeout": one_cluster.getExpirationTimeout(),
                    "host_name": one_cluster.getHostName(),
                    "life_time_limit": one_cluster.getLifeTimeLimit(),
                    "main_port": one_cluster.getMainPort(),
                    "max_memory_size": one_cluster.getMaxMemorySize(),
                    "max_memory_time_limit": one_cluster.getMaxMemoryTimeLimit(),
                    "name": one_cluster.getName(),
                    "security_level": one_cluster.getSecurityLevel(),
                    "session_fault_tolerance_level": one_cluster.getSessionFaultToleranceLevel(),
                    "load_balancing_mode": one_cluster.getLoadBalancingMode(),
                    "cluster_recycling_errors_count_threshold": one_cluster.getClusterRecyclingErrorsCountThreshold(),
                    "cluster_recycling_kill_by_memory_with_dump": one_cluster.isClusterRecyclingKillByMemoryWithDump(),
                    "cluster_recycling_kill_problem_processes": one_cluster.isClusterRecyclingKillProblemProcesses(),
                    "platform_version": platform_version
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
