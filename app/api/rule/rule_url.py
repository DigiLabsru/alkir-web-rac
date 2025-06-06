from fastapi import APIRouter, status
from fastapi.encoders import jsonable_encoder
from fastapi.responses import JSONResponse

from ...common.schemas.request import (
    ApplyAssignmentRules,
    AssigmentRuleInfo,
    NewAssigmentRuleInfo,
    WorkingServerInfo,
)
from .method.apply_rule import apply_rule
from .method.create_new_rule import create_new_rule
from .method.get_rule_info import get_rule_info
from .method.get_rule_list import get_rule_list
from .method.remove_rule import remove_rule
from .method.update_rule import update_rule

router = APIRouter(
    prefix='/v1/assigment_rule',
    tags=['Администрирование рабочего сервера (/v1/assigment_rule/*)']
)


@router.post('/info/one/', summary='Получение информации о assigment rule')
def assigment_rule_info_one(req: AssigmentRuleInfo) -> JSONResponse:
    return JSONResponse(
        status_code=status.HTTP_200_OK,
        content=jsonable_encoder(get_rule_info(req))
    )


@router.post('/info/list/', summary='Получение списка информации о assigment rules')
def assigment_rule_info_list(req: WorkingServerInfo) -> JSONResponse:
    return JSONResponse(
        status_code=status.HTTP_200_OK,
        content=jsonable_encoder(get_rule_list(req))
    )


@router.post('/apply/', summary='Применение требований назначения')
def rule_apply(req: ApplyAssignmentRules) -> JSONResponse:
    return JSONResponse(
        status_code=status.HTTP_200_OK,
        content=jsonable_encoder(apply_rule(req))
    )


@router.post('/insert/', summary='Создание нового требования назначения')
def rule_insert(req: NewAssigmentRuleInfo) -> JSONResponse:
    return JSONResponse(
        status_code=status.HTTP_200_OK,
        content=jsonable_encoder(create_new_rule(req))
    )


@router.post('/update/', summary='Обновление настроек требования назначения')
def rule_update(req: NewAssigmentRuleInfo) -> JSONResponse:
    return JSONResponse(
        status_code=status.HTTP_200_OK,
        content=jsonable_encoder(update_rule(req))
    )


@router.post('/remove/', summary='Удаление требования назначения')
def rule_remove(req: AssigmentRuleInfo) -> JSONResponse:
    return JSONResponse(
        status_code=status.HTTP_200_OK,
        content=jsonable_encoder(remove_rule(req))
    )
