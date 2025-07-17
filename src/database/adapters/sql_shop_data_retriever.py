import uuid

from sqlalchemy import select

from src.core.ports.abstract_shop_data_retriever import AbstractShopDataRetriever
from src.database.adapters.sql_base_class import SQLBaseClass
from src.database.models import Balance as BalanceModel


class SQLShopDataRetriever(SQLBaseClass, AbstractShopDataRetriever):
    """
    A retriver to interact with infrastructure.

    In our case, it interacts with PostgreSQL via SQLAlchemy.
    Implements the AbstractShopDataRetriever contract.
    Subclasses the SQLBaseClass to get basic things like getting a connection.
    """
    async def get_customers(self, shop_id: uuid.UUID) -> list[uuid.UUID]:
        """
        Get all customer ids for a selected shop.

        :param shop_id: uuid
        :return: list of customers who have balance in the shop
        """
        async with self.get_session() as session:
            stmt = select(BalanceModel.user_id).where(BalanceModel.shop_id == shop_id)
            result = await session.execute(stmt)
            customers = [customer for customer in result.scalars().all()]
            return customers
