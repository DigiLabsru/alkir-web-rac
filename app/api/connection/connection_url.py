from fastapi import APIRouter, status
from fastapi.encoders import jsonable_encoder
from fastapi.responses import JSONResponse

from ...common.schemas.request import (ConnectionIBList, ConnectionInfo,
                                       ConnectionInfoDis, ConnectionList)
from .method.disconnect_connection import disconnect_connection
from .method.get_connection_info import get_connection_info
from .method.get_connection_infobase import get_connection_infobase
from .method.get_connection_list import get_connection_list

router = APIRouter(
    prefix='/v1/connection',
    tags=['Администрирование соединений (/v1/connection/*)']
)


@router.post('/info/', summary='Получение информации о соединении')
def connection_info(req: ConnectionInfo) -> JSONResponse:
    return JSONResponse(
        status_code=status.HTTP_200_OK,
        content=jsonable_encoder(get_connection_info(req))
    )


@router.post('/summary/list/', summary='Получение списка соединений')
def connection_list(req: ConnectionList) -> JSONResponse:
    return JSONResponse(
        status_code=status.HTTP_200_OK,
        content=jsonable_encoder(get_connection_list(req))
    )


@router.post('/summary/infobase/', summary='Получение списка соединений по ИБ')
def connection_infobase(req: ConnectionIBList) -> JSONResponse:
    return JSONResponse(
        status_code=status.HTTP_200_OK,
        content=jsonable_encoder(get_connection_infobase(req))
    )


@router.post('/disconnect/', summary='Разрыв соединения')
def connection_disconnect(req: ConnectionInfoDis) -> JSONResponse:
    return JSONResponse(
        status_code=status.HTTP_200_OK,
        content=jsonable_encoder(disconnect_connection(req))
    )
