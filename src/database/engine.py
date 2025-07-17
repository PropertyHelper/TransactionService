from sqlalchemy.ext.asyncio import create_async_engine, AsyncEngine, async_sessionmaker


def create_db_engine(db_url, echo=True) -> AsyncEngine:
    """
    Create async database engine for PostgreSQL.

    :param db_url: Database connection string (asyncpg format)
    :param echo: Enable SQL query logging

    :return Configured async SQLAlchemy engine

    Note:
        Engine should be created once and reused throughout application lifecycle
    """
    engine = create_async_engine(db_url, echo=echo)
    return engine


def create_db_session_factory(engine):
    """
    Create async session factory for database operations.

    :param engine: Configured async SQLAlchemy engine

    :return Async session maker for creating database sessions

    Note:
        expire_on_commit=False prevents lazy loading issues after commit
        Sessions should be used within async context managers
    """
    return async_sessionmaker(engine, expire_on_commit=False)
