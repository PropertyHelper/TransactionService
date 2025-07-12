from sqlalchemy.ext.asyncio import AsyncSession


class SQLBaseClass:
    def __init__(self, session_factory):
        """
        Initialize repository with session factory.

        Args:
            session_factory: Async session maker for database operations
        """
        self.session_factory = session_factory

    def get_session(self) -> AsyncSession:
        """
        Create new database session.

        Returns:
            Async database session for transaction management
        """
        return self.session_factory()
