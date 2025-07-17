from contextlib import asynccontextmanager

from fastapi import FastAPI
from prometheus_fastapi_instrumentator import Instrumentator

from src.container import Container
from src.database.models import Base
from src.api.v1.routers.customer_data import router as customer_router
from src.api.v1.routers.shop_data import router as shop_router


def build_app(container: Container) -> FastAPI:
    """
    Application factory that creates and configures FastAPI instance.

    :param container: Configured dependency injection container
    :return Configured FastAPI application instance
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
    # setyp modules that will use container DI
    container.wire(modules=["src.api.v1.routers.customer_data",
                            "src.api.v1.routers.shop_data"])
    app.include_router(customer_router, tags=["Customer"])
    app.include_router(shop_router, tags=["Shop"])
    # setup metrics for prometheus
    Instrumentator(excluded_handlers=["/metrics"]).instrument(app).expose(app)
    return app
