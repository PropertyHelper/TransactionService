import uuid
import datetime

from pydantic import BaseModel

class ItemCreate(BaseModel):
    item_id: uuid.UUID
    quantity: int
    unit_cost: int
    point_allocation_percentage: int

class TransactionCreate(BaseModel):
    user_id: uuid.UUID
    shop_id: uuid.UUID
    items: list[ItemCreate]

class Item(ItemCreate):
    total_cost: int

class Transaction(TransactionCreate):
    tid: uuid.UUID
    total_cost: int
    points_allocated: int
    performed_at: datetime.datetime
    items: list[Item]

class UserBalances(BaseModel):
    user_id: uuid.UUID
    shops: list[tuple[uuid.UUID, int]]

class ShopUsers(BaseModel):
    shop_id: uuid.UUID
    users: list[uuid.UUID]
