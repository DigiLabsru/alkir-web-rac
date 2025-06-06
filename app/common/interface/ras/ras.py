import os
import signal
import socket

import jpype
from loguru import logger

from ....common.schemas.request import BaseRequest, InfoBase
from .subclasses.rac import Rac


class RasInterface(Rac):
    def __init__(self, req: BaseRequest | InfoBase, prometheus: bool = False, its_get_clusters: bool = False):
        from ....main import app
        self.ras_server: str = req.ras_server
        self.ras_port: int = req.ras_port
        self.cluster_admin: str = req.cluster_admin
        self.cluster_pwd: str = req.cluster_pwd
        self.central_admin: str = req.central_admin
        self.central_pwd: str = req.central_pwd
        self.timeout: str = req.timeout
        self.cluster_name: str = req.cluster_name
        self.cluster_id: str = req.cluster_id
        if isinstance(req, InfoBase):
            self.ib_admin: str = req.ib_admin
            self.ib_pwb: str = req.ib_pwb
            self.ib_id: str = req.ib_id
            self.ib_name: str = req.ib_name
        self.prometheus: bool = prometheus
        self.its_get_clusters = its_get_clusters
        try:
            with socket.create_connection((self.ras_server, self.ras_port), timeout=3):
                pass
        except (socket.timeout, ConnectionRefusedError, OSError):
            raise Exception(f"Не удалось установить сетевое соединение с {self.ras_server}:{self.ras_port}. Причины - сервер выключен, на указанном порту не запущена служба RAS, \
не открыт порт на целевом сервере в firewall, нет маршрута до целевого сервера.")
        try:
            OutOfMemoryError = jpype.JClass("java.lang.OutOfMemoryError")
            if req.debug is False:
                app.state.java_logger.setLevel(jpype.JClass("java.util.logging.Level").OFF)
            else:
                app.state.java_logger.setLevel(jpype.JClass("java.util.logging.Level").ALL)
            self.factory = app.state.AgentAdminConnectorFactory()
            self.connector = self.factory.createConnector(self.timeout)
            self.connect()
        except OutOfMemoryError as ex:
            logger.critical(f"Ошибка OutOfMemoryError, перезапускаем приложение. Текст ошибки: {ex}")
            os.kill(os.getpid(), signal.SIGHUP)
        except Exception as ex:
            logger.critical(f"Ошибка при инициализации клиента RAC. Сервер - {self.ras_server}, порт - {self.ras_port}. Текст ошибки: {ex}")
            self.connector.shutdown()
            raise

    def close(self):
        if self.connector is not None:
            try:
                self.connector.shutdown()
            except Exception:
                pass
            finally:
                self.connector = None
