import uuid
from abc import ABC, abstractmethod


class AbstractShopDataRetriever(ABC):
    @abstractmethod
    async def get_customers(self, shop_id: uuid.UUID) -> list[uuid.UUID]:
        ...
