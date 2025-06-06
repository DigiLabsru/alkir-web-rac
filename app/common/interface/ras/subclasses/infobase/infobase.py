import jpype

from .....schemas.request import InfobaseProperty


class Infobase():
    def java_get_info_bases(self):
        self.authenticate()
        return self.connection.getInfoBases(self.cluster_id)

    def java_get_info_base_info(self, ib_id=None):
        self.authenticate()
        self.authenticate_info_base()
        if ib_id is None:
            self.set_ib_id()
            ib_id = self.ib_id
        return self.connection.getInfoBaseInfo(self.cluster_id, ib_id)

    def java_get_infobase_sessions(self, ib_id=None):
        self.authenticate()
        if ib_id is None:
            self.set_ib_id()
            ib_id = self.ib_id
        if isinstance(ib_id, str):
            ib_id = jpype.JClass("java.util.UUID").fromString(ib_id)
        return self.connection.getInfoBaseSessions(self.cluster_id, ib_id)

    def java_get_infobase_connections(self, process_id: str):
        self.authenticate()
        self.authenticate_info_base()
        self.set_ib_id()
        return self.connection.getInfoBaseConnections(self.cluster_id, jpype.JClass("java.util.UUID").fromString(process_id), self.ib_id)

    def java_get_infobase_connections_short(self, infobase_id: str):
        self.authenticate()
        # self.authenticate_info_base()
        # self.set_ib_id()
        return self.connection.getInfoBaseConnectionsShort(self.cluster_id, jpype.JClass("java.util.UUID").fromString(infobase_id))

    def java_get_infobase_locks(self, base_id: str = None):
        self.authenticate()
        if base_id is not None:
            result_ib_id = jpype.JClass("java.util.UUID").fromString(base_id)
        else:
            result_ib_id = self.ib_id
        return self.connection.getInfoBaseLocks(self.cluster_id, result_ib_id)

    def java_get_infobase_short_info(self):
        self.authenticate()
        self.set_ib_id()
        return self.connection.getInfoBaseShortInfo(self.cluster_id, self.ib_id)

    def java_get_infobases_short(self):
        self.authenticate()
        return self.connection.getInfoBasesShort(self.cluster_id)

    def java_update_infobase_short(self, new_ib_descr: str):
        self.authenticate()
        self.set_ib_id()
        infobase_short_info = self.connection.getInfoBaseShortInfo(self.cluster_id, self.ib_id)
        infobase_short_info.setDescr(new_ib_descr)
        return self.connection.updateInfoBaseShort(self.cluster_id, infobase_short_info)

    def java_create_infobase(self, new_infabase: InfobaseProperty):
        self.authenticate()
        self.authenticate_info_base()
        self.set_ib_id()
        NewInfoBaseInfo = jpype.JClass("com._1c.v8.ibis.admin.InfoBaseInfo")
        new_infobase_info = NewInfoBaseInfo()
        new_infobase_info.setDateOffset(new_infabase.date_offset)
        new_infobase_info.setDbms(new_infabase.dbms_type)
        new_infobase_info.setDbName(new_infabase.db_name)
        new_infobase_info.setDbPassword(new_infabase.db_password)
        new_infobase_info.setDbServerName(new_infabase.db_server_name)
        new_infobase_info.setDbUser(new_infabase.db_user)
        new_infobase_info.setLocale(new_infabase.locale)
        new_infobase_info.setDescr(new_infabase.descr)
        new_infobase_info.setName(new_infabase.name)
        if new_infabase.denied_from is not None:
            new_infobase_info.setDeniedFrom(new_infabase.denied_from)
        if new_infabase.denied_message is not None:
            new_infobase_info.setDeniedMessage(new_infabase.denied_message)
        if new_infabase.denied_parameter is not None:
            new_infobase_info.setDeniedParameter(new_infabase.denied_parameter)
        if new_infabase.denied_to is not None:
            new_infobase_info.setDeniedTo(new_infabase.denied_to)
        if new_infabase.external_session_manager_connection_string is not None:
            new_infobase_info.setExternalSessionManagerConnectionString(new_infabase.external_session_manager_connection_string)
        if new_infabase.external_session_manager_required is not None:
            new_infobase_info.setExternalSessionManagerRequired(new_infabase.external_session_manager_required)
        if new_infabase.license_distribution_allowed is not None:
            new_infobase_info.setLicenseDistributionAllowed(new_infabase.license_distribution_allowed)
        if new_infabase.permission_code is not None:
            new_infobase_info.setPermissionCode(new_infabase.permission_code)
        if new_infabase.reserve_working_processes is not None:
            new_infobase_info.setReserveWorkingProcesses(new_infabase.reserve_working_processes)
        if new_infabase.safe_mode_security_profile_name is not None:
            new_infobase_info.setSafeModeSecurityProfileName(new_infabase.safe_mode_security_profile_name)
        if new_infabase.scheduled_jobs_denied is not None:
            new_infobase_info.setScheduledJobsDenied(new_infabase.scheduled_jobs_denied)
        if new_infabase.security_profile_name is not None:
            new_infobase_info.setSecurityProfileName(new_infabase.security_profile_name)
        if new_infabase.sessions_denied is not None:
            new_infobase_info.setSessionsDenied(new_infabase.sessions_denied)
        return self.connection.createInfoBase(self.cluster_id, new_infobase_info, new_infabase.create_base_flag)

    def java_update_infobase(self, update_infabase_property: InfobaseProperty):
        self.authenticate()
        self.authenticate_info_base()
        self.set_ib_id()
        infobase_property = self.connection.getInfoBaseInfo(self.cluster_id, self.ib_id)
        if update_infabase_property.denied_from is not None:
            update_infabase_property.setDeniedFrom(update_infabase_property.denied_from)
        if update_infabase_property.denied_message is not None:
            infobase_property.setDeniedMessage(update_infabase_property.denied_message)
        if update_infabase_property.denied_parameter is not None:
            infobase_property.setDeniedParameter(update_infabase_property.denied_parameter)
        if update_infabase_property.denied_to is not None:
            infobase_property.setDeniedTo(update_infabase_property.denied_to)
        if update_infabase_property.external_session_manager_connection_string is not None:
            infobase_property.setExternalSessionManagerConnectionString(update_infabase_property.external_session_manager_connection_string)
        if update_infabase_property.external_session_manager_required is not None:
            infobase_property.setExternalSessionManagerRequired(update_infabase_property.external_session_manager_required)
        if update_infabase_property.license_distribution_allowed is not None:
            infobase_property.setLicenseDistributionAllowed(update_infabase_property.license_distribution_allowed)
        if update_infabase_property.permission_code is not None:
            infobase_property.setPermissionCode(update_infabase_property.permission_code)
        if update_infabase_property.reserve_working_processes is not None:
            infobase_property.setReserveWorkingProcesses(update_infabase_property.reserve_working_processes)
        if update_infabase_property.safe_mode_security_profile_name is not None:
            infobase_property.setSafeModeSecurityProfileName(update_infabase_property.safe_mode_security_profile_name)
        if update_infabase_property.scheduled_jobs_denied is not None:
            infobase_property.setScheduledJobsDenied(update_infabase_property.scheduled_jobs_denied)
        if update_infabase_property.security_profile_name is not None:
            infobase_property.setSecurityProfileName(update_infabase_property.security_profile_name)
        if update_infabase_property.sessions_denied is not None:
            infobase_property.setSessionsDenied(update_infabase_property.sessions_denied)
        return self.connection.updateInfoBase(self.cluster_id, infobase_property)

    def java_drop_infobase(self, infobase_creation_mode: int):
        self.authenticate()
        self.authenticate_info_base()
        self.set_ib_id()
        return self.connection.dropInfoBase(self.cluster_id, self.ib_id, infobase_creation_mode)
