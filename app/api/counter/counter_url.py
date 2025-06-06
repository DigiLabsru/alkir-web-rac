from fastapi import APIRouter, status
from fastapi.encoders import jsonable_encoder
from fastapi.responses import JSONResponse

from ...common.schemas.request import (
    BaseRequest,
    NewResourceConsumptionCounter,
    ResourceConsumptionCounterInfo,
    ResourceConsumptionCounterValueInfo,
    UpdateResourceConsumptionCounter,
)
from .method.clear_counter import clear_counter
from .method.create_new_counter import create_new_counter
from .method.get_counter_accumulated_list import get_counter_accumulated_list
from .method.get_counter_info import get_counter_info
from .method.get_counter_list import get_counter_list
from .method.get_counter_values_list import get_counter_values_list
from .method.remove_counter import remove_counter
from .method.update_counter import update_counter

router = APIRouter(
    prefix='/v1/counter',
    tags=['Администрирование счетчика (/v1/counter/*)']
)


@router.post('/info/one/', summary='Получение информации по счетчику')
def counter_info_one(req: ResourceConsumptionCounterInfo) -> JSONResponse:
    return JSONResponse(
        status_code=status.HTTP_200_OK,
        content=jsonable_encoder(get_counter_info(req))
    )


@router.post('/info/list/', summary='Получение списка информации по счетчикам')
def counter_info_list(req: BaseRequest) -> JSONResponse:
    return JSONResponse(
        status_code=status.HTTP_200_OK,
        content=jsonable_encoder(get_counter_list(req))
    )


@router.post('/info/values/', summary='Получение списка информации по счетчикам')
def counter_info_values(req: ResourceConsumptionCounterValueInfo) -> JSONResponse:
    return JSONResponse(
        status_code=status.HTTP_200_OK,
        content=jsonable_encoder(get_counter_values_list(req))
    )


@router.post('/info/accumulated_values/', summary='Получение списка информации по счетчикам')
def counter_info_accumulated_values(req: ResourceConsumptionCounterValueInfo) -> JSONResponse:
    return JSONResponse(
        status_code=status.HTTP_200_OK,
        content=jsonable_encoder(get_counter_accumulated_list(req))
    )


@router.post('/insert/', summary='Создание нового счетчика')
def counter_insert(req: NewResourceConsumptionCounter) -> JSONResponse:
    return JSONResponse(
        status_code=status.HTTP_200_OK,
        content=jsonable_encoder(create_new_counter(req))
    )


@router.post('/update/', summary='Обновление настроек счетчика')
def counter_update(req: UpdateResourceConsumptionCounter) -> JSONResponse:
    return JSONResponse(
        status_code=status.HTTP_200_OK,
        content=jsonable_encoder(update_counter(req))
    )


@router.post('/remove/', summary='Удаление счетчика')
def counter_remove(req: ResourceConsumptionCounterInfo) -> JSONResponse:
    return JSONResponse(
        status_code=status.HTTP_200_OK,
        content=jsonable_encoder(remove_counter(req))
    )


@router.post('/clear/', summary='Очистка счетчика')
def counter_clear(req: ResourceConsumptionCounterValueInfo) -> JSONResponse:
    return JSONResponse(
        status_code=status.HTTP_200_OK,
        content=jsonable_encoder(clear_counter(req))
    )
