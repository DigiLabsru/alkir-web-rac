import jpype

from ....common.interface.ras.ras import RasInterface
from ....common.schemas.request import InfoBase


def get_infobase_info_list(req: InfoBase):
    try:
        rac = RasInterface(req=req)
        infobases_list = rac.java_get_info_bases()
        rac.close()
    except Exception as ex:
        return {
            "error": 1,
            "message": f"Произошла ошибка при получении данных из RAS. Текст ошибки: {ex}",
            "data": ""
        }
    try:
        result: list = []
        SimpleDateFormat = jpype.JClass('java.text.SimpleDateFormat')
        sdf = SimpleDateFormat("yyyy-MM-dd HH:mm:ss")
        for one_base in infobases_list:
            result.append(
                {
                    "date_offset": one_base.getDateOffset(),
                    "dbms": one_base.getDbms(),
                    "db_name": one_base.getDbName(),
                    "db_server_name": one_base.getDbServerName(),
                    "db_user": one_base.getDbUser(),
                    "denied_from": sdf.format(one_base.getDeniedFrom()),
                    "denied_message": one_base.getDeniedMessage(),
                    "denied_parameter": one_base.getDeniedParameter(),
                    "denied_to": sdf.format(one_base.getDeniedTo()),
                    "description": one_base.getDescr(),
                    "external_session_manager_connection_string": one_base.getExternalSessionManagerConnectionString(),
                    "external_session_manager_required": one_base.getExternalSessionManagerRequired(),
                    "infobase_id": one_base.getInfoBaseId().toString(),
                    "license_distribution_allowed": one_base.getLicenseDistributionAllowed(),
                    "locale": one_base.getLocale(),
                    "name": one_base.getName(),
                    "permission_code": one_base.getPermissionCode(),
                    "reserve_working_processes": one_base.getReserveWorkingProcesses(),
                    "safe_mode_security_profile_name": one_base.getSafeModeSecurityProfileName(),
                    "security_level": one_base.getSecurityLevel(),
                    "is_sessions_denied": one_base.isSessionsDenied(),
                    "is_scheduled_jobs_denied": one_base.isScheduledJobsDenied(),
                    "security_profile_name": one_base.getSecurityProfileName()
                }
            )
    except Exception as ex:
        return {
            "error": 1,
            "message": f"Произошла ошибка при обработке данных. Текст ошибки: {ex}",
            "data": []
        }

    return {
        "error": 0,
        "message": "",
        "data": result
    }
