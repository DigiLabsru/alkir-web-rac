import jpype

from .....schemas.request import NewAssigmentRuleInfo


class Assignment():
    def java_apply_assignment_rules(self, full: int):
        self.authenticate()
        return self.connection.applyAssignmentRules(self.cluster_id, full)

    def java_get_assignment_rule_info(self, server_id: str, rule_id: str):
        self.authenticate()
        return self.connection.getAssignmentRuleInfo(self.cluster_id, jpype.JClass("java.util.UUID").fromString(server_id), jpype.JClass("java.util.UUID").fromString(rule_id))

    def java_get_assignment_rules(self, server_id: str):
        self.authenticate()
        return self.connection.getAssignmentRules(self.cluster_id, jpype.JClass("java.util.UUID").fromString(server_id))

    def java_reg_resource_assignment_rule(self, property: NewAssigmentRuleInfo):
        self.authenticate()
        AssignmentRuleInfo = jpype.JClass("com._1c.v8.ibis.admin.AssignmentRuleInfo")
        new_object = AssignmentRuleInfo(jpype.JClass("java.util.UUID").fromString(property.rule_id))
        new_object.setApplicationExt(property.application_ext)
        new_object.setInfoBaseName(property.infobase_name)
        new_object.setObjectType(property.object_type)
        new_object.setPriority(property.priority)
        new_object.setRuleType(property.rule_type)
        return self.connection.regAssignmentRule(self.cluster_id, jpype.JClass("java.util.UUID").fromString(property.server_id), new_object, property.position)

    def java_update_resource_assignment_rule(self, property: NewAssigmentRuleInfo):
        self.authenticate()
        new_object = self.connection.getAssignmentRuleInfo(self.cluster_id, jpype.JClass("java.util.UUID").fromString(property.server_id), jpype.JClass("java.util.UUID").fromString(property.rule_id))
        new_object.setApplicationExt(property.application_ext)
        new_object.setInfoBaseName(property.infobase_name)
        new_object.setObjectType(property.object_type)
        new_object.setPriority(property.priority)
        new_object.setRuleType(property.rule_type)
        return self.connection.regAssignmentRule(self.cluster_id, jpype.JClass("java.util.UUID").fromString(property.server_id), new_object, property.position)

    def java_unreg_assignment_rule(self, server_id: str, rule_id: str):
        self.authenticate()
        return self.connection.unregAssignmentRule(self.cluster_id, jpype.JClass("java.util.UUID").fromString(server_id), jpype.JClass("java.util.UUID").fromString(rule_id))
