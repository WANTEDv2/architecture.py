from abc import ABC, abstractmethod


class CreateDvd(ABC):   # Будет работать с репозиторием через интерфейс
    @abstractmethod
    def exec(self, cddvd_dto: dict) -> dict:   # Этот метод принимает dvd ДТО и возвращает dvd ДТО
        pass
