import jpype

from .....schemas.request import NewResourceConsumptionLimit


class ResourceConsumption():
    def java_get_resource_consumption_limit_info(self, limit_name: str):
        self.authenticate()
        return self.connection.getResourceConsumptionLimitInfo(self.cluster_id, limit_name)

    def java_get_resource_consumption_limits(self):
        self.authenticate()
        return self.connection.getResourceConsumptionLimits(self.cluster_id)

    def java_reg_resource_consumption_limit(self, property: NewResourceConsumptionLimit):
        self.authenticate()
        ResourceConsumptionLimit = jpype.JClass("com._1c.v8.ibis.admin.ResourceConsumptionLimit")
        new_object = ResourceConsumptionLimit()
        new_object.setAction(property.action)
        new_object.setActiveSessionCount(property.active_session_count)
        new_object.setCalls(property.calls)
        new_object.setCounter(property.counter)
        new_object.setCpuTime(property.cpu_time)
        new_object.setDbmsBytes(property.dbms_bytes)
        new_object.setDescription(property.description)
        new_object.setDuration(property.duration)
        new_object.setDurationDbms(property.duration_dbms)
        new_object.setDurationService(property.duration_service)
        new_object.setMemory(property.memory)
        new_object.setMessage(property.message)
        new_object.setName(property.name)
        new_object.setReadBytes(property.read_bytes)
        new_object.setSessionCount(property.session_count)
        new_object.setWriteBytes(property.write_bytes)
        return self.connection.regResourceConsumptionLimit(self.cluster_id, new_object)

    def java_update_resource_consumption_limit(self, property: NewResourceConsumptionLimit):
        self.authenticate()
        new_object = self.connection.getResourceConsumptionLimitInfo(self.cluster_id, property.name)
        new_object.setAction(property.action)
        new_object.setActiveSessionCount(property.active_session_count)
        new_object.setCalls(property.calls)
        new_object.setCounter(property.counter)
        new_object.setCpuTime(property.cpu_time)
        new_object.setDbmsBytes(property.dbms_bytes)
        new_object.setDescription(property.description)
        new_object.setDuration(property.duration)
        new_object.setDurationDbms(property.duration_dbms)
        new_object.setDurationService(property.duration_service)
        new_object.setMemory(property.memory)
        new_object.setMessage(property.message)
        new_object.setName(property.name)
        new_object.setReadBytes(property.read_bytes)
        new_object.setSessionCount(property.session_count)
        new_object.setWriteBytes(property.write_bytes)
        return self.connection.regResourceConsumptionLimit(self.cluster_id, new_object)

    def java_unreg_resource_consumption_limit(self, limit_name: str):
        self.authenticate()
        return self.connection.unregResourceConsumptionLimit(self.cluster_id, limit_name)
