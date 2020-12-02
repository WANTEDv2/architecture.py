from abc import ABC, abstractmethod


class RemoveDvd(ABC):
    @abstractmethod
    def exec(self, id: int) -> dict:
        pass
