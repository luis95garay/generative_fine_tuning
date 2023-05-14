from fastapi import FastAPI

# from routes import segmentation, wall_painting
from routes import pokemon


def route_registry(app: FastAPI):
    # app.include_router(wall_painting.router)
    # app.include_router(segmentation.router)
    app.include_router(pokemon.router)
