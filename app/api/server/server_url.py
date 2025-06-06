from fastapi import APIRouter, status
from fastapi.encoders import jsonable_encoder
from fastapi.responses import JSONResponse

from ...common.schemas.request import BaseRequest, NewWorkingServer, WorkingServerInfo
from .method.create_new_server import create_new_server
from .method.get_server_info import get_server_info
from .method.get_server_list import get_server_list
from .method.remove_server import remove_server
from .method.update_server import update_server

router = APIRouter(
    prefix='/v1/working_server',
    tags=['Администрирование рабочего сервера (/v1/working_server/*)']
)


@router.post('/info/one/', summary='Получение информации о рабочем сервере')
def working_server_info_one(req: WorkingServerInfo) -> JSONResponse:
    return JSONResponse(
        status_code=status.HTTP_200_OK,
        content=jsonable_encoder(get_server_info(req))
    )


@router.post('/info/list/', summary='Получение списка информации о рабочих серверах')
def working_server_info_list(req: BaseRequest) -> JSONResponse:
    return JSONResponse(
        status_code=status.HTTP_200_OK,
        content=jsonable_encoder(get_server_list(req))
    )


@router.post('/insert/', summary='Создание нового рабочего сервера')
def working_server_insert(req: NewWorkingServer) -> JSONResponse:
    return JSONResponse(
        status_code=status.HTTP_200_OK,
        content=jsonable_encoder(create_new_server(req))
    )


@router.post('/update/', summary='Обновление настроек рабочего сервера')
def working_server_update(req: NewWorkingServer) -> JSONResponse:
    return JSONResponse(
        status_code=status.HTTP_200_OK,
        content=jsonable_encoder(update_server(req))
    )


@router.post('/remove/', summary='Удаление рабочего сервера')
def working_server_remove(req: WorkingServerInfo) -> JSONResponse:
    return JSONResponse(
        status_code=status.HTTP_200_OK,
        content=jsonable_encoder(remove_server(req))
    )
