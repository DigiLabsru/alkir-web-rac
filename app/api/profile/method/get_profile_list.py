from ....common.interface.ras.ras import RasInterface
from ....common.schemas.request import BaseRequest


def get_profile_list(req: BaseRequest):
    try:
        rac = RasInterface(req=req)
        rac_data = rac.java_get_security_profiles()
        rac.close()
    except Exception as ex:
        return {
            "error": 1,
            "message": f"Произошла ошибка при получении данных из RAS. Текст ошибки: {ex}",
            "data": []
        }
    try:
        result: list = []
        for one_data in rac_data:
            result.append(
                {
                    "add_in_use_full_access": one_data.getAddInUseFullAccess(),
                    "all_modules_extension": one_data.getAllModulesExtension(),
                    "com_use_full_access": one_data.getComUseFullAccess(),
                    "cryptography_allowed": one_data.getCryptographyAllowed(),
                    "descr": one_data.getDescr(),
                    "external_app_full_access": one_data.getExternalAppFullAccess(),
                    "file_system_full_access": one_data.getFileSystemFullAccess(),
                    "full_privileged_mode": one_data.getFullPrivilegedMode(),
                    "internet_use_full_access": one_data.getInternetUseFullAccess(),
                    "modules_available_for_extension": one_data.getModulesAvailableForExtension(),
                    "modules_not_available_for_extension": one_data.getModulesNotAvailableForExtension(),
                    "privileged_mode_in_safe_mode_allowed": one_data.getPrivilegedModeInSafeModeAllowed(),
                    "privileged_mode_roles": one_data.getPrivilegedModeRoles(),
                    "right_extension": one_data.getRightExtension(),
                    "right_extension_definition_roles": one_data.getRightExtensionDefinitionRoles(),
                    "safe_mode_profile": one_data.getSafeModeProfile(),
                    "sp_name": one_data.getSPName(),
                    "unsafe_external_module_full_access": one_data.getUnsafeExternalModuleFullAccess()
                }
            )
    except Exception as ex:
        return {
            "error": 1,
            "message": f"Произошла ошибка при обработке данных. Текст ошибки: {ex}",
            "data": {}
        }

    return {
        "error": 0,
        "message": "",
        "data": result
    }
