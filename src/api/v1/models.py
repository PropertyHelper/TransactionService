from pydantic import BaseModel

from src.core.models import Transaction


class TransactionResponse(BaseModel):
    """
    Encapsulate transaction API response.

    Object encapsulates list for potential extendability.
    """
    transactions: list[Transaction]
