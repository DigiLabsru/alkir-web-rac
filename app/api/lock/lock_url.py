from fastapi import APIRouter, status
from fastapi.encoders import jsonable_encoder
from fastapi.responses import JSONResponse

from ...common.schemas.request import BaseRequest
from .method.get_lock_list import get_lock_list

router = APIRouter(
    prefix='/v1/lock',
    tags=['Администрирование блокировок (/v1/lock/*)']
)


@router.post('/info/list/', summary='Получение списка блокировок')
def lock_info_list(req: BaseRequest) -> JSONResponse:
    return JSONResponse(
        status_code=status.HTTP_200_OK,
        content=jsonable_encoder(get_lock_list(req))
    )
