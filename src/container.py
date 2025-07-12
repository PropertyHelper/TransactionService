from dependency_injector import containers, providers

from src.database.adapters.sql_customer_data_repository import SQLCustomerDataRepository
from src.database.engine import create_db_engine, create_db_session_factory


class Container(containers.DeclarativeContainer):
    """
    Dependency Injection Container for UserDataService.

    Manages all application dependencies including database connections,
    repositories, and domain services. Follows singleton pattern to avoid duplicating essential objects.
    """

    config = providers.Configuration()

    engine = providers.Singleton(
        create_db_engine,
        db_url=config.db_url,
        echo=True
    )

    session_factory = providers.Singleton(
        create_db_session_factory,
        engine=engine
    )

    customer_data_repository = providers.Singleton(
        SQLCustomerDataRepository,
        session_factory=session_factory
    )
