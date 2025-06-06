import os
import sys
import threading
import traceback
from contextlib import asynccontextmanager

import jpype
from fastapi import FastAPI, Request, status
from fastapi.encoders import jsonable_encoder
from fastapi.exceptions import RequestValidationError, ResponseValidationError
from fastapi.middleware.cors import CORSMiddleware
from fastapi.openapi.docs import get_redoc_html
from fastapi.responses import HTMLResponse, JSONResponse
from fastapi.staticfiles import StaticFiles
from loguru import logger
from starlette.responses import FileResponse

from .api.agent import agent_url
from .api.cluster import cluster_url
from .api.connection import connection_url
from .api.counter import counter_url
from .api.infobase import infobase_url
from .api.limit import limit_url
from .api.lock import lock_url
from .api.manager import manager_url
from .api.process import process_url
from .api.profile import profile_url
from .api.rule import rule_url
from .api.server import server_url
from .api.service import service_url
from .api.session import session_url

logger.info('Старт приложения')


@asynccontextmanager
async def lifespan(app: FastAPI):
    # Запуск JVM при старте приложения
    jpype.startJVM(
        classpath=[
            f"{os.path.dirname(os.path.abspath(__file__))}/common/interface/ras/lib/*"
        ],
        convertStrings=True
    )
    # Основной класс работы с RAS
    app.state.AgentAdminConnectorFactory = jpype.JClass("com._1c.v8.ibis.admin.client.AgentAdminConnectorFactory")
    # Инициализация логера Java
    app.state.java_logger = jpype.JClass("java.util.logging.Logger").getLogger("")
    yield
    # Завершение JVM при остановке
    jpype.shutdownJVM()

app: FastAPI = FastAPI(
    title="alkir-web-rac",
    version="1.0",
    docs_url=None,
    redoc_url=None,
    openapi_url="/v1/openapi.json",
    root_path="",
    lifespan=lifespan
)
app.mount("/static", StaticFiles(directory="app/static"), name="static")
# app.mount("/site", StaticFiles(directory="app/web/site"), name="static")

app.add_middleware(
    CORSMiddleware,
    allow_origins=['*'],
    allow_credentials=True,
    allow_methods=['*'],
    allow_headers=['*'],
)

# добавление endpoint
app.include_router(agent_url.router)
app.include_router(cluster_url.router)
app.include_router(connection_url.router)
app.include_router(infobase_url.router)
app.include_router(manager_url.router)
app.include_router(process_url.router)
app.include_router(server_url.router)
app.include_router(service_url.router)
app.include_router(session_url.router)
app.include_router(limit_url.router)
app.include_router(rule_url.router)
app.include_router(counter_url.router)
app.include_router(profile_url.router)
app.include_router(lock_url.router)

logger.info('Приложение успешно запущено')

# Ссылка на документацию


@app.get("/v1/docs", include_in_schema=False)
async def redoc_html() -> HTMLResponse:
    return get_redoc_html(
        openapi_url="/v1/openapi.json",
        title=app.title + " - ReDoc",
        redoc_js_url="/static/redoc.standalone.js",
        redoc_favicon_url="/static/favicon.png",
        with_google_fonts=False
    )


@app.exception_handler(RequestValidationError)
async def request_validation_exception_handler(request: Request, exc: RequestValidationError):
    logger.error(f'Ошибка валидации запроса.\n{jsonable_encoder({"detail": str(exc.errors()), "body": str(exc.body)})}')
    return JSONResponse(
        status_code=status.HTTP_422_UNPROCESSABLE_ENTITY,
        content=jsonable_encoder({"detail": exc.errors(), "body": exc.body}),
    )

# Перехват ошибки валидации исходящего запроса


@app.exception_handler(ResponseValidationError)
async def response_validation_exception_handler(request: Request, exc: ResponseValidationError):
    logger.error(f'Ошибка валидации ответа.\n{jsonable_encoder({"detail": str(exc.errors())})}')
    return JSONResponse(
        status_code=status.HTTP_422_UNPROCESSABLE_ENTITY,
        content=jsonable_encoder({"detail": str(exc.errors())}),
    )


@app.get("/v1/thread-info", include_in_schema=False)
def thread_info():
    threads = threading.enumerate()
    logger.info(f"Active threads: {len(threads)}")
    for one_thread in threads:
        print(f"Thread {one_thread.name} ({one_thread.ident}): {one_thread.is_alive()}")
    return {"threads": len(threads)}


@app.get("/v1/thread-dump", include_in_schema=False)
def thread_dump():
    Thread = jpype.JClass("java.lang.Thread")
    sb = []
    for thread in Thread.getAllStackTraces().keySet():
        sb.append(f"Thread: {thread.getName()}\n")
        for trace in thread.getStackTrace():
            sb.append(f"\t{trace}\n")

    # Сохранение в файл
    with open("thread_dump.log", "w") as f:
        f.write("".join(sb))
    return FileResponse('thread_dump.log')


@app.get("/v1/debug/threads", include_in_schema=False)
async def thread_debug():
    stacks = {}
    for thread_id, frame in sys._current_frames().items():
        stacks[thread_id] = traceback.format_stack(frame)
    return stacks


@app.get("/v1/heals_check", include_in_schema=False)
def heals_check():
    Thread = jpype.JClass("java.lang.Thread")
    thread_count: int = len(Thread.getAllStackTraces().keySet())
    if thread_count > 300:
        logger.warning("Количество тредов Java более 300")
        # os._exit(1)
    else:
        logger.info(f"Количество тредов Java равно {thread_count}")
    return JSONResponse(
        status_code=status.HTTP_200_OK,
        content=jsonable_encoder({"status": "ok", "thread_count": thread_count}),
    )
