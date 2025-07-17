import uuid
import datetime

from pydantic import BaseModel

class ItemCreate(BaseModel):
    """
    Use to create a new item.
    """
    item_id: uuid.UUID
    quantity: int
    unit_cost: int
    point_allocation_percentage: int

class TransactionCreate(BaseModel):
    """
    Use to create a new transaction.
    """
    user_id: uuid.UUID
    shop_id: uuid.UUID
    items: list[ItemCreate]

class Item(ItemCreate):
    """
    Use to represent the item domain model
    """
    total_cost: int

class Transaction(TransactionCreate):
    """
    User to represent transaction domain model
    """
    tid: uuid.UUID
    total_cost: int
    points_allocated: int
    performed_at: datetime.datetime
    items: list[Item]

class UserBalances(BaseModel):
    """
    Use to represent customer's balances domain model
    """
    user_id: uuid.UUID
    shops: list[tuple[uuid.UUID, int]]

class ShopUsers(BaseModel):
    """
    User to represent customers of a particular shop.
    """
    shop_id: uuid.UUID
    users: list[uuid.UUID]
