import uuid

from src.core.models import Transaction
from src.core.ports.abstract_customer_data_repository import AbstractCustomerDataRepository
from src.database.adapters.sql_base_class import SQLBaseClass


class SQLCustomerDataRepository(SQLBaseClass, AbstractCustomerDataRepository):
    async def record_transaction(self, transaction: Transaction) -> None:
        pass

    async def get_customer_transactions(self, customer_id: uuid.UUID, offset: int = 0, limit: int = 100) -> list[
        Transaction]:
        pass

    async def get_balance(self, customer_id: uuid.UUID) -> list[tuple[uuid.UUID, int]]:
        pass
