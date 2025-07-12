from pydantic import BaseModel

from src.core.models import Transaction


class TransactionResponse(BaseModel):
    transactions: list[Transaction]
