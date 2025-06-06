from typing import Annotated

from fastapi import APIRouter, Query, status
from fastapi.encoders import jsonable_encoder
from fastapi.responses import JSONResponse, Response

from ...common.schemas.request import BaseRequest, WorkingProcessInfo
from .method.get_process_info import get_process_info
from .method.get_process_list import get_process_list

router = APIRouter(
    prefix='/v1/working_process',
    tags=['Администрирование рабочего процесса (/v1/working_process/*)']
)


@router.post('/info/one/', summary='Получение информации о рабочем процессе')
def working_process_info_one(req: WorkingProcessInfo) -> JSONResponse:
    return JSONResponse(
        status_code=status.HTTP_200_OK,
        content=jsonable_encoder(get_process_info(req))
    )


@router.post('/info/list/', summary='Получение списка информации о рабочих процессах')
def working_process_info_list(req: BaseRequest) -> JSONResponse:
    return JSONResponse(
        status_code=status.HTTP_200_OK,
        content=jsonable_encoder(get_process_list(req))
    )


@router.get('/info/list/prometheus/', summary='Получение списка информации о сеансах в разрезе кластера в формате Prometheus')
def session_list_cluster_prometheus(req: Annotated[BaseRequest, Query()]) -> JSONResponse:
    return Response(
        content=str(get_process_list(req=req, prometheus=True)),
        media_type="text/plain",  # Указываем MIME-тип
        headers={"X-Custom-Header": "text-data"}
    )
