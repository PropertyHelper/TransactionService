from dependency_injector.wiring import inject, Provide

from src.container import Container
from src.core.ports.abstract_customer_data_repository import AbstractCustomerDataRepository
from src.core.services.customer_data import CustomerDataService


@inject
def get_customer_data_service(customer_repository: AbstractCustomerDataRepository = Provide[Container.customer_data_repository]) -> CustomerDataService:
    return CustomerDataService(repository=customer_repository)
