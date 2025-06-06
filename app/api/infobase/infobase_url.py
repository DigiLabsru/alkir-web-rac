from fastapi import APIRouter, status
from fastapi.encoders import jsonable_encoder
from fastapi.responses import JSONResponse

from ...common.schemas.request import (
    BaseRequest,
    DeleteInfoBase,
    InfoBase,
    InfobaseProperty,
    InfoBaseSummaryUpdate,
    UpdateInfobaseProperty,
)
from .method.create_infobase import create_infobase
from .method.drop_infobase import drop_infobase
from .method.get_infobase_info import get_infobase_info
from .method.get_infobase_info_list import get_infobase_info_list
from .method.get_infobase_summary_info import get_infobase_summary_info
from .method.get_infobase_summary_list import get_infobase_summary_list
from .method.get_infobase_summary_update import get_infobase_summary_update
from .method.update_infobase import update_infobase

router = APIRouter(
    prefix='/v1/infobase',
    tags=['Администрирование информационной базой (/v1/infobase/*)']
)


@router.post('/info/', summary='Получение информации об информационной базе')
def infobase_info(req: InfoBase) -> JSONResponse:
    return JSONResponse(
        status_code=status.HTTP_200_OK,
        content=jsonable_encoder(get_infobase_info(req))
    )


@router.post('/info/list/', summary='Получение информации об информационных базах')
def infobase_list_info(req: BaseRequest) -> JSONResponse:
    return JSONResponse(
        status_code=status.HTTP_200_OK,
        content=jsonable_encoder(get_infobase_info_list(req))
    )


@router.post('/summary/list/', summary='Получение кратной информации обо всех информационных базах. Не требует авторизации в самой базе.')
def infobase_summary_list(req: BaseRequest) -> JSONResponse:
    return JSONResponse(
        status_code=status.HTTP_200_OK,
        content=jsonable_encoder(get_infobase_summary_list(req))
    )


@router.post('/summary/info/', summary='Получение кратной информации об информационной базе. Не требует авторизации в самой базе.')
def infobase_summary_info(req: InfoBase) -> JSONResponse:
    return JSONResponse(
        status_code=status.HTTP_200_OK,
        content=jsonable_encoder(get_infobase_summary_info(req))
    )


@router.post('/summary/update/', summary='Обновление кратной информации об информационной базе. Не требует авторизации в самой базе.')
def infobase_summary_update(req: InfoBaseSummaryUpdate) -> JSONResponse:
    return JSONResponse(
        status_code=status.HTTP_200_OK,
        content=jsonable_encoder(get_infobase_summary_update(req))
    )


@router.post('/create/', summary='Создание информационной базы.')
def infobase_create(req: InfobaseProperty) -> JSONResponse:
    return JSONResponse(
        status_code=status.HTTP_200_OK,
        content=jsonable_encoder(create_infobase(req))
    )


@router.post('/update/', summary='Обновление параметров информационной базы.')
def infobase_update(req: UpdateInfobaseProperty) -> JSONResponse:
    return JSONResponse(
        status_code=status.HTTP_200_OK,
        content=jsonable_encoder(update_infobase(req))
    )


@router.post('/drop/', summary='Удаление информационной базы.')
def infobase_drop(req: DeleteInfoBase) -> JSONResponse:
    return JSONResponse(
        status_code=status.HTTP_200_OK,
        content=jsonable_encoder(drop_infobase(req))
    )
