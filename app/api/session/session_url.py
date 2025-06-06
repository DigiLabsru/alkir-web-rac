from typing import Annotated

from fastapi import APIRouter, Query, status
from fastapi.encoders import jsonable_encoder
from fastapi.responses import JSONResponse, Response

from ...common.schemas.request import (
    SessionClusterList,
    SessionInfo,
    SessionInfobaseList,
    TerminateSession,
)
from .method.get_session_info import get_session_info
from .method.get_session_list_cluster import get_session_list_cluster
from .method.get_session_list_infobase import get_session_list_infobase
from .method.interrupt_current_server_call_session import (
    interrupt_current_server_call_session,
)
from .method.terminate_session import terminate_session

router = APIRouter(
    prefix='/v1/session',
    tags=['Администрирование сеансов информационных баз (/v1/session/*)']
)


@router.post('/list/infobase/', summary='Получение списка информации о сеансах в разрезе информационной базы')
def session_list_infobase(req: SessionInfobaseList) -> JSONResponse:
    return JSONResponse(
        status_code=status.HTTP_200_OK,
        content=jsonable_encoder(get_session_list_infobase(req))
    )


@router.get('/list/infobase/prometheus/', summary='Получение списка информации о сеансах в разрезе информационной базы в формате Prometheus')
def session_list_infobase_prometheus(req: Annotated[SessionInfobaseList, Query()]) -> JSONResponse:
    return Response(
        content=str(get_session_list_infobase(req=req, prometheus=True)),
        media_type="text/plain",  # Указываем MIME-тип
        headers={"X-Custom-Header": "text-data"}
    )


@router.post('/list/cluster/', summary='Получение списка информации о сеансах в разрезе кластера')
def session_list_cluster(req: SessionClusterList) -> JSONResponse:
    return JSONResponse(
        status_code=status.HTTP_200_OK,
        content=jsonable_encoder(get_session_list_cluster(req))
    )


@router.get('/list/cluster/prometheus/', summary='Получение списка информации о сеансах в разрезе кластера в формате Prometheus')
def session_list_cluster_prometheus(req: Annotated[SessionClusterList, Query()]) -> JSONResponse:
    return Response(
        content=str(get_session_list_cluster(req=req, prometheus=True)),
        media_type="text/plain",  # Указываем MIME-тип
        headers={"X-Custom-Header": "text-data"}
    )


@router.post('/info/', summary='Получение информации о сеансе', include_in_schema=False)
def session_info(req: SessionInfo) -> JSONResponse:
    return JSONResponse(
        status_code=status.HTTP_200_OK,
        content=jsonable_encoder(get_session_info(req))
    )


@router.post('/terminate/', summary='Получение информации о сеансе', include_in_schema=False)
def session_terminate(req: TerminateSession) -> JSONResponse:
    return JSONResponse(
        status_code=status.HTTP_200_OK,
        content=jsonable_encoder(terminate_session(req))
    )


@router.post('/interrupt-current-server-call/', summary='Получение информации о сеансе', include_in_schema=False)
def session_interrupt_current_server_call(req: TerminateSession) -> JSONResponse:
    return JSONResponse(
        status_code=status.HTTP_200_OK,
        content=jsonable_encoder(interrupt_current_server_call_session(req))
    )
