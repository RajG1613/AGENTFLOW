from contextlib import asynccontextmanager

from fastapi import FastAPI

from app.api.router import api_router
from app.core.lifecycle import startup, shutdown
from app.core.settings import settings


@asynccontextmanager
async def lifespan(app: FastAPI):
    await startup()
    try:
        yield
    finally:
        await shutdown()


app = FastAPI(
    title="AgentFlow",
    version="0.1.0",
    lifespan=lifespan,
)

app.include_router(api_router, prefix="/api")


@app.get("/")
async def root():
    return {
        "name": "AgentFlow",
        "status": "running",
        "version": settings.APP_VERSION,
    }