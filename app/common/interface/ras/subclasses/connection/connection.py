import jpype


class Connection():
    def java_get_connection_info_short(self, connection_id: str):
        self.authenticate()
        # self.authenticate_info_base()
        return self.connection.getConnectionInfoShort(self.cluster_id, jpype.JClass("java.util.UUID").fromString(connection_id))

    def java_get_connection_locks(self):
        self.authenticate()
        return self.connection.getConnectionLocks(self.cluster_id, self.connection_id)

    def java_get_connections_short(self):
        self.authenticate()
        return self.connection.getConnectionsShort(self.cluster_id)

    def diconnect_connection(self, process_id: str, connection_id: str):
        self.authenticate()
        self.authenticate_info_base()
        self.connection.disconnect(self.cluster_id, jpype.JClass("java.util.UUID").fromString(process_id), jpype.JClass("java.util.UUID").fromString(connection_id))
