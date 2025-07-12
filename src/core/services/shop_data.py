import uuid

from src.core.models import ShopUsers
from src.core.ports.abstract_shop_data_retriever import AbstractShopDataRetriever


class ShopDataService:
    def __init__(self, retriever: AbstractShopDataRetriever):
        self.retriever = retriever

    async def get_customers(self, shop_id: uuid.UUID) -> ShopUsers:
        customers = await self.retriever.get_customers(shop_id=shop_id)
        shop_users = ShopUsers(shop_id=shop_id, users=customers)
        return shop_users