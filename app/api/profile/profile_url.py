from fastapi import APIRouter, status
from fastapi.encoders import jsonable_encoder
from fastapi.responses import JSONResponse

from ...common.schemas.request import (BaseRequest, NewSecurityProfile,
                                       NewSecurityProfileAddIn,
                                       NewSecurityProfileApplication,
                                       NewSecurityProfileCOMClass,
                                       NewSecurityProfileExternalModule,
                                       NewSecurityProfileInternetResource,
                                       NewSecurityProfileVirtualDirectory,
                                       SecurityProfileDropInfo,
                                       SecurityProfileDropInfoExt,
                                       SecurityProfileDropInfoExtVD)
from .method.create_new_profile import create_new_profile
from .method.create_new_profile_add_in import create_new_profile_add_in
from .method.create_new_profile_application import \
    create_new_profile_application
from .method.create_new_profile_com_class import create_new_profile_com_class
from .method.create_new_profile_external_module import \
    create_new_profile_external_module
from .method.create_new_profile_internet_resource import \
    create_new_profile_internet_resource
from .method.create_new_profile_virtual_directory import \
    create_new_profile_virtual_directory
from .method.get_profile_add_in_list import get_profile_add_in_list
from .method.get_profile_application_list import get_profile_application_list
from .method.get_profile_com_class_list import get_profile_com_class_list
from .method.get_profile_external_module_list import \
    get_profile_external_module_list
from .method.get_profile_internet_resource_list import \
    get_profile_internet_resource_list
from .method.get_profile_list import get_profile_list
from .method.get_profile_virtual_directories_list import \
    get_profile_virtual_directories_list
from .method.remove_profile import remove_profile
from .method.remove_profile_add_in import remove_profile_add_in
from .method.remove_profile_application import remove_profile_application
from .method.remove_profile_com_class import remove_profile_com_class
from .method.remove_profile_external_module import \
    remove_profile_external_module
from .method.remove_profile_internet_resource import \
    remove_profile_internet_resource
from .method.remove_profile_virtual_directory import \
    remove_profile_virtual_directory
from .method.update_profile import update_profile
from .method.update_profile_add_in import update_profile_add_in
from .method.update_profile_application import update_profile_application
from .method.update_profile_com_class import update_profile_com_class
from .method.update_profile_external_module import \
    update_profile_external_module
from .method.update_profile_internet_resource import \
    update_profile_internet_resource
from .method.update_profile_virtual_directory import \
    update_profile_virtual_directory

router = APIRouter(
    prefix='/v1/profile',
    tags=['Администрирование профилей безопасности (/v1/profile/*)']
)


@router.post('/info/list/', summary='Получение списка информации о профилях безопасности')
def profile_info_list(req: BaseRequest) -> JSONResponse:
    return JSONResponse(
        status_code=status.HTTP_200_OK,
        content=jsonable_encoder(get_profile_list(req))
    )


@router.post('/info/list/add_in/', summary='Получение списка информации о профилях безопасности add_in')
def profile_info_add_in_list(req: SecurityProfileDropInfo) -> JSONResponse:
    return JSONResponse(
        status_code=status.HTTP_200_OK,
        content=jsonable_encoder(get_profile_add_in_list(req))
    )


@router.post('/info/list/application/', summary='Получение списка информации о профилях безопасности application')
def profile_info_application_list(req: SecurityProfileDropInfo) -> JSONResponse:
    return JSONResponse(
        status_code=status.HTTP_200_OK,
        content=jsonable_encoder(get_profile_application_list(req))
    )


@router.post('/info/list/com_class/', summary='Получение списка информации о профилях безопасности com_class')
def profile_info_com_class_list(req: SecurityProfileDropInfo) -> JSONResponse:
    return JSONResponse(
        status_code=status.HTTP_200_OK,
        content=jsonable_encoder(get_profile_com_class_list(req))
    )


@router.post('/info/list/internet_resource/', summary='Получение списка информации о профилях безопасности internet_resource')
def profile_info_internet_resource_list(req: SecurityProfileDropInfo) -> JSONResponse:
    return JSONResponse(
        status_code=status.HTTP_200_OK,
        content=jsonable_encoder(get_profile_internet_resource_list(req))
    )


@router.post('/info/list/external_module/', summary='Получение списка информации о профилях безопасности external_module')
def profile_info_external_module_list(req: SecurityProfileDropInfo) -> JSONResponse:
    return JSONResponse(
        status_code=status.HTTP_200_OK,
        content=jsonable_encoder(get_profile_external_module_list(req))
    )


@router.post('/info/list/virtual_directories/', summary='Получение списка информации о профилях безопасности virtual_directories')
def profile_info_virtual_directories_list(req: SecurityProfileDropInfo) -> JSONResponse:
    return JSONResponse(
        status_code=status.HTTP_200_OK,
        content=jsonable_encoder(get_profile_virtual_directories_list(req))
    )


@router.post('/insert/', summary='Создание нового профиля безопасности')
def profile_insert(req: NewSecurityProfile) -> JSONResponse:
    return JSONResponse(
        status_code=status.HTTP_200_OK,
        content=jsonable_encoder(create_new_profile(req))
    )


@router.post('/update/', summary='Обновление настроек профиля безопасности')
def profile_update(req: NewSecurityProfile) -> JSONResponse:
    return JSONResponse(
        status_code=status.HTTP_200_OK,
        content=jsonable_encoder(update_profile(req))
    )


@router.post('/insert/add_in/', summary='Создание нового профиля безопасности add_in')
def profile_insert_add_in(req: NewSecurityProfileAddIn) -> JSONResponse:
    return JSONResponse(
        status_code=status.HTTP_200_OK,
        content=jsonable_encoder(create_new_profile_add_in(req))
    )


@router.post('/update/add_in/', summary='Обновление настроек профиля безопасности add_in')
def profile_update_add_in(req: NewSecurityProfileAddIn) -> JSONResponse:
    return JSONResponse(
        status_code=status.HTTP_200_OK,
        content=jsonable_encoder(update_profile_add_in(req))
    )


@router.post('/insert/application/', summary='Создание нового профиля безопасности application')
def profile_insert_application(req: NewSecurityProfileApplication) -> JSONResponse:
    return JSONResponse(
        status_code=status.HTTP_200_OK,
        content=jsonable_encoder(create_new_profile_application(req))
    )


@router.post('/update/application/', summary='Обновление настроек профиля безопасности application')
def profile_update_application(req: NewSecurityProfileApplication) -> JSONResponse:
    return JSONResponse(
        status_code=status.HTTP_200_OK,
        content=jsonable_encoder(update_profile_application(req))
    )


@router.post('/insert/com_class/', summary='Создание нового профиля безопасности com_class')
def profile_insert_com_class(req: NewSecurityProfileCOMClass) -> JSONResponse:
    return JSONResponse(
        status_code=status.HTTP_200_OK,
        content=jsonable_encoder(create_new_profile_com_class(req))
    )


@router.post('/update/com_class/', summary='Обновление настроек профиля безопасности com_class')
def profile_update_com_class(req: NewSecurityProfileCOMClass) -> JSONResponse:
    return JSONResponse(
        status_code=status.HTTP_200_OK,
        content=jsonable_encoder(update_profile_com_class(req))
    )


@router.post('/insert/external_module/', summary='Создание нового профиля безопасности external_module')
def profile_insert_external_module(req: NewSecurityProfileExternalModule) -> JSONResponse:
    return JSONResponse(
        status_code=status.HTTP_200_OK,
        content=jsonable_encoder(create_new_profile_external_module(req))
    )


@router.post('/update/external_module/', summary='Обновление настроек профиля безопасности external_module')
def profile_update_external_module(req: NewSecurityProfileExternalModule) -> JSONResponse:
    return JSONResponse(
        status_code=status.HTTP_200_OK,
        content=jsonable_encoder(update_profile_external_module(req))
    )


@router.post('/insert/internet_resource/', summary='Создание нового профиля безопасности internet_resource')
def profile_insert_internet_resource(req: NewSecurityProfileInternetResource) -> JSONResponse:
    return JSONResponse(
        status_code=status.HTTP_200_OK,
        content=jsonable_encoder(create_new_profile_internet_resource(req))
    )


@router.post('/update/internet_resource/', summary='Обновление настроек профиля безопасности internet_resource')
def profile_update_internet_resource(req: NewSecurityProfileInternetResource) -> JSONResponse:
    return JSONResponse(
        status_code=status.HTTP_200_OK,
        content=jsonable_encoder(update_profile_internet_resource(req))
    )


@router.post('/insert/virtual_directory/', summary='Создание нового профиля безопасности virtual_directory')
def profile_insert_virtual_directory(req: NewSecurityProfileVirtualDirectory) -> JSONResponse:
    return JSONResponse(
        status_code=status.HTTP_200_OK,
        content=jsonable_encoder(create_new_profile_virtual_directory(req))
    )


@router.post('/update/virtual_directory/', summary='Обновление настроек профиля безопасности virtual_directory')
def profile_update_virtual_directory(req: NewSecurityProfileVirtualDirectory) -> JSONResponse:
    return JSONResponse(
        status_code=status.HTTP_200_OK,
        content=jsonable_encoder(update_profile_virtual_directory(req))
    )


@router.post('/remove/', summary='Удаление профиля безопасности')
def profile_remove(req: SecurityProfileDropInfo) -> JSONResponse:
    return JSONResponse(
        status_code=status.HTTP_200_OK,
        content=jsonable_encoder(remove_profile(req))
    )


@router.post('/remove/add_in/', summary='Удаление профиля безопасности add_in')
def profile_remove_add_in(req: SecurityProfileDropInfoExt) -> JSONResponse:
    return JSONResponse(
        status_code=status.HTTP_200_OK,
        content=jsonable_encoder(remove_profile_add_in(req))
    )


@router.post('/remove/application/', summary='Удаление профиля безопасности application')
def profile_remove_application(req: SecurityProfileDropInfoExt) -> JSONResponse:
    return JSONResponse(
        status_code=status.HTTP_200_OK,
        content=jsonable_encoder(remove_profile_application(req))
    )


@router.post('/remove/com_class/', summary='Удаление профиля безопасности com_class')
def profile_remove_com_class(req: SecurityProfileDropInfoExt) -> JSONResponse:
    return JSONResponse(
        status_code=status.HTTP_200_OK,
        content=jsonable_encoder(remove_profile_com_class(req))
    )


@router.post('/remove/external_module/', summary='Удаление профиля безопасности external_module')
def profile_remove_external_module(req: SecurityProfileDropInfoExt) -> JSONResponse:
    return JSONResponse(
        status_code=status.HTTP_200_OK,
        content=jsonable_encoder(remove_profile_external_module(req))
    )


@router.post('/remove/internet_resource/', summary='Удаление профиля безопасности internet_resource')
def profile_remove_internet_resource(req: SecurityProfileDropInfoExt) -> JSONResponse:
    return JSONResponse(
        status_code=status.HTTP_200_OK,
        content=jsonable_encoder(remove_profile_internet_resource(req))
    )


@router.post('/remove/virtual_directory/', summary='Удаление профиля безопасности virtual_directory')
def profile_remove_virtual_directory(req: SecurityProfileDropInfoExtVD) -> JSONResponse:
    return JSONResponse(
        status_code=status.HTTP_200_OK,
        content=jsonable_encoder(remove_profile_virtual_directory(req))
    )
