import uuid
from abc import ABC, abstractmethod

from src.core.models import Transaction


class AbstractCustomerDataRepository(ABC):
    @abstractmethod
    async def record_transaction(self, transaction: Transaction) -> None:
        ...

    @abstractmethod
    async def get_customer_transactions(self, customer_id: uuid.UUID, offset: int = 0, limit: int = 100) -> list[Transaction]:
        ...

    @abstractmethod
    async def get_balance(self, customer_id: uuid.UUID) -> list[tuple[uuid.UUID, int]]:
        ...
