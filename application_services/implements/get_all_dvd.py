from application_services.get_all_dvd import GetAllDvd
from application_services.implements.dvd_mapper import DvdMapper
from domain_services.i_dvd_repository import IDvdRepository


class GetAllDvd(GetAllDvd):
    def __init__(self, repository: IDvdRepository):
        self.repository = repository

    def exec(self) -> list:
        cddvd = self.repository.all()
        return list(map(lambda b: DvdMapper.domain_to_dto(b), cddvd))
