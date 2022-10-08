from fastapi import FastAPI

from app.routers.default.handlers.classes import router as classes_router


def get_application(on_startup=(), on_shutdown=()) -> FastAPI:
    app = FastAPI(on_startup=on_startup, on_shutdown=on_shutdown)
    app.include_router(router=classes_router)
    return app
