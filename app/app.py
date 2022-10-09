from fastapi import FastAPI

from app.routers.default.handlers.students import router as students_router
from app.routers.default.handlers.faculties import router as faculties_router
from app.routers.default.handlers.specializations import router as specializations_router

APP_ROUTERS = [students_router, faculties_router, specializations_router]


def get_application(on_startup=(), on_shutdown=()) -> FastAPI:
    app = FastAPI(on_startup=on_startup, on_shutdown=on_shutdown)
    for router in APP_ROUTERS:
        app.include_router(router=router)
    return app
