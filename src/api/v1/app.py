from contextlib import asynccontextmanager

from fastapi import FastAPI

from src.container import Container
from src.database.models import Base



def build_app(container: Container) -> FastAPI:
    """
    Application factory that creates and configures FastAPI instance.

    Args:
        container: Configured dependency injection container

    Returns:
        Configured FastAPI application instance
    """

    @asynccontextmanager
    async def lifespan(app: FastAPI):
        """
        Application lifespan manager for startup/shutdown events.

        Startup: Initializes database schema and sets container reference
        Shutdown: Cleanup operations (handled automatically by context manager)
        """
        app.container = container
        engine = container.engine()
        async with engine.begin() as conn:
            await conn.run_sync(Base.metadata.create_all)
        yield

    app = FastAPI(lifespan=lifespan)
    container.wire(modules=["src.api.v1.routers.customer_data",
                            "src.api.v1.routers.shop_data"])
    return app
