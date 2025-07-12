import datetime
import uuid

from sqlalchemy import ForeignKey
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column, relationship
from sqlalchemy import func


class Base(DeclarativeBase):
    """
    Base class for all SQLAlchemy models.

    Provides common functionality and metadata for all database entities.
    """
    pass

class Balance(Base):
    __tablename__ = "balances"
    user_id: Mapped[uuid.UUID] = mapped_column(primary_key=True)
    shop_id: Mapped[uuid.UUID] = mapped_column(primary_key=True)
    balance: Mapped[int]
    balance_created: Mapped[datetime.date] = mapped_column(default=func.now())

class Transaction(Base):
    __tablename__ = "transactions"
    transaction_id: Mapped[uuid.UUID] = mapped_column(primary_key=True)
    user_id: Mapped[uuid.UUID]
    shop_id: Mapped[uuid.UUID]
    total_cost: Mapped[int]
    points_allocated: Mapped[int]
    performed_at: Mapped[datetime.datetime] = mapped_column(default=func.now())
    items: Mapped[list["TransactionItem"]] = relationship("TransactionItem", back_populates="transaction")

class TransactionItem(Base):
    __tablename__ = "transaction_items"
    transaction_id: Mapped[uuid.UUID] = mapped_column(ForeignKey("transactions.transaction_id"), primary_key=True)
    item_id: Mapped[uuid.UUID] = mapped_column(primary_key=True)
    quantity: Mapped[int]
    unit_cost: Mapped[int]
    point_allocation_percentage: Mapped[int]
    total_cost: Mapped[int]
    transaction: Mapped["Transaction"] = relationship(back_populates="items")
