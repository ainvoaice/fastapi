from fastapi.middleware.cors import CORSMiddleware
from contextlib import asynccontextmanager
from fastapi import FastAPI
from app.config import Settings
from app.utils.logger import logger_config
from app.db.database import engine
from app.api import rou

logger = logger_config(__name__)

@asynccontextmanager
async def lifespan(app: FastAPI):
    try:
        async with engine.begin() as conn: pass
        yield
    finally:
        await engine.dispose()

def create_app(settings: Settings):
    app = FastAPI(
        title=settings.PROJECT_NAME,
        version=settings.VERSION,
        docs_url="/",
        redoc_url="/redoc",
        lifespan=lifespan,
    )
    
    # app.state.settings = settings
    
    # CORS
    app.add_middleware(
        CORSMiddleware,
        allow_origins=settings.ALLOWED_ORIGINS,
        allow_credentials=True,
        allow_methods=["*"],
        allow_headers=["*"],
    )

    app.include_router(rou)
    
    return app
