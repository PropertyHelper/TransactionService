import uuid

from sqlalchemy import select, and_
from sqlalchemy.orm import selectinload

from src.core.models import Transaction, Item
from src.core.ports.abstract_customer_data_repository import AbstractCustomerDataRepository
from src.database.adapters.sql_base_class import SQLBaseClass
from src.database.models import (
    Transaction as TransactionModel,
    TransactionItem as TransactionItemModel,
    Balance as BalanceModel
)

def model_transaction_to_domain(transaction_model: TransactionModel) -> Transaction:
    return Transaction(
        tid=transaction_model.transaction_id,
        user_id=transaction_model.user_id,
        shop_id=transaction_model.shop_id,
        total_cost=transaction_model.total_cost,
        points_allocated=transaction_model.points_allocated,
        performed_at=transaction_model.performed_at,
        items=[Item(
            item_id=item_model.item_id,
            quantity=item_model.quantity,
            unit_cost=item_model.unit_cost,
            point_allocation_percentage=item_model.point_allocation_percentage,
            total_cost=item_model.total_cost
        ) for item_model in transaction_model.items]
    )

class SQLCustomerDataRepository(SQLBaseClass, AbstractCustomerDataRepository):
    async def record_transaction(self, transaction: Transaction) -> None:
        async with self.get_session() as session:
            transaction_model = TransactionModel(
                transaction_id=transaction.tid,
                user_id=transaction.user_id,
                shop_id=transaction.shop_id,
                total_cost=transaction.total_cost,
                points_allocated=transaction.points_allocated,
                performed_at=transaction.performed_at,
                items=[TransactionItemModel(transaction_id=transaction.tid,
                                            item_id=item.item_id,
                                            quantity=item.quantity,
                                            unit_cost=item.unit_cost,
                                            point_allocation_percentage=item.point_allocation_percentage,
                                            total_cost=item.total_cost) for item in transaction.items]
            )
            select_balance = select(BalanceModel).where(and_(BalanceModel.user_id == transaction.user_id,
                                                             BalanceModel.shop_id == transaction.shop_id))
            result = await session.execute(select_balance)
            balance = result.scalar_one_or_none()
            if balance is None:
                # add a balance record
                balance = BalanceModel(user_id=transaction.user_id,
                                       shop_id=transaction.shop_id,
                                       balance=transaction.points_allocated)
            else:
                balance.balance += transaction.points_allocated
            session.add_all([transaction_model, balance])
            await session.commit()

    async def get_customer_transactions(self, customer_id: uuid.UUID, offset: int = 0, limit: int = 100) -> list[
        Transaction]:
        async with self.get_session() as session:
            stmt = select(TransactionModel).options(selectinload(TransactionModel.items)).where(TransactionModel.user_id == customer_id).offset(offset).limit(limit).order_by(TransactionModel.performed_at.desc())
            records = await session.execute(stmt)
            return [model_transaction_to_domain(transaction) for transaction in records.scalars().all()]

    async def get_balance(self, customer_id: uuid.UUID) -> list[tuple[uuid.UUID, int]]:
        async with self.get_session() as session:
            stmt = select(BalanceModel.shop_id, BalanceModel.balance).where(BalanceModel.user_id == customer_id)
            result = await session.execute(stmt)
            shop_balance = [record for record in result.all()]
            return shop_balance
