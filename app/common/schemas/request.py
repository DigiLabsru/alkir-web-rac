from datetime import datetime
from typing import Literal

from pydantic import BaseModel, Field


class BaseRequest(BaseModel):
    cluster_admin: str = Field(title='Админ кластера', description='Админ кластера', default="", example="super_admin")
    cluster_pwd: str = Field(title='Пароль админа кластера', description='Пароль админа кластера', default="", example="super_secret_password!")
    central_admin: str = Field(title='Админ центрального кластера', description='Админ центрального кластера', default="", example="central_admin")
    central_pwd: str = Field(title='Пароль админа центрального кластера', description='Пароль админа центрального кластера', default="", example="super_secret_password?")
    ras_server: str = Field(title='Адрес RAS', description='Адрес RAS', example="srv-1c-app")
    ras_port: int = Field(title='Порт RAS', description='Порт RAS', default=1545)
    timeout: int = Field(title='Таймаут на коннект к серверу', description='Таймаут на коннект к серверу', default=2000)
    cluster_name: str = Field(title='Имя кластера', description='Имя кластера. Если на сервере один кластер получается автоматически.', default=None, example="Локальный кластер")
    cluster_id: str = Field(title='ID кластера', description='ID кластера. Если на сервере один кластер получается автоматически.', default=None, example="462629aa-39f5-4f37-8b80-697ff2c3ce48")
    debug: bool = Field(title='Отладка запроса', default=False)


class InfoBase(BaseRequest):
    ib_admin: str = Field(title='Логин админа ИБ', description='Логин админа информационной базы', default="")
    ib_pwb: str = Field(title='Пароль админа ИБ', description='Пароль админа информационной базы', default="")
    ib_id: str = Field(title='ID информационной базы', description='ID информационной базы', default=None)
    ib_name: str = Field(title='Имя информационной базы', description='Имя информационной базы', default=None)


class SessionInfobaseList(InfoBase):
    with_license: bool = Field(title='Флаг показа сведения о лицензиях', description='Флаг показа сведения о лицензиях. True - показывать, False - нет.', default=True)


class SessionClusterList(BaseRequest):
    with_license: bool = Field(title='Флаг показа сведения о лицензиях', description='Флаг показа сведения о лицензиях. True - показывать, False - нет.', default=True)


class SessionInfo(BaseRequest):
    session_id: str = Field(title='ID сессии', description='ID сессии для получения подробной информации')
    with_license: bool = Field(title='Флаг показа сведения о лицензиях', description='Флаг показа сведения о лицензиях. True - показывать, False - нет.', default=True)


class TerminateSession(BaseRequest):
    session_id: str = Field(title='ID сессии', description='ID сессии для получения подробной информации')
    message: str = Field(title='ID сессии', description='ID сессии для получения подробной информации')


class InfoBaseSummaryUpdate(InfoBase):
    new_ib_descr: str = Field(title='Новое описание информационной базы', description='Новое описание информационной базы')


class DeleteInfoBase(InfoBase):
    infobase_creation_mode: Literal[0, 1, 2] = Field(title='Режим удаления базы', description='''Новое описание информационной базы:  
 - 0 - не трогать базу данных
 - 1 - при удалении информационной базы удалить базу данных
 - 2 - при удалении информационной базы очистить базу данных''')  # noqa W291


class InfobaseProperty(BaseRequest):
    # обязательные параметры
    dbms_type: Literal['MSSQLServer', 'PostgreSQL'] = Field(title='Тип СУБД', description='''Тип СУБД где будет располагаться информационная база.  
**Важный момент!**  
Если сервер приложений находится на Linux подключение к MSSQL платформой не поддерживается
''', default=None)  # noqa W291
    db_name: str = Field(title='Имя базы СУБД', description='Имя сервера базы данных, в котором хранится информационная база', default=None)
    db_user: str = Field(title='Логин СУБД', description='Имя пользователя сервера базы данных', default=None)
    db_password: str = Field(title='Пароль от СУБД', description='Пароль пользователя сервера базы данных', default=None)
    db_server_name: str = Field(title='Адрес СУБД', description='Имя сервера базы данных, на котором хранится информационная база', default=None)
    name: str = Field(title='Имя информационной базы', description='Имя информационной базы', default=None)

    date_offset: int = Field(title='Смещение даты', description='Устанавливает смещение даты информационной базы', default=0)
    denied_from: datetime = Field(
        title='Начало блокировки', description='Время начала периода блокировки сеанса. Формат даты - yyyy-mm-dd hh:mm:ss',
        example=f'{datetime.now().strftime("%Y-%m-%d %H:%M:%S")}', default=None)
    denied_message: str = Field(title='Сообщение для блокировки', description='Сообщение, которое отображается при попытке подключения к заблокированной базе', default=None)
    denied_parameter: str = Field(title='Значение параметра блокировки сеанса', description='Значение параметра блокировки сеанса', default=None)
    denied_to: datetime = Field(title='Конец блокировки',
                                description='Время конца периода блокировки сеанса. Формат даты - yyyy-mm-dd hh:mm:ss',
                                example=f'{datetime.now().strftime("%Y-%m-%d %H:%M:%S")}', default=None)
    descr: str = Field(title='Описание информационной базы', description='Описание информационной базы', default='')
    external_session_manager_connection_string: str = Field(title='Параметры внешнего менеджера сеансов', description='Параметры внешнего менеджера сеансов', default=None)
    external_session_manager_required: bool = Field(
        title='Флаг обязательности внешнего менеджера соединений',
        description='Флаг, показывающий, является ли использование внешнего менеджера сеансов обязательным', default=None)
    license_distribution_allowed:  Literal[0, 1] = Field(
        title='Раздача лицензий сервером приложения',
        description='Флаг, показывающий, разрешено ли распространение лицензий с сервера 1С:Предприятия', default=None)
    locale: Literal['ru', 'en'] = Field(title='Идентификатор локали информационной базы', description='Идентификатор локали информационной базы', default='ru')
    permission_code: str = Field(title='Код доступа к заблокированной базе', description='Код, позволяющий открывать сеансы в период блокировки информационной базы.', default=None)
    reserve_working_processes: bool = Field(
        title='Рабочий процесс под информационную базу',
        description='Флаг, который показывает, должен ли сервер создавать отдельные рабочие процессы для информационной базы', default=False)
    safe_mode_security_profile_name: str = Field(
        title='Имя профиля безопасности для базы для безопасного режима',
        description='Имя профиля безопасности информационной базы для безопасного режима', default=None)
    scheduled_jobs_denied: bool = Field(title='Блокировка фоновых заданий', description='''Флаг, показывающий, запрещено ли выполнение плановых заданий информационной базы:
 - false - старт фоновых заданий разрешен
 - true - старт фоновых заданий запрещен
''', default=False)
    security_profile_name: str = Field(title='Имя профиля безопасности информационной базы', description='Имя профиля безопасности информационной базы', default=None)
    sessions_denied: bool = Field(title='Блокировка информационной базы', description='''Флаг отвечающий за блокировку информационной базы:
 - false - доступ в информационную базу разрешен
 - true - доступ в информационную базу запрещен
''', default=False)
    create_base_flag: Literal[0, 1] = Field(title='Флаг создания базы', description='''Флаг создания базы в СУБД для информационной базы:
 - 0 - не создавать базу в СУБД
 - 1 - создать базу в СУБД
''', default=1)


class UpdateInfobaseProperty(InfoBase, InfobaseProperty):
    pass


class Temp(BaseRequest):
    cluster_manager_id: str = Field(title='ID менеджера', description='ID менеджера кластера', default=None)
    process_id: str = Field(title='ID процесса', description='ID менеджера кластера', default=None)


class ConnectionInfo(BaseRequest):
    connection_id: str = Field(title='ID соединения', description='ID соединения')


class ConnectionInfoDis(BaseRequest):
    connection_id: str = Field(title='ID соединения', description='ID соединения')
    process_id: str = Field(title='ID рабочего процесса', description='Идентификатор рабочего процесса сервера')


class ConnectionList(InfoBase):
    process_id: str = Field(title='ID рабочего процесса', description='Идентификатор рабочего процесса сервера')


class ConnectionIBList(InfoBase):
    infobase_id: str = Field(title='ID информационной базы', description='Идентификатор информационной базы')


class ConnectionDisconnect(BaseRequest):
    process_id: str = Field(title='ID рабочего процесса', description='Идентификатор рабочего процесса сервера')
    connection_id: str = Field(title='ID соединения', description='ID соединения')
    ib_admin: str = Field(title='Пароль админа кластера', description='Пароль админа кластера', default="")
    ib_pwb: str = Field(title='Пароль админа кластера', description='Пароль админа кластера', default="")


class NewAdmin(BaseRequest):
    new_admin_descr: str = Field(title='Описание', description="Устанавливает описание центрального администратора сервера или администратора кластера серверов")
    new_admin_name: str = Field(title='Имя', description="Устанавливает имя центрального администратора сервера или администратора кластера серверов. В случае локальной \
авторизации это является логинов.")
    new_admin_password: str = Field(title='Пароль', description="Устанавливает пароль администратора. Используется только при локальной авторизации.")
    new_admin_password_auth_allowed: bool = Field(title='Признак локальной аутентификации',
                                                        description="Устанавливает флаг, показывающий, разрешена ли аутентификация по паролю для администратора.")
    new_admin_sys_auth_allowed: bool = Field(title='Признак доменной аутентификации',
                                                   description="Устанавливает флаг, показывающий, разрешена ли аутентификация операционной системы для администратора.")
    new_admin_sys_user_name: str = Field(
        title='Доменное имя', description=r"Устанавливает имя пользователя операционной системы администратора кластера серверов. Должно быть в формате domain\login")


class RemoveAdmin(BaseRequest):
    remove_admin_name: str = Field(title='Имя', description="Имя удаляемого центрального администратора сервера.")


class NewCluster(BaseRequest):
    cluster_recycling_errors_count_threshold: int = Field(
        title='Допустимое отклонение количества',
        description='''Устанавливает допустимое отклонение для количества ошибок сервера на запрос в минуту на основе среднего значения для всех процессов.
Например, если значение параметра установлено на «50», а среднее количество ошибок на один запрос в минуту за последние 5 минут составляет «100»,
то пороговое значение считается превышенным для процессов, которые вызвали более 150 ошибок на запрос в минуту.''')
    cluster_recycling_kill_by_memory_with_dump: bool = Field(title='Обязательный дамп', description='Принудительно создает дамп памяти процессов, которые завершаются за превышение лимита памяти.')
    cluster_recycling_kill_problem_processes: bool = Field(title='Принудительно завершает процессы с ошибками.', description='''Принудительно завершает процессы с ошибками.
Если установлено значение true, то процессы, признанные по результатам мониторинга процессами по умолчанию, будут принудительно завершены.
Возможные причины, по которым процесс может быть признан процессом по умолчанию:
 - превышено значение допустимое отклонение для количества ошибок сервера на запрос в минуту на основе среднего значения для всех процессов (cluster_recycling_errors_count_threshold)
 - превышен объем памяти, используемой процессором
 - зависание процесса (перестает отвечать на запросы)
 - процесс не был завершен в течение определенного времени после исключения из кластера.''')
    expiration_timeout: int = Field(title='Таймаут', description='Устанавливает тайм-аут истечения срока действия')
    host_name: str = Field(title='Имя хоста главного кластера', description='Устанавливает имя или IP-адрес компьютера, на котором расположены регистр кластера и главный процесс менеджера кластера.')
    life_time_limit: int = Field(title='Время жизни', description='Устанавливает ограничение по времени жизни рабочих процессов кластера')
    load_balancing_mode: int = Field(title='Режим балансировки нагрузки', description='''Устанавливает режим балансировки нагрузки.
0 - приоритеты определяются доступной производительностью
1 - приоритеты определяются доступной памятью
Значение по умолчанию: 0
''', default=0)
    main_port: int = Field(title='Основной порт', description='Устанавливает основной номер IP-порта менеджера кластера')
    max_memory_size: int = Field(title='Лимит памяти на рабочий процесс', description='Устанавливает лимит (в КБ) виртуального адресного пространства на рабочий процесс')
    max_memory_time_limit: int = Field(title='Лимит времени на превышение лимита памяти', description='Получает максимально допустимый период (в секундах) превышения лимита размера памяти')
    name: str = Field(title='Имя кластера', description='Имя кластера')
    security_level: int = Field(title='Уровень безопасности соединения', description='Устанавливает уровень безопасности соединения')
    session_fault_tolerance_level: int = Field(title='Уровень отказоустойчивости сеанса', description='Устанавливает уровень отказоустойчивости сеанса')


class ClusterManagerInfo(BaseRequest):
    manager_id: str = Field(title='ID менеджера', description='ID менеджера для получения подробной информации')


class WorkingProcessInfo(BaseRequest):
    process_id: str = Field(title='ID процесса', description='ID процесса для получения подробной информации')


class WorkingServerInfo(BaseRequest):
    server_id: str = Field(title='ID сервера', description='ID сервера для получения подробной информации')


class NewAssigmentRuleInfo(BaseRequest):
    server_id: str = Field(title='ID сервера', description='ID сервера для получения подробной информации')
    rule_id: str = Field(title='ID правила', description='ID правила для получения подробной информации')
    position: int = Field(title='Позиция', description='position in the rule list (starts from 0)')
    application_ext: str = Field(title='application with additional criteria for applying the rule', description='')
    infobase_name: str = Field(title='the name of the infobase where the rule is used', description='')
    object_type: str = Field(title='assignment object ID', description='')
    priority: int = Field(title='assignment rule priority', description='')
    rule_type: int = Field(title='assignment rule 0 - do not distribute to this server 1 - same as no rule 2 - distribute to this server', description='')


class ApplyAssignmentRules(BaseRequest):
    full: int = Field(title='assigment rule application mode', description='''assigment rule application mode:
        0 - partial
        1 - full''')


class AssigmentRuleInfo(BaseRequest):
    server_id: str = Field(title='ID сервера', description='ID сервера для получения подробной информации')
    rule_id: str = Field(title='ID правила', description='ID правила для получения подробной информации')


class PortRanges(BaseModel):
    low_bound: int = Field(title='the lower bound of the port range', description='')
    high_bound: int = Field(title='the upper bound of the port range', description='')


class NewWorkingServer(BaseRequest):
    server_id: str = Field(title='ID сервера', description='Устанавливает ID сервера')
    cluster_main_port: int = Field(title='Основной порт кластера', description='Устанавливает основной номер IP-порта менеджера кластера')
    connections_per_working_process_limit: int = Field(title='the maximum number of connections per process', description='')
    critical_processes_total_memory: int = Field(title='the critical memory size of all working processes and cluster managers on work server', description='')
    host_name: str = Field(title='Имя хоста главного кластера', description='Устанавливает имя или IP-адрес компьютера, на котором расположены регистр кластера и главный процесс менеджера кластера.')
    infobases_per_working_process_limit: int = Field(title='the maximum allowed number of infobases per process', description='')
    main_port: int = Field(title='Основной порт', description='Устанавливает основной номер IP-порта менеджера кластера')
    name: str = Field(title='Имя кластера', description='Имя кластера')
    port_ranges: list[PortRanges] = Field(title='Диапазон портов', description='Диапазон портов')
    safe_call_memory_limit: int = Field(title='the safe memory size limit per call (in bytes)', description="", default=0)
    safe_working_processes_memory_limit: int = Field(title='the safe memory size limit per working process on a server', description="", default=0)
    temporary_allowed_processes_total_memory: int = Field(title='the temporary allowed memory size of working processes and cluster managers on work server', description='', default=0)
    temporary_allowed_processes_total_memory_time_limit: int = Field(
        title='the maximum time for working processes and cluster managers to excess temporary allowed memory size', description="", default=0)
    working_process_memory_limit: int = Field(title='the maximum memory size available to processes', description="", default=0)
    working_server_id: str = Field(title='the working server ID', description='')
    is_dedicated_managers: bool = Field(title='the flag that shows whether dedicated managers are used for each service', description='')
    is_main_server: bool = Field(title=' the flag that shows whether the server is central', description='')


class ResourceConsumptionLimitInfo(BaseRequest):
    limit_name: str = Field(title='Имя ограничения', description='Наименование лимита ограничений ресурсов')


class NewResourceConsumptionLimit(BaseRequest):
    action: int = Field(title='action type', description='')
    active_session_count: int = Field(title='limit value of active session count', description='')
    calls: int = Field(title='limit value of call count', description='')
    counter: str = Field(title='counter name', description='')
    cpu_time: int = Field(title='limit value of the CPU time server calls', description='')
    dbms_bytes: int = Field(title='limit value of data transmission DBMS', description='')
    description: str = Field(title='resource limit description', description='')
    duration: int = Field(title='limit value of the server calls duration', description='')
    duration_dbms: int = Field(title='limit value of the duration DBMS calls', description='')
    duration_service: int = Field(title='limit value of service call duration', description='')
    memory: int = Field(title='limit value of the session memory usage', description='')
    message: str = Field(title='error message text for users', description='')
    name: str = Field(title='Имя ограничения', description='Наименование лимита ограничений ресурсов')
    read_bytes: int = Field(title='limit value of the session disk read operations', description='')
    session_count: int = Field(title='limit value of session count', description='')
    write_bytes: int = Field(title='limit value of the session disk write operations', description='')


class ResourceConsumptionCounterInfo(BaseRequest):
    counter_name: str = Field(title='Имя счетчика', description='Наименование счетчика ограничений ресурсов')


class ResourceConsumptionCounterValueInfo(BaseRequest):
    counter_name: str = Field(title='Имя счетчика', description='Наименование счетчика ограничений ресурсов')
    object_name: str = Field(title='Объект', description='Наименование объекта')


class NewResourceConsumptionCounter(BaseRequest):
    collection_time: int = Field(title='counter collection time (millisecond)', description='')
    description: str = Field(title='count info description', description='')
    filter_type: int = Field(title='counter type of filter', description='')
    filter_value: str = Field(title='filter value', description='')
    group: int = Field(title='counter grouping type', description='')
    name: str = Field(title='resource counter name', description='')
    is_analyze_active_session_count: bool = Field(title='flag that show to analyze active session count', description='')
    is_analyze_calls: bool = Field(title='flag that show to analyze call count', description='')
    is_analyze_cpu_time: bool = Field(title='flag that show to analyze cpu time', description='')
    is_analyze_dbms_bytes: bool = Field(title='flag that show to analyze DBMS bytes', description='')
    is_analyze_duration: bool = Field(title='flag that show to analyze call duration', description='')
    is_analyze_duration_dbms: bool = Field(title='flag that show to analyze duration call DBMS', description='')
    is_analyze_duration_service: bool = Field(title='flag that show to analyze call service duration', description='')
    is_analyze_memory: bool = Field(title='flag that show to analyze memory', description='')
    is_analyze_read_bytes: bool = Field(title='flag that show to analyze disk read operation', description='')
    is_analyze_session_count: bool = Field(title='flag that show to analyze session count', description='')
    is_analyze_write_bytes: bool = Field(title='flag that show to analyze disk write operation', description='')


class UpdateResourceConsumptionCounter(NewResourceConsumptionCounter):
    counter_name: str = Field(title='Имя счетчика', description='Наименование счетчика ограничений ресурсов')


class NewSecurityProfile(BaseRequest):
    add_in_use_full_access: bool = Field(title='the value of the flag that shows whether using arbitrary add-ins is allowed', description='')
    all_modules_extension: bool = Field(title='the value of the flag that allows extension of all modules', description='')
    com_use_full_access: bool = Field(title='the value of the flag that shows whether using arbitrary COM objects is allowed', description='')
    cryptography_allowed: bool = Field(title='the value of the flag that allows cryptography functionality to work', description='')
    descr: str = Field(title='external component description', description='')
    external_app_full_access: bool = Field(title='the value of the flag that shows whether using arbitrary applications is allowed', description='')
    file_system_full_access: bool = Field(title='the value of the flag that shows whether full access to the file system is allowed', description='')
    full_privileged_mode: bool = Field(title='the value of the flag that shows whether enabling privileged mode in safe mode is allowed', description='')
    internet_use_full_access: bool = Field(title='the value of the flag that shows whether using arbitrary Internet resources is allowed', description='')
    modules_available_for_extension: str = Field(title='list of modules available for extension', description='')
    modules_not_available_for_extension: str = Field(title='list of modules not available for extension', description='')
    privileged_mode_in_safe_mode_allowed: bool = Field(title='the value of the flag that shows whether enabling privileged mode in safe mode is allowed', description='')
    privileged_mode_roles: str = Field(title='list of roles used in privileged mode if full privileged mode is not allowed', description='')
    right_extension: bool = Field(title='the value of the flag that allows every right extension', description='')
    right_extension_definition_roles: str = Field(title='list of extensible rights defining roles', description='')
    safe_mode_profile: bool = Field(title='the value of the flag that shows whether using a script profile in safe mode is allowed', description='')
    sp_name: str = Field(title='Имя профиля безопасности', description='Имя профиля безопасности')
    unsafe_external_module_full_access: bool = Field(title='the value of the flag that shows whether using arbitrary unsafe external modules is allowed', description='')


class SecurityProfileDropInfo(BaseRequest):
    sp_name: str = Field(title='Имя профиля безопасности', description='Имя профиля безопасности')


class SecurityProfileDropInfoExt(BaseRequest):
    sp_name: str = Field(title='Имя профиля безопасности', description='Имя профиля безопасности')
    name: str = Field(title='Имя профиля безопасности', description='Имя профиля безопасности')


class SecurityProfileDropInfoExtVD(BaseRequest):
    sp_name: str = Field(title='Имя профиля безопасности', description='Имя профиля безопасности')
    alias: str = Field(title='Имя профиля безопасности', description='Имя профиля безопасности')


class NewSecurityProfileAddIn(BaseRequest):
    add_in_hash: str = Field(title='add-in hash', description='')
    descr: str = Field(title='add-in description', description='')
    name: str = Field(title='add-in name', description='')
    sp_name: str = Field(title='Имя профиля безопасности', description='Имя профиля безопасности')


class NewSecurityProfileApplication(BaseRequest):
    command_wild: str = Field(title='application command-line format', description='')
    descr: str = Field(title='application description', description='')
    name: str = Field(title='application name', description='')
    sp_name: str = Field(title='Имя профиля безопасности', description='Имя профиля безопасности')


class NewSecurityProfileCOMClass(BaseRequest):
    computer_name: str = Field(title='computer name', description='')
    descr: str = Field(title='COM class description', description='')
    file_name: str = Field(title='the file name (string presentation of the moniker)', description='')
    name: str = Field(title='COM class name', description='')
    object_uuid: str = Field(title='object identifier', description='')
    sp_name: str = Field(title='Имя профиля безопасности', description='Имя профиля безопасности')


class NewSecurityProfileInternetResource(BaseRequest):
    address: str = Field(title='Internet resource address', description='')
    descr: str = Field(title='Internet resource description', description='')
    name: str = Field(title='Internet resource name', description='')
    port: int = Field(title='Internet resource port', description='')
    protocol: str = Field(title='the Internet resource access protocol', description='')
    sp_name: str = Field(title='Имя профиля безопасности', description='Имя профиля безопасности')


class NewSecurityProfileExternalModule(BaseRequest):
    descr: str = Field(title='external module description', description='')
    module_hash: str = Field(title='external module hash', description='')
    name: str = Field(title='external module name', description='')
    sp_name: str = Field(title='Имя профиля безопасности', description='Имя профиля безопасности')


class NewSecurityProfileVirtualDirectory(BaseRequest):
    alias: str = Field(title='the logical URL of a virtual directory', description='')
    allowed_read: str = Field(title='the value of the flag that shows whether reading from the virtual directory is allowed', description='')
    allowed_write: int = Field(title='the value of the flag that shows whether writing to the virtual directory is allowed', description='')
    descr: str = Field(title='virtual directory description', description='')
    physical_path: str = Field(title='the physical URL of a virtual directory', description='')
    sp_name: str = Field(title='Имя профиля безопасности', description='Имя профиля безопасности')
