import uuid
from abc import ABC, abstractmethod


class AbstractShopDataRetriever(ABC):
    """
    Abstract interface for any shop data retriever infrastructure.
    """
    @abstractmethod
    async def get_customers(self, shop_id: uuid.UUID) -> list[uuid.UUID]:
        """
        Get customers of a shop

        :param shop_id: uid
        :return: list of uids of customers with open balances at a shop
        """
        ...
