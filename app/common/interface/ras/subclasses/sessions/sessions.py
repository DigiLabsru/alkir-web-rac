import jpype


class Sessions():
    def java_terminate_session(self, sid: str, message: str):
        self.authenticate()
        return self.connection.terminateSession(self.cluster_id, jpype.JClass("java.util.UUID").fromString(sid), message)

    def java_get_sessions(self):
        self.authenticate()
        return self.connection.getSessions(self.cluster_id)

    def java_get_session_info(self, sid):
        self.authenticate()
        if isinstance(sid, str):
            sid = jpype.JClass("java.util.UUID").fromString(sid)
        return self.connection.getSessionInfo(self.cluster_id, sid)

    def java_get_session_locks(self):
        return self.connection.getSessionLocks(self.cluster_id)
