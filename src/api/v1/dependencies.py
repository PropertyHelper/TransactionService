from dependency_injector.wiring import inject, Provide

from src.container import Container
from src.core.ports.abstract_customer_data_repository import AbstractCustomerDataRepository
from src.core.ports.abstract_shop_data_retriever import AbstractShopDataRetriever
from src.core.services.customer_data import CustomerDataService
from src.core.services.shop_data import ShopDataService


@inject
def get_customer_data_service(customer_repository: AbstractCustomerDataRepository = Provide[Container.customer_data_repository]) -> CustomerDataService:
    """
    Use to get the customer data service.

    :param customer_repository: repository from container DI
    :return: customer data service
    Note:
        - used by fastapi DI system
        - uses DI to inject customer_repository in the building process
    """
    return CustomerDataService(repository=customer_repository)

@inject
def get_shop_data_service(shop_retriever: AbstractShopDataRetriever = Provide[Container.shop_data_retriever]) -> ShopDataService:
    """
    Use to get the shop data service.

    :param shop_retriever: retriever from container DI
    :return: shop data service
    Note:
        - used by fastapi DI system
        - uses DI to inject shop_retriever in the building process
    """
    return ShopDataService(retriever=shop_retriever)
