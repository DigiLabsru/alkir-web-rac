import jpype

from .....schemas.request import (
    NewSecurityProfile,
    NewSecurityProfileAddIn,
    NewSecurityProfileApplication,
    NewSecurityProfileCOMClass,
    NewSecurityProfileExternalModule,
    NewSecurityProfileInternetResource,
    NewSecurityProfileVirtualDirectory,
)


class SecurityProfile():
    def java_get_security_profile_add_ins(self, sp_name: str):
        self.authenticate()
        return self.connection.getSecurityProfileAddIns(self.cluster_id, sp_name)

    def java_get_security_profile_applications(self, sp_name: str):
        self.authenticate()
        return self.connection.getSecurityProfileApplications(self.cluster_id, sp_name)

    def java_get_security_profile_com_classes(self, sp_name: str):
        self.authenticate()
        return self.connection.getSecurityProfileComClasses(self.cluster_id, sp_name)

    def java_get_security_profile_internet_resources(self, sp_name: str):
        self.authenticate()
        return self.connection.getSecurityProfileInternetResources(self.cluster_id, sp_name)

    def java_get_security_profiles(self):
        self.authenticate()
        return self.connection.getSecurityProfiles(self.cluster_id)

    def java_get_security_profile_unsafe_external_modules(self, sp_name: str):
        self.authenticate()
        return self.connection.getSecurityProfileUnsafeExternalModules(self.cluster_id, sp_name)

    def java_get_security_profile_virtual_directories(self, sp_name: str):
        self.authenticate()
        return self.connection.getSecurityProfileVirtualDirectories(self.cluster_id, sp_name)

    def java_create_security_profile(self, property: NewSecurityProfile):
        self.authenticate()
        SecurityProfile = jpype.JClass("com._1c.v8.ibis.admin.SecurityProfile")
        new_object = SecurityProfile()
        new_object.setAddInUseFullAccess(property.add_in_use_full_access)
        new_object.setAllModulesExtension(property.all_modules_extension)
        new_object.setComUseFullAccess(property.com_use_full_access)
        new_object.setCryptographyAllowed(property.cryptography_allowed)
        new_object.setDescr(property.descr)
        new_object.setExternalAppFullAccess(property.external_app_full_access)
        new_object.setFileSystemFullAccess(property.file_system_full_access)
        new_object.setFullPrivilegedMode(property.full_privileged_mode)
        new_object.setInternetUseFullAccess(property.internet_use_full_access)
        new_object.setModulesAvailableForExtension(property.modules_available_for_extension)
        new_object.setModulesNotAvailableForExtension(property.modules_not_available_for_extension)
        new_object.setPrivilegedModeInSafeModeAllowed(property.privileged_mode_in_safe_mode_allowed)
        new_object.setPrivilegedModeRoles(property.privileged_mode_roles)
        new_object.setRightExtension(property.right_extension)
        new_object.setRightExtensionDefinitionRoles(property.right_extension_definition_roles)
        new_object.setSafeModeProfile(property.safe_mode_profile)
        new_object.setSPName(property.sp_name)
        new_object.setUnsafeExternalModuleFullAccess(property.unsafe_external_module_full_access)
        return self.connection.createSecurityProfile(self.cluster_id, new_object)

    def java_update_security_profile(self, property: NewSecurityProfile):
        self.authenticate()
        profiles = self.connection.getSecurityProfiles(self.cluster_id)
        for one_profile in profiles:
            if one_profile.getSPName() == property.sp_name:
                new_object = one_profile
                break
        new_object.setAddInUseFullAccess(property.add_in_use_full_access)
        new_object.setAllModulesExtension(property.all_modules_extension)
        new_object.setComUseFullAccess(property.com_use_full_access)
        new_object.setCryptographyAllowed(property.cryptography_allowed)
        new_object.setDescr(property.descr)
        new_object.setExternalAppFullAccess(property.external_app_full_access)
        new_object.setFileSystemFullAccess(property.file_system_full_access)
        new_object.setFullPrivilegedMode(property.full_privileged_mode)
        new_object.setInternetUseFullAccess(property.internet_use_full_access)
        new_object.setModulesAvailableForExtension(property.modules_available_for_extension)
        new_object.setModulesNotAvailableForExtension(property.modules_not_available_for_extension)
        new_object.setPrivilegedModeInSafeModeAllowed(property.privileged_mode_in_safe_mode_allowed)
        new_object.setPrivilegedModeRoles(property.privileged_mode_roles)
        new_object.setRightExtension(property.right_extension)
        new_object.setRightExtensionDefinitionRoles(property.right_extension_definition_roles)
        new_object.setSafeModeProfile(property.safe_mode_profile)
        new_object.setSPName(property.sp_name)
        new_object.setUnsafeExternalModuleFullAccess(property.unsafe_external_module_full_access)
        return self.connection.createSecurityProfile(self.cluster_id, new_object)

    def java_drop_security_profile(self, sp_name: str):
        self.authenticate()
        return self.connection.dropSecurityProfile(self.cluster_id, sp_name)

    def java_create_security_profile_add_in(self, property: NewSecurityProfileAddIn):
        self.authenticate()
        SecurityProfile = jpype.JClass("com._1c.v8.ibis.admin.SecurityProfileAddIn")
        new_object = SecurityProfile()
        new_object.setAddInHash(property.add_in_hash)
        new_object.setDescr(property.descr)
        new_object.setName(property.name)
        new_object.setSPName(property.sp_name)
        return self.connection.createSecurityProfileAddIn(self.cluster_id, new_object)

    def java_update_security_profile_add_in(self, property: NewSecurityProfileAddIn):
        self.authenticate()
        profiles = self.connection.getSecurityProfileAddIns(self.cluster_id, property.sp_name)
        for one_profile in profiles:
            if one_profile.getName() == property.name:
                new_object = one_profile
                break
        new_object.setAddInHash(property.add_in_hash)
        new_object.setDescr(property.descr)
        new_object.setName(property.name)
        new_object.setSPName(property.sp_name)
        return self.connection.createSecurityProfileAddIn(self.cluster_id, new_object)

    def java_drop_security_profile_add_in(self, sp_name: str, name: str):
        self.authenticate()
        return self.connection.dropSecurityProfileAddIn(self.cluster_id, sp_name, name)

    def java_create_security_profile_application(self, property: NewSecurityProfileApplication):
        self.authenticate()
        SecurityProfile = jpype.JClass("com._1c.v8.ibis.admin.SecurityProfileApplication")
        new_object = SecurityProfile()
        new_object.setCommandWild(property.command_wild)
        new_object.setDescr(property.descr)
        new_object.setName(property.name)
        new_object.setSPName(property.sp_name)
        return self.connection.createSecurityProfileApplication(self.cluster_id, new_object)

    def java_update_security_profile_application(self, property: NewSecurityProfileApplication):
        self.authenticate()
        profiles = self.connection.getSecurityProfileApplications(self.cluster_id, property.sp_name)
        for one_profile in profiles:
            if one_profile.getSPName() == property.sp_name:
                new_object = one_profile
                break
        new_object.setCommandWild(property.command_wild)
        new_object.setDescr(property.descr)
        new_object.setName(property.name)
        new_object.setSPName(property.sp_name)
        return self.connection.createSecurityProfileApplication(self.cluster_id, new_object)

    def java_drop_security_profile_application(self, sp_name: str, name: str):
        self.authenticate()
        return self.connection.dropSecurityProfileApplication(self.cluster_id, sp_name, name)

    def java_create_security_profile_com_class(self, property: NewSecurityProfileCOMClass):
        self.authenticate()
        SecurityProfile = jpype.JClass("com._1c.v8.ibis.admin.SecurityProfileCOMClass")
        new_object = SecurityProfile()
        new_object.setComputerName(property.computer_name)
        new_object.setDescr(property.descr)
        new_object.setFileName(property.file_name)
        new_object.setName(property.name)
        new_object.setObjectUuid(property.Object_uuid)
        new_object.setSPName(property.sp_name)
        return self.connection.createSecurityProfileComClass(self.cluster_id, new_object)

    def java_update_security_profile_com_class(self, property: NewSecurityProfileCOMClass):
        self.authenticate()
        profiles = self.connection.getSecurityProfileComClasses(self.cluster_id, property.sp_name)
        for one_profile in profiles:
            if one_profile.getSPName() == property.sp_name:
                new_object = one_profile
                break
        new_object.setComputerName(property.computer_name)
        new_object.setDescr(property.descr)
        new_object.setFileName(property.file_name)
        new_object.setName(property.name)
        new_object.setObjectUuid(property.object_uuid)
        new_object.setSPName(property.sp_name)
        return self.connection.createSecurityProfileComClass(self.cluster_id, new_object)

    def java_drop_security_profile_com_class(self, sp_name: str, name: str):
        self.authenticate()
        return self.connection.dropSecurityProfileComClass(self.cluster_id, sp_name, name)

    def java_create_security_profile_internet_resource(self, property: NewSecurityProfileInternetResource):
        self.authenticate()
        SecurityProfile = jpype.JClass("com._1c.v8.ibis.admin.SecurityProfileInternetResource")
        new_object = SecurityProfile()
        new_object.setAddress(property.address)
        new_object.setDescr(property.descr)
        new_object.setName(property.name)
        new_object.setPort(property.port)
        new_object.setProtocol(property.protocol)
        new_object.setSPName(property.sp_name)

        return self.connection.createSecurityProfileInternetResource(self.cluster_id, new_object)

    def java_update_security_profile_internet_resource(self, property: NewSecurityProfileInternetResource):
        self.authenticate()
        profiles = self.connection.getSecurityProfileInternetResources(self.cluster_id, property.sp_name)
        for one_profile in profiles:
            if one_profile.getSPName() == property.sp_name:
                new_object = one_profile
                break
        new_object.setAddress(property.address)
        new_object.setDescr(property.descr)
        new_object.setName(property.name)
        new_object.setPort(property.port)
        new_object.setProtocol(property.protocol)
        new_object.setSPName(property.sp_name)
        return self.connection.createSecurityProfileInternetResource(self.cluster_id, new_object)

    def java_drop_security_profile_internet_resource(self, sp_name: str, name: str):
        self.authenticate()
        return self.connection.dropSecurityProfileInternetResource(self.cluster_id, sp_name, name)

    def java_create_security_profile_external_module(self, property: NewSecurityProfileExternalModule):
        self.authenticate()
        SecurityProfile = jpype.JClass("com._1c.v8.ibis.admin.SecurityProfileExternalModule")
        new_object = SecurityProfile()
        new_object.setDescr(property.descr)
        new_object.setModuleHash(property.module_hash)
        new_object.setName(property.name)
        new_object.setSPName(property.sp_name)
        return self.connection.createSecurityProfileUnsafeExternalModule(self.cluster_id, new_object)

    def java_update_security_profile_external_module(self, property: NewSecurityProfileExternalModule):
        self.authenticate()
        profiles = self.connection.getSecurityProfileUnsafeExternalModules(self.cluster_id, property.sp_name)
        for one_profile in profiles:
            if one_profile.getSPName() == property.sp_name:
                new_object = one_profile
                break
        new_object.setDescr(property.descr)
        new_object.setModuleHash(property.module_hash)
        new_object.setName(property.name)
        new_object.setSPName(property.sp_name)
        return self.connection.createSecurityProfileUnsafeExternalModule(self.cluster_id, new_object)

    def java_drop_security_profile_external_module(self, sp_name: str, name: str):
        self.authenticate()
        return self.connection.dropSecurityProfileUnsafeExternalModule(self.cluster_id, sp_name, name)

    def java_create_security_profile_virtual_directory(self, property: NewSecurityProfileVirtualDirectory):
        self.authenticate()
        SecurityProfile = jpype.JClass("com._1c.v8.ibis.admin.SecurityProfileVirtualDirectory")
        new_object = SecurityProfile()
        new_object.setAlias(property.alias)
        new_object.setAllowedRead(property.allowed_read)
        new_object.setAllowedWrite(property.allowed_write)
        new_object.setDescr(property.descr)
        new_object.setPhysicalPath(property.physical_path)
        new_object.setSPName(property.sp_name)
        return self.connection.createSecurityProfileVirtualDirectory(self.cluster_id, new_object)

    def java_update_security_profile_virtual_directory(self, property: NewSecurityProfileVirtualDirectory):
        self.authenticate()
        profiles = self.connection.getSecurityProfileVirtualDirectories(self.cluster_id, property.sp_name)
        for one_profile in profiles:
            if one_profile.getSPName() == property.sp_name:
                new_object = one_profile
                break
        new_object.setAlias(property.alias)
        new_object.setAllowedRead(property.allowed_read)
        new_object.setAllowedWrite(property.allowed_write)
        new_object.setDescr(property.descr)
        new_object.setPhysicalPath(property.physical_path)
        new_object.setSPName(property.sp_name)
        return self.connection.createSecurityProfileVirtualDirectory(self.cluster_id, new_object)

    def java_drop_security_profile_virtual_directory(self, sp_name: str, alias: str):
        self.authenticate()
        return self.connection.dropSecurityProfileVirtualDirectory(self.cluster_id, sp_name, alias)
