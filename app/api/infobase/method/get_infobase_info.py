import jpype

from ....common.interface.ras.ras import RasInterface
from ....common.schemas.request import InfoBase


def get_infobase_info(req: InfoBase):
    try:
        rac = RasInterface(req=req)
        infobase_full_info = rac.java_get_info_base_info()
        rac.close()

    except Exception as ex:
        return {
            "error": 1,
            "message": f"Произошла ошибка при получении данных из RAS. Текст ошибки: {ex}",
            "data": ""
        }
    try:
        SimpleDateFormat = jpype.JClass('java.text.SimpleDateFormat')
        sdf = SimpleDateFormat("yyyy-MM-dd HH:mm:ss")
        result = {
            "date_offset": infobase_full_info.getDateOffset(),
            "dbms": infobase_full_info.getDbms(),
            "db_name": infobase_full_info.getDbName(),
            "db_server_name": infobase_full_info.getDbServerName(),
            "db_user": infobase_full_info.getDbUser(),
            "denied_from": sdf.format(infobase_full_info.getDeniedFrom()),
            "denied_message": infobase_full_info.getDeniedMessage(),
            "denied_parameter": infobase_full_info.getDeniedParameter(),
            "denied_to": sdf.format(infobase_full_info.getDeniedTo()),
            "description": infobase_full_info.getDescr(),
            "external_session_manager_connection_string": infobase_full_info.getExternalSessionManagerConnectionString(),
            "external_session_manager_required": infobase_full_info.getExternalSessionManagerRequired(),
            "infobase_id": infobase_full_info.getInfoBaseId().toString(),
            "license_distribution_allowed": infobase_full_info.getLicenseDistributionAllowed(),
            "locale": infobase_full_info.getLocale(),
            "name": infobase_full_info.getName(),
            "permission_code": infobase_full_info.getPermissionCode(),
            "reserve_working_processes": infobase_full_info.getReserveWorkingProcesses(),
            "safe_mode_security_profile_name": infobase_full_info.getSafeModeSecurityProfileName(),
            "security_level": infobase_full_info.getSecurityLevel(),
            "is_sessions_denied": infobase_full_info.isSessionsDenied(),
            "is_scheduled_jobs_denied": infobase_full_info.isScheduledJobsDenied(),
            "security_profile_name": infobase_full_info.getSecurityProfileName()
        }
        return {
            "error": 0,
            "message": "",
            "data": result
        }
    except Exception as ex:
        return {
            "error": 1,
            "message": f"Произошла ошибка при обработке данных. Текст ошибки: {ex}",
            "data": []
        }
