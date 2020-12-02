from abc import ABC, abstractmethod


class UpdateDvd(ABC):
    @abstractmethod
    def exec(self, cddvd_dto: dict) -> dict:
        pass
