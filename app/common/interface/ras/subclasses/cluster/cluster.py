import jpype

from .....schemas.request import NewAdmin, NewCluster


class Cluster():
    def java_unreg_cluster_admin(self, remove_admin_name):
        return self.connection.unregClusterAdmin(self.cluster_id, remove_admin_name)

    def java_get_clusters(self):
        return self.connection.getClusters()

    def java_get_cluster_managers(self):
        self.authenticate()
        return self.connection.getClusterManagers(self.cluster_id)

    def java_get_cluster_manager_info(self, cluster_manager_id: str):
        self.authenticate()
        return self.connection.getClusterManagerInfo(self.cluster_id, jpype.JClass("java.util.UUID").fromString(cluster_manager_id))

    def java_get_cluster_service_all(self):
        self.authenticate()
        return self.connection.getClusterServices(self.cluster_id)

    def java_get_cluster_info(self):
        return self.connection.getClusterInfo(self.cluster_id)

    def java_get_cluster_admins(self):
        self.authenticate()
        return self.connection.getClusterAdmins(self.cluster_id)

    def java_reg_cluster_admin(self, agent_admin_property: NewAdmin):
        RegUserInfo = jpype.JClass("com._1c.v8.ibis.admin.RegUserInfo")
        new_user_info = RegUserInfo(
            agent_admin_property.new_admin_name,
            agent_admin_property.new_admin_descr,
            agent_admin_property.new_admin_password,
            agent_admin_property.new_admin_password_auth_allowed,
            agent_admin_property.new_admin_sys_auth_allowed,
            agent_admin_property.new_admin_sys_user_name
        )
        return self.connection.regClusterAdmin(self.cluster_id, new_user_info)

    def java_reg_cluster(self, cluster_property: NewCluster):
        RegClusterInfo = jpype.JClass("com._1c.v8.ibis.admin.ClusterInfo")
        new_cluster_info = RegClusterInfo()
        new_cluster_info.setExpirationTimeout(cluster_property.expiration_timeout)
        new_cluster_info.setHostName(cluster_property.host_name)
        new_cluster_info.setLifeTimeLimit(cluster_property.life_time_limit)
        new_cluster_info.setMainPort(cluster_property.main_port)
        new_cluster_info.setMaxMemorySize(cluster_property.max_memory_size)
        new_cluster_info.setMaxMemoryTimeLimit(cluster_property.max_memory_time_limit)
        new_cluster_info.setName(cluster_property.name)
        new_cluster_info.setSecurityLevel(cluster_property.security_level)
        new_cluster_info.setSessionFaultToleranceLevel(cluster_property.session_fault_tolerance_level)
        new_cluster_info.setLoadBalancingMode(cluster_property.load_balancing_mode)
        new_cluster_info.setClusterRecyclingErrorsCountThreshold(cluster_property.cluster_recycling_errors_count_threshold)
        new_cluster_info.setClusterRecyclingKillProblemProcesses(cluster_property.cluster_recycling_kill_problem_processes)
        new_cluster_info.setClusterRecyclingKillByMemoryWithDump(cluster_property.cluster_recycling_kill_by_memory_with_dump)
        return self.connection.regCluster(new_cluster_info)

    def java_update_cluster(self, cluster_property: NewCluster):
        new_cluster_info = self.connection.getClusterInfo(self.cluster_id)
        new_cluster_info.setExpirationTimeout(cluster_property.expiration_timeout)
        new_cluster_info.setHostName(cluster_property.host_name)
        new_cluster_info.setLifeTimeLimit(cluster_property.life_time_limit)
        new_cluster_info.setMainPort(cluster_property.main_port)
        new_cluster_info.setMaxMemorySize(cluster_property.max_memory_size)
        new_cluster_info.setMaxMemoryTimeLimit(cluster_property.max_memory_time_limit)
        new_cluster_info.setName(cluster_property.name)
        new_cluster_info.setSecurityLevel(cluster_property.security_level)
        new_cluster_info.setSessionFaultToleranceLevel(cluster_property.session_fault_tolerance_level)
        new_cluster_info.setLoadBalancingMode(cluster_property.load_balancing_mode)
        new_cluster_info.setClusterRecyclingErrorsCountThreshold(cluster_property.cluster_recycling_errors_count_threshold)
        new_cluster_info.setClusterRecyclingKillProblemProcesses(cluster_property.cluster_recycling_kill_problem_processes)
        new_cluster_info.setClusterRecyclingKillByMemoryWithDump(cluster_property.cluster_recycling_kill_by_memory_with_dump)
        return self.connection.regCluster(new_cluster_info)

    def java_unreg_cluster(self):
        self.authenticate()
        return self.connection.unregCluster(self.cluster_id)
