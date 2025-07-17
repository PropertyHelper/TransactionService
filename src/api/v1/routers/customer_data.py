import uuid

from fastapi import APIRouter, Depends

from src.api.v1.dependencies import get_customer_data_service
from src.api.v1.models import TransactionResponse
from src.core.models import TransactionCreate, Transaction, UserBalances
from src.core.services.customer_data import CustomerDataService

router = APIRouter(prefix="/userdata")

@router.post("/transaction")
async def record_transaction(transaction_create: TransactionCreate,
                       customer_data_service: CustomerDataService = Depends(lambda: get_customer_data_service())) -> Transaction:
    """
    Save a transaction API.

    :param transaction_create: object to create a transaciton
    :param customer_data_service: service embedded from DI system
    :return: Transaction Domain model
    """
    transaction = await customer_data_service.record_transaction(transaction_create)
    return transaction

@router.get("/{customer_id}")
async def get_customer_balance(customer_id: uuid.UUID,
                         customer_data_service: CustomerDataService = Depends(lambda: get_customer_data_service())) -> UserBalances:
    """
    Get customer balance data.

    :param customer_id: uid
    :param customer_data_service: service embedded from DI system
    :return: UserBalances model
    """
    balances = await customer_data_service.get_balances(customer_id)
    return balances

@router.get("/transactions/{customer_id}")
async def get_transactions(customer_id: uuid.UUID,
                           offset: int = 0,
                           limit: int = 100,
                         customer_data_service: CustomerDataService = Depends(lambda: get_customer_data_service())) -> TransactionResponse:
    """
    Get up to limit most recent transaction skipping offset of them.

    :param customer_id: uid
    :param offset: int to skip records
    :param limit: up to this number of transactions
    :param customer_data_service: service embedded from DI system
    :return: TransactionResponse model
    """
    transactions = await customer_data_service.get_customer_transactions(customer_id, offset=offset, limit=limit)
    return TransactionResponse(transactions=transactions)
