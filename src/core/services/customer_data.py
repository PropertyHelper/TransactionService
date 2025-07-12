import uuid

from src.core.models import TransactionCreate, Transaction, UserBalances
from src.core.ports.abstract_customer_data_repository import AbstractCustomerDataRepository


class CustomerDataService:
    def __init__(self, repository: AbstractCustomerDataRepository):
        self.repository = repository

    async def record_transaction(self, transaction_create: TransactionCreate) -> Transaction:
        ...

    async def get_balances(self, user_id: uuid.UUID) -> UserBalances:
        ...

    async def get_customer_transactions(self, user_id: uuid.UUID, offset: int  = 0, limit: int = 100):
        ...
