from domain.Cddvd import Cddvd


class DvdMapper:
    @staticmethod
    def dto_to_domain(dto: dict) -> Cddvd:
        return Cddvd(id=None if "id" not in dto else dto['id'], name=dto['name'])

    @staticmethod
    def domain_to_dto(book: Cddvd) -> dict:
        return {"id": book.id, "name": book.name}
