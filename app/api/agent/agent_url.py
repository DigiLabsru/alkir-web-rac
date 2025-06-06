from fastapi import APIRouter, status
from fastapi.encoders import jsonable_encoder
from fastapi.responses import JSONResponse

from ...common.schemas.request import BaseRequest, NewAdmin, RemoveAdmin
from .method.create_new_agent_admin import create_new_agent_admin
from .method.get_agent_admins import get_agent_admins
from .method.get_agent_version import get_agent_version
from .method.remove_agent_admin import remove_agent_admin

router = APIRouter(
    prefix='/v1/agent',
    tags=['Администрирование агента кластера серверов (/v1/agent/*)']
)


@router.post('/admin/list/', summary='Получение списка администраторов агента кластера')
def agent_admin_list(req: BaseRequest) -> JSONResponse:
    return JSONResponse(
        status_code=status.HTTP_200_OK,
        content=jsonable_encoder(get_agent_admins(req))
    )


@router.post('/admin/register/', summary='Добавление нового администратора агента кластера')
def agent_register_admin(req: NewAdmin) -> JSONResponse:
    return JSONResponse(
        status_code=status.HTTP_200_OK,
        content=jsonable_encoder(create_new_agent_admin(req))
    )


@router.post('/admin/remove/', summary='Удаление администратора агента кластера')
def agent_remove_admin(req: RemoveAdmin) -> JSONResponse:
    return JSONResponse(
        status_code=status.HTTP_200_OK,
        content=jsonable_encoder(remove_agent_admin(req))
    )


@router.post('/version/', summary='Получение версии агента кластера')
def agent_versions(req: BaseRequest) -> JSONResponse:
    return JSONResponse(
        status_code=status.HTTP_200_OK,
        content=jsonable_encoder(get_agent_version(req))
    )
