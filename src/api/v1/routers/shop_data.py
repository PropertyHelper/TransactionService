import uuid

from fastapi import APIRouter, Depends

from src.api.v1.dependencies import get_shop_data_service
from src.core.models import ShopUsers
from src.core.services.shop_data import ShopDataService

router = APIRouter(prefix="/shopdata")


@router.get("/{shop_id}")
async def get_customers(shop_id: uuid.UUID, shop_data_service: ShopDataService = Depends(lambda: get_shop_data_service())) -> ShopUsers:
    """
    Get customers of a shop.

    :param shop_id: uid
    :param shop_data_service: got from DI
    :return: domain model
    """
    customers = await shop_data_service.get_customers(shop_id)
    return customers
