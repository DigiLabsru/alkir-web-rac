from fastapi import APIRouter, status
from fastapi.encoders import jsonable_encoder
from fastapi.responses import JSONResponse

from ...common.schemas.request import (
    BaseRequest,
    NewResourceConsumptionLimit,
    ResourceConsumptionLimitInfo,
)
from .method.create_new_limit import create_new_limit
from .method.get_limit_info import get_limit_info
from .method.get_limit_list import get_limit_list
from .method.remove_limit import remove_limit
from .method.update_limit import update_limit

router = APIRouter(
    prefix='/v1/limit',
    tags=['Администрирование ограничений (/v1/limit/*)']
)


@router.post('/info/one/', summary='Получение информации по ограничению')
def limit_info_one(req: ResourceConsumptionLimitInfo) -> JSONResponse:
    return JSONResponse(
        status_code=status.HTTP_200_OK,
        content=jsonable_encoder(get_limit_info(req))
    )


@router.post('/info/list/', summary='Получение списка информации об ограничениях')
def limit_info_list(req: BaseRequest) -> JSONResponse:
    return JSONResponse(
        status_code=status.HTTP_200_OK,
        content=jsonable_encoder(get_limit_list(req))
    )


@router.post('/insert/', summary='Создание нового ограничения')
def limit_insert(req: NewResourceConsumptionLimit) -> JSONResponse:
    return JSONResponse(
        status_code=status.HTTP_200_OK,
        content=jsonable_encoder(create_new_limit(req))
    )


@router.post('/update/', summary='Обновление настроек ограничения')
def limit_update(req: NewResourceConsumptionLimit) -> JSONResponse:
    return JSONResponse(
        status_code=status.HTTP_200_OK,
        content=jsonable_encoder(update_limit(req))
    )


@router.post('/remove/', summary='Удаление ограничения')
def limit_remove(req: ResourceConsumptionLimitInfo) -> JSONResponse:
    return JSONResponse(
        status_code=status.HTTP_200_OK,
        content=jsonable_encoder(remove_limit(req))
    )
