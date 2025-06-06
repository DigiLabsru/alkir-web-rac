import jpype

from .....schemas.request import NewWorkingServer


class WorkingServer():
    def java_get_working_servers(self):
        self.authenticate()
        return self.connection.getWorkingServers(self.cluster_id)

    def java_get_working_server_info(self, server_id: str):
        self.authenticate()
        return self.connection.getWorkingServerInfo(self.cluster_id, jpype.JClass("java.util.UUID").fromString(server_id))

    def java_reg_working_server(self, property: NewWorkingServer):
        self.authenticate()
        RegWorkingServerInfoInfo = jpype.JClass("com._1c.v8.ibis.admin.WorkingServerInfo")
        # port_ranges_list = []
        port_ranges_list_java = jpype.JClass("java.util.List")
        for one_port in property.port_ranges:
            PortRangeInfo = jpype.JClass("com._1c.v8.ibis.admin.PortRangeInfo")
            port_range = PortRangeInfo(one_port.high_bound, one_port.low_bound)
            # port_ranges_list.append(port_range)
            port_ranges_list_java.add(port_range)

        new_object = RegWorkingServerInfoInfo(jpype.JClass("java.util.UUID").fromString(property.server_id), property.name, property.cluster_main_port)
        new_object.setConnectionsPerWorkingProcessLimit(property.connections_per_working_process_limit)
        new_object.setCriticalProcessesTotalMemory(property.critical_processes_total_memory)
        new_object.setDedicatedManagers(property.is_dedicated_managers)
        new_object.setHostName(property.host_name)
        new_object.setInfoBasesPerWorkingProcessLimit(property.infobases_per_working_process_limit)
        new_object.setMainPort(property.main_port)
        new_object.setMainServer(property.is_main_server)
        new_object.setPortRanges(port_ranges_list_java)
        new_object.setSafeCallMemoryLimit(property.safe_call_memory_limit)
        new_object.setSafeWorkingProcessesMemoryLimit(property.safe_working_processes_memory_limit)
        new_object.setTemporaryAllowedProcessesTotalMemory(property.temporary_allowed_processes_total_memory)
        new_object.setTemporaryAllowedProcessesTotalMemoryTimeLimit(property.temporary_allowed_processes_total_memory_time_limit)
        new_object.setWorkingProcessMemoryLimit(property.working_process_memory_limit)
        return self.connection.regWorkingServer(self.cluster_id, new_object)

    def java_update_working_server(self, property: NewWorkingServer):
        self.authenticate()
        # port_ranges_list = []
        port_ranges_list_java = jpype.JClass("java.util.List")
        for one_port in property.port_ranges:
            PortRangeInfo = jpype.JClass("com._1c.v8.ibis.admin.PortRangeInfo")
            port_range = PortRangeInfo(one_port.high_bound, one_port.low_bound)
            # port_ranges_list.append(port_range)
            port_ranges_list_java.add(port_range)

        new_object = self.connection.getWorkingServerInfo(self.cluster_id, jpype.JClass("java.util.UUID").fromString(property.server_id))
        new_object.setConnectionsPerWorkingProcessLimit(property.connections_per_working_process_limit)
        new_object.setCriticalProcessesTotalMemory(property.critical_processes_total_memory)
        new_object.setDedicatedManagers(property.is_dedicated_managers)
        new_object.setHostName(property.host_name)
        new_object.setInfoBasesPerWorkingProcessLimit(property.infobases_per_working_process_limit)
        new_object.setMainPort(property.main_port)
        new_object.setMainServer(property.is_main_server)
        new_object.setPortRanges(port_ranges_list_java)
        new_object.setSafeCallMemoryLimit(property.safe_call_memory_limit)
        new_object.setSafeWorkingProcessesMemoryLimit(property.safe_working_processes_memory_limit)
        new_object.setTemporaryAllowedProcessesTotalMemory(property.temporary_allowed_processes_total_memory)
        new_object.setTemporaryAllowedProcessesTotalMemoryTimeLimit(property.temporary_allowed_processes_total_memory_time_limit)
        new_object.setWorkingProcessMemoryLimit(property.working_process_memory_limit)
        return self.connection.regWorkingServer(self.cluster_id, new_object)

    def java_unreg_working_server(self, server_id: str):
        self.authenticate()
        return self.connection.unregWorkingServer(self.cluster_id, jpype.JClass("java.util.UUID").fromString(server_id))
