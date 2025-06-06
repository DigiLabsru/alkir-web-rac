import jpype


class WorkingProcesses():
    def java_get_server_working_processes(self):
        return self.connection.getServerWorkingProcesses(self.cluster_id)

    def java_get_working_processes(self):
        self.authenticate()
        return self.connection.getWorkingProcesses(self.cluster_id)

    def java_get_working_process_info(self, process_id: str):
        self.authenticate()
        return self.connection.getWorkingProcessInfo(self.cluster_id, jpype.JClass("java.util.UUID").fromString(process_id))
