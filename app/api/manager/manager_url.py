from fastapi import APIRouter, status
from fastapi.encoders import jsonable_encoder
from fastapi.responses import JSONResponse

from ...common.schemas.request import BaseRequest, ClusterManagerInfo
from .method.get_manager_info import get_manager_info
from .method.get_manager_list import get_manager_list

router = APIRouter(
    prefix='/v1/manager',
    tags=['Администрирование менеджера кластера серверов (/v1/manager/*)']
)


@router.post('/info/one/', summary='Получение информации о менеджере')
def manager_info_one(req: ClusterManagerInfo) -> JSONResponse:
    return JSONResponse(
        status_code=status.HTTP_200_OK,
        content=jsonable_encoder(get_manager_info(req))
    )


@router.post('/info/list/', summary='Получение списка информации о менеджерах')
def manager_info_list(req: BaseRequest) -> JSONResponse:
    return JSONResponse(
        status_code=status.HTTP_200_OK,
        content=jsonable_encoder(get_manager_list(req))
    )
