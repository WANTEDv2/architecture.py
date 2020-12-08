from application_services.CreateDvd import CreateDvd
from application_services.UpdateDvd import UpdateDvd
from application_services.implements.dvd_mapper import DvdMapper
from domain_services.i_dvd_repository import IDvdRepository


class CreateOrUpdateDvd (CreateDvd, UpdateDvd):   # Класс унаследовал итерфэйсы application_services
    def __init__(self, repository: IDvdRepository):
        self.repository = repository

    def exec(self, dvd_dto: dict) -> dict:   # Создание dvd
        cddvd = DvdMapper.dto_to_domain(dvd_dto)
        new_dvd = self.repository.create_or_update(cddvd)
        return DvdMapper.domain_to_dto(new_dvd)