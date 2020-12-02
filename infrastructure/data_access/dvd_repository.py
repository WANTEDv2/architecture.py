from domain.Cddvd import Cddvd
from domain_services.i_dvd_repository import IDvdRepository


class DvdRepository(IDvdRepository):
    def __init__(self):   # Сохранение в оперативной памяти
        self._db = {1: Cddvd(name="Фильм1", id=1),
                    2: Cddvd(name="Фильм2", id=2)}
        self._counter = len(self._db) + 1

    def create_or_update(self, cddvd: Cddvd) -> Cddvd:
        if not cddvd.id:
            cddvd.id = self._counter
            self._counter += 1
        self._db[cddvd.id] = cddvd
        return cddvd

    def remove(self, id: int) -> None:
        if id in self._db:
            del self._db[id]

    def all(self) -> list:
        return list(self._db.values())