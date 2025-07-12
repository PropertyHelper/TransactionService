from dependency_injector.wiring import inject, Provide

from src.container import Container
from src.core.ports.abstract_customer_data_repository import AbstractCustomerDataRepository
from src.core.ports.abstract_shop_data_retriever import AbstractShopDataRetriever
from src.core.services.customer_data import CustomerDataService
from src.core.services.shop_data import ShopDataService


@inject
def get_customer_data_service(customer_repository: AbstractCustomerDataRepository = Provide[Container.customer_data_repository]) -> CustomerDataService:
    return CustomerDataService(repository=customer_repository)

@inject
def get_shop_data_service(shop_retriever: AbstractShopDataRetriever = Provide[Container.shop_data_retriever]) -> ShopDataService:
    return ShopDataService(retriever=shop_retriever)
