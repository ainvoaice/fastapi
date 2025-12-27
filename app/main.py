from fastapi.middleware.cors import CORSMiddleware
from contextlib import asynccontextmanager
from fastapi import FastAPI
from app.config import Settings
from app.utils.logger import logger_config
from app.db.database import init_db, close_db
from app.models.mini import User, Group

logger = logger_config(__name__)

@asynccontextmanager
async def lifespan(app: FastAPI):
    logger.info("Starting up application...")
    await init_db(app.state.settings)
    logger.info("Application startup complete")
    yield
    logger.info("Shutting down application...")
    await close_db()
    logger.info("Application shutdown complete")

def create_app(settings: Settings):
    app = FastAPI(
        title=settings.PROJECT_NAME,
        version=settings.VERSION,
        docs_url="/",
        redoc_url="/redoc",
        lifespan=lifespan,
    )
    
    app.state.settings = settings
    
    # CORS
    app.add_middleware(
        CORSMiddleware,
        allow_origins=settings.ALLOWED_ORIGINS,
        allow_credentials=True,
        allow_methods=["*"],
        allow_headers=["*"],
    )

    # Minimal example routes
    @app.get("/users")
    async def get_users():
        return [{"userid": "dummy", "username": "dummy"}]

    @app.get("/groups")
    async def get_groups():
        return [{"groupid": "dummy", "groupname": "dummy"}]
    
    return app
