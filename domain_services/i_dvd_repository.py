from abc import ABC, abstractmethod

from domain.Cddvd import Cddvd


class IDvdRepository(ABC):
    @abstractmethod
    def create_or_update(self, cddvd: Cddvd) -> Cddvd:  # Возвращает диск
        pass

    @abstractmethod
    def remove(self, id: int) -> None:
        pass

    @abstractmethod
    def all(self) -> list:  # Возвращает список
        pass
