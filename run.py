from fastapi import FastAPI

from app.routers.default.handlers.classes import router as classes_router


def get_application() -> FastAPI:
    app = FastAPI()
    app.include_router(router=classes_router)
    return app


app = get_application()
