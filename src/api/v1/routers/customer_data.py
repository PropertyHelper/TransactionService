import uuid

from fastapi import APIRouter, Depends, HTTPException

from src.api.v1.dependencies import get_customer_data_service
from src.api.v1.models import TransactionResponse
from src.core.models import TransactionCreate, Transaction, UserBalances
from src.core.services.customer_data import CustomerDataService

router = APIRouter(prefix="/userdata")

@router.post("/transaction")
async def record_transaction(transaction_create: TransactionCreate,
                       customer_data_service: CustomerDataService = Depends(lambda: get_customer_data_service())) -> Transaction:
    transaction = await customer_data_service.record_transaction(transaction_create)
    return transaction

@router.get("/{customer_id}")
async def get_customer_balance(customer_id: uuid.UUID,
                         customer_data_service: CustomerDataService = Depends(lambda: get_customer_data_service())) -> UserBalances:
    balances = await customer_data_service.get_balances(customer_id)
    return balances

@router.get("/transactions/{customer_id}")
async def get_transactions(customer_id: uuid.UUID,
                           offset: int = 0,
                           limit: int = 100,
                         customer_data_service: CustomerDataService = Depends(lambda: get_customer_data_service())) -> TransactionResponse:
    transactions = await customer_data_service.get_customer_transactions(customer_id, offset=offset, limit=limit)
    return TransactionResponse(transactions=transactions)
