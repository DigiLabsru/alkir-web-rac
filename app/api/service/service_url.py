from fastapi import APIRouter, status
from fastapi.encoders import jsonable_encoder
from fastapi.responses import JSONResponse

from ...common.schemas.request import BaseRequest
from .method.get_service_list import get_service_list

router = APIRouter(
    prefix='/v1/service',
    tags=['Администрирование сервиса менеджера кластера (/v1/service/*)']
)


@router.post('/info/list/', summary='Получение списка информации о сервисах')
def service_info_list(req: BaseRequest) -> JSONResponse:
    return JSONResponse(
        status_code=status.HTTP_200_OK,
        content=jsonable_encoder(get_service_list(req))
    )
