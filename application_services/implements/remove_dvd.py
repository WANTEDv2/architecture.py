from application_services.Remove_dvd import RemoveDvd
from domain_services.i_dvd_repository import IDvdRepository


class RemoveDvd(RemoveDvd):
    def __init__(self, repository: IDvdRepository):
        self.repository = repository

    def exec(self, id: int) -> None:
        self.repository.remove(id)