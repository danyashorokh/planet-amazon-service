import uvicorn
from fastapi import FastAPI
from omegaconf import OmegaConf

from src.containers.containers import AppContainer
from src.routes.routers import router as app_router
from src.routes import planet as planet_routes

PORT = 1024


def create_app() -> FastAPI:
    container = AppContainer()
    cfg = OmegaConf.load('config/config.yml')
    container.config.from_dict(cfg)
    container.wire([planet_routes])

    app = FastAPI()
    set_routers(app)
    return app


def set_routers(app: FastAPI):
    app.include_router(app_router, prefix='/planet', tags=['planet'])


if __name__ == '__main__':
    app = create_app()
    uvicorn.run(app, port=PORT, host='0.0.0.0')
