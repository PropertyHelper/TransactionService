import uuid
from abc import ABC, abstractmethod

from src.core.models import Transaction


class AbstractCustomerDataRepository(ABC):
    """
    Abstract interface for any customer data repository infrastructure.
    """
    @abstractmethod
    async def record_transaction(self, transaction: Transaction) -> None:
        """
        Save a transaction

        :param transaction: domain model
        :return: None
        """
        ...

    @abstractmethod
    async def get_customer_transactions(self, customer_id: uuid.UUID, offset: int = 0, limit: int = 100) -> list[Transaction]:
        """
        Get recent transactions

        :param customer_id: uid
        :param offset: skip number of records
        :param limit: limit the result
        :return: list of domain transactions
        """
        ...

    @abstractmethod
    async def get_balance(self, customer_id: uuid.UUID) -> list[tuple[uuid.UUID, int]]:
        """
        Get customer balances.

        :param customer_id: uid
        :return: list of tuples (customer id, number of points)
        """
        ...
