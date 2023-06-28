from typing import List

from fastapi import FastAPI, Request, Depends
from fastapi.middleware import Middleware
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import JSONResponse

from api import router
from core.config import config
from core.exceptions import CustomException
from core.fastapi.dependencies import Logging
from core.fastapi.middlewares import (
    AuthenticationMiddleware,
    AuthBackend,
    SQLAlchemyMiddleware,
    ResponseLogMiddleware,
)


def init_routers(app_: FastAPI) -> None:
    app_.include_router(router)


def init_listeners(app_: FastAPI) -> None:
    # Exception handler
    @app_.exception_handler(CustomException)
    async def custom_exception_handler(request: Request, exc: CustomException):
        return JSONResponse(
            status_code=exc.code,
            content={"success": exc.success, "message": exc.message},
        )


def on_auth_error(request: Request, exc: Exception):
    status_code, success, message = 401, None, str(exc)
    if isinstance(exc, CustomException):
        status_code = int(exc.code)
        success = exc.success
        message = exc.message

    return JSONResponse(
        status_code=status_code,
        content={"success": success, "message": message},
    )


def make_middleware() -> List[Middleware]:
    middleware = [
        Middleware(
            CORSMiddleware,
            allow_origins=["*"],
            allow_credentials=True,
            allow_methods=["*"],
            allow_headers=["*"],
        ),
        Middleware(
            AuthenticationMiddleware,
            backend=AuthBackend(),
            on_error=on_auth_error,
        ),
        Middleware(SQLAlchemyMiddleware),
        Middleware(ResponseLogMiddleware),
    ]
    return middleware
 
def create_app() -> FastAPI:
    app_ = FastAPI(
        title="Assessment",
        description="August API",
        version="1.0.0",
        docs_url=None if config.ENV == "production" else "/assessment/docs",
        redoc_url=None if config.ENV == "production" else "/assessment/redoc",
        dependencies=[Depends(Logging)],
        middleware=make_middleware(),
    )
    init_routers(app_=app_)
    init_listeners(app_=app_)
    return app_


app = create_app()
