import jpype

from ....schemas.request import NewAdmin
from .assignment.assignment import Assignment
from .cluster.cluster import Cluster
from .connection.connection import Connection
from .infobase.infobase import Infobase
from .resource_consumption.resource_consumption import ResourceConsumption
from .resource_consumption_counter.resource_consumption_counter import (
    ResourceConsumptionCounter,
)
from .security_profile.security_profile import SecurityProfile
from .sessions.sessions import Sessions
from .working_processes.working_processes import WorkingProcesses
from .working_server.working_server import WorkingServer


class Rac(Cluster, Assignment, ResourceConsumptionCounter, Connection, Infobase, SecurityProfile, WorkingServer, ResourceConsumption, WorkingProcesses, Sessions):
    def connect(self):
        if jpype.isJVMStarted() is True:
            try:
                self.connection = self.connector.connect(self.ras_server, self.ras_port)
            except Exception as ex:
                raise Exception(f"Ошибка про соединении с кластером. Текст ошибки библиотеки: {ex}")
            try:
                self.connection.authenticateAgent(self.central_admin, self.central_pwd)
            except Exception as ex:
                raise Exception(f"Ошибка при аутентификации в агенте кластера. Текст ошибки библиотеки: {ex}")
            clusters = self.connection.getClusters()
            if self.its_get_clusters is False:
                if self.cluster_id is None:
                    match clusters.size():
                        case 1:
                            self.cluster_id = clusters[0].getClusterId()
                        case s if s > 1:
                            raise Exception("На этом сервере зарегистрировано несколько кластеров, поэтому невозможно однозначно автоматически задать ID. \
Задавайте его через параметр cluster_id в запросе.")
                        case 0:
                            raise Exception("На этом сервере не зарегистрировано ни одного кластера.")
                else:
                    self.cluster_id = jpype.JClass("java.util.UUID").fromString(self.cluster_id)
                if self.cluster_name is None:
                    self.cluster_name = self.java_get_cluster_info().getName()
        else:
            raise Exception("Не обнаружено запущенной виртуальной машины java")

    def authenticate_info_base(self):
        self.connection.addAuthentication(self.cluster_id, self.ib_admin, self.ib_pwb)

    def authenticate(self):
        self.connection.authenticate(self.cluster_id, self.cluster_admin, self.cluster_pwd)

    def shutdown(self):
        self.connector.shutdown()

    def java_get_agent_admins(self):
        return self.connection.getAgentAdmins()

    def java_get_agent_version(self):
        return self.connection.getAgentVersion()

    def set_ib_id(self):
        if self.ib_id is None and self.ib_name is None:
            raise Exception("ID информационной базы (ib_id) и имя информационной базы (ib_name) не заданы. Надо задать любой из этих параметров.")
        if self.ib_id is not None:
            self.ib_id = jpype.JClass("java.util.UUID").fromString(self.ib_id)
        else:
            for one_base in self.java_get_info_bases():
                if one_base.getName() == self.ib_name:
                    self.ib_id = one_base.getInfoBaseId()
            if self.ib_id is None:
                raise Exception(f"Не удалось найти в кластере информационной базы {self.ib_name}")

    def java_get_locks(self):
        self.authenticate()
        return self.connection.getLocks(self.cluster_id)

    def java_unreg_agent_admin(self, remove_admin_name):
        return self.connection.unregAgentAdmin(remove_admin_name)

    def java_reg_agent_admin(self, agent_admin_property: NewAdmin):
        RegUserInfo = jpype.JClass("com._1c.v8.ibis.admin.RegUserInfo")
        new_user_info = RegUserInfo(
            agent_admin_property.new_admin_name,
            agent_admin_property.new_admin_descr,
            agent_admin_property.new_admin_password,
            agent_admin_property.new_admin_password_auth_allowed,
            agent_admin_property.new_admin_sys_auth_allowed,
            agent_admin_property.new_admin_sys_user_name
        )
        return self.connection.regAgentAdmin(new_user_info)

    def java_interrupt_current_server_call(self, sid: str, message: str):
        self.authenticate()
        return self.connection.interruptCurrentServerCall(self.cluster_id, jpype.JClass("java.util.UUID").fromString(sid), message)
