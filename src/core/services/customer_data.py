import uuid
import datetime
from os import remove

from src.core.models import TransactionCreate, Transaction, UserBalances, ItemCreate, Item
from src.core.ports.abstract_customer_data_repository import AbstractCustomerDataRepository


def calculate_total_cost(transaction_create: TransactionCreate) -> int:
    return sum(item.quantity * item.unit_cost for item in transaction_create.items)

def calculate_points_allocated(transaction_create: TransactionCreate) -> int:
    return sum(item.quantity * item.unit_cost * item.point_allocation_percentage // 100
               for item in transaction_create.items)

def transform_to_items(item_create_list: list[ItemCreate]) -> list[Item]:
    return [Item(**item_create.model_dump(), total_cost=(item_create.unit_cost * item_create.quantity))
            for item_create in item_create_list]


class CustomerDataService:
    def __init__(self, repository: AbstractCustomerDataRepository):
        self.repository = repository

    async def record_transaction(self, transaction_create: TransactionCreate) -> Transaction:
        transaction_create_dict = transaction_create.model_dump()
        del transaction_create_dict["items"]
        transaction = Transaction(**transaction_create_dict,
                                  tid=uuid.uuid4(),
                                  total_cost=calculate_total_cost(transaction_create),
                                  points_allocated=calculate_points_allocated(transaction_create),
                                  performed_at=datetime.datetime.now(),
                                  items=transform_to_items(transaction_create.items))
        try:
            await self.repository.record_transaction(transaction)
        except Exception as e:
            print(e)
            raise
        return transaction

    async def get_balances(self, user_id: uuid.UUID) -> UserBalances:
        balances = await self.repository.get_balance(user_id)
        return UserBalances(user_id=user_id, shops=balances)

    async def get_customer_transactions(self, user_id: uuid.UUID, offset: int  = 0, limit: int = 100) -> list[Transaction]:
        transactions = await self.repository.get_customer_transactions(user_id, offset, limit)
        return transactions
