import uuid

from src.core.models import ShopUsers
from src.core.ports.abstract_shop_data_retriever import AbstractShopDataRetriever


class ShopDataService:
    """
    A domain service responsible for operations with shop data.
    """
    def __init__(self, retriever: AbstractShopDataRetriever):
        """
        Initiate with a repository.

        :param retriever: object implementing AbstractShopDataRetriever
        """
        self.retriever = retriever

    async def get_customers(self, shop_id: uuid.UUID) -> ShopUsers:
        """
        Get customers of a particular shop
        :param shop_id: uid
        :return: model encapsulating customer ids.
        """
        customers = await self.retriever.get_customers(shop_id=shop_id)
        shop_users = ShopUsers(shop_id=shop_id, users=customers)
        return shop_users