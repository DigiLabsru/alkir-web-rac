from fastapi import APIRouter, status
from fastapi.encoders import jsonable_encoder
from fastapi.responses import JSONResponse

from ...common.schemas.request import BaseRequest, NewAdmin, NewCluster, RemoveAdmin
from .method.create_new_cluster import create_new_cluster
from .method.create_new_cluster_admin import create_new_cluster_admin
from .method.get_cluster_admins import get_cluster_admins
from .method.get_cluster_info import get_cluster_info
from .method.get_cluster_list import get_cluster_list
from .method.remove_cluster import remove_cluster
from .method.remove_cluster_admin import remove_cluster_admin
from .method.update_cluster import update_cluster

router = APIRouter(
    prefix='/v1/cluster',
    tags=['Администрирование кластера серверов (/v1/cluster/*)']
)


@router.post('/admin/list/', summary='Получение списка администраторов кластера')
def cluster_admin_list(req: BaseRequest) -> JSONResponse:
    return JSONResponse(
        status_code=status.HTTP_200_OK,
        content=jsonable_encoder(get_cluster_admins(req))
    )


@router.post('/admin/register/', summary='Добавление нового администратора кластера')
def cluster_admin_register(req: NewAdmin) -> JSONResponse:
    return JSONResponse(
        status_code=status.HTTP_200_OK,
        content=jsonable_encoder(create_new_cluster_admin(req))
    )


@router.post('/admin/remove/', summary='Удаление администратора кластера')
def cluster_admin_remove(req: RemoveAdmin) -> JSONResponse:
    return JSONResponse(
        status_code=status.HTTP_200_OK,
        content=jsonable_encoder(remove_cluster_admin(req))
    )


@router.post('/info/', summary='Получение информации о кластере')
def cluster_info(req: BaseRequest) -> JSONResponse:
    return JSONResponse(
        status_code=status.HTTP_200_OK,
        content=jsonable_encoder(get_cluster_info(req))
    )


@router.post('/list/', summary='Получение списка описаний кластеров, зарегистрированных на центральном сервере.')
def cluster_list(req: BaseRequest) -> JSONResponse:
    return JSONResponse(
        status_code=status.HTTP_200_OK,
        content=jsonable_encoder(get_cluster_list(req))
    )


@router.post('/insert/', summary='Создание нового кластера')
def cluster_insert(req: NewCluster) -> JSONResponse:
    return JSONResponse(
        status_code=status.HTTP_200_OK,
        content=jsonable_encoder(create_new_cluster(req))
    )


@router.post('/update/', summary='Обновление настроек кластера')
def cluster_update(req: NewCluster) -> JSONResponse:
    return JSONResponse(
        status_code=status.HTTP_200_OK,
        content=jsonable_encoder(update_cluster(req))
    )


@router.post('/remove/', summary='Удаление кластера', description="Учетные данные для аутентификации должны быть из удаляемого кластера")
def cluster_remove(req: BaseRequest) -> JSONResponse:
    return JSONResponse(
        status_code=status.HTTP_200_OK,
        content=jsonable_encoder(remove_cluster(req))
    )
