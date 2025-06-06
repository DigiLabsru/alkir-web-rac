import jpype

from .....schemas.request import (
    NewResourceConsumptionCounter,
    UpdateResourceConsumptionCounter,
)


class ResourceConsumptionCounter():
    def java_get_resource_consumption_counter_accumulated_values(self, counter_name: str, object_name: str):
        self.authenticate()
        return self.connection.getResourceConsumptionCounterAccumulatedValues(self.cluster_id, counter_name, object_name)

    def java_get_resource_consumption_counter_info(self, counter_name: str):
        self.authenticate()
        return self.connection.getResourceConsumptionCounterInfo(self.cluster_id, counter_name)

    def java_get_resource_consumption_counters(self):
        self.authenticate()
        return self.connection.getResourceConsumptionCounters(self.cluster_id)

    def java_get_resource_consumption_counter_values(self, counter_name: str, object_name: str):
        self.authenticate()
        return self.connection.getResourceConsumptionCounterValues(self.cluster_id, counter_name, object_name)

    def java_reg_resource_consumption_counter(self, property: NewResourceConsumptionCounter):
        self.authenticate()
        ResourceConsumptionCounter = jpype.JClass("com._1c.v8.ibis.admin.ResourceConsumptionCounter")
        new_object = ResourceConsumptionCounter()
        new_object.setAnalyzeActiveSessionCount(property.is_analyze_active_session_count)
        new_object.setAnalyzeCalls(property.is_analyze_calls)
        new_object.setAnalyzeCpuTime(property.is_analyze_cpu_time)
        new_object.setAnalyzeDbmsBytes(property.is_analyze_dbms_bytes)
        new_object.setAnalyzeDuration(property.is_analyze_duration)
        new_object.setAnalyzeDurationDbms(property.is_analyze_duration_dbms)
        new_object.setAnalyzeDurationService(property.is_analyze_duration_service)
        new_object.setAnalyzeMemory(property.is_analyze_memory)
        new_object.setAnalyzeReadBytes(property.is_analyze_read_bytes)
        new_object.setAnalyzeSessionCount(property.is_analyze_session_count)
        new_object.setAnalyzeWriteBytes(property.is_analyze_write_bytes)
        new_object.setCollectionTime(property.collection_time)
        new_object.setDescription(property.description)
        new_object.setFilterType(property.filter_type)
        new_object.setFilterValue(property.filter_value)
        new_object.setGroup(property.group)
        new_object.setName(property.name)
        return self.connection.regResourceConsumptionCounter(self.cluster_id, new_object)

    def java_update_resource_consumption_counter(self, property: UpdateResourceConsumptionCounter):
        self.authenticate()
        new_object = self.connection.getResourceConsumptionCounterInfo(self.cluster_id, property.counter_name)
        new_object.setAnalyzeActiveSessionCount(property.is_analyze_active_session_count)
        new_object.setAnalyzeCalls(property.is_analyze_calls)
        new_object.setAnalyzeCpuTime(property.is_analyze_cpu_time)
        new_object.setAnalyzeDbmsBytes(property.is_analyze_dbms_bytes)
        new_object.setAnalyzeDuration(property.is_analyze_duration)
        new_object.setAnalyzeDurationDbms(property.is_analyze_duration_dbms)
        new_object.setAnalyzeDurationService(property.is_analyze_duration_service)
        new_object.setAnalyzeMemory(property.is_analyze_memory)
        new_object.setAnalyzeReadBytes(property.is_analyze_read_bytes)
        new_object.setAnalyzeSessionCount(property.is_analyze_session_count)
        new_object.setAnalyzeWriteBytes(property.is_analyze_write_bytes)
        new_object.setCollectionTime(property.collection_time)
        new_object.setDescription(property.description)
        new_object.setFilterType(property.filter_type)
        new_object.setFilterValue(property.filter_value)
        new_object.setGroup(property.group)
        new_object.setName(property.name)
        return self.connection.regResourceConsumptionCounter(self.cluster_id, new_object)

    def java_unreg_resource_consumption_counter(self, counter_name: str):
        self.authenticate()
        return self.connection.unregResourceConsumptionCounter(self.cluster_id, counter_name)

    def java_clear_resource_consumption_counter_accumulated_values(self, counter_name: str, object_name: str):
        self.authenticate()
        return self.connection.clearResourceConsumptionCounterAccumulatedValues(self.cluster_id, counter_name, object_name)
