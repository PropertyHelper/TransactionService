import uuid

from src.core.ports.abstract_shop_data_retriever import AbstractShopDataRetriever
from src.database.adapters.sql_base_class import SQLBaseClass


class SQLShopDataRetriever(SQLBaseClass, AbstractShopDataRetriever):
    async def get_customers(self, shop_id: uuid.UUID) -> list[uuid.UUID]:
        pass
