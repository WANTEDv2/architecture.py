from abc import ABC, abstractmethod


class GetAllDvd(ABC):
    @abstractmethod
    def exec(self) -> list:
        pass
