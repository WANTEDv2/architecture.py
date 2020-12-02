class Cddvd:
    def __init__(self, name: str, id: int = None):
        self._name = name
        self._id = id

    @property
    def name(self) -> str:
        return self._name

    @name.setter
    def name(self, value: str) -> None:
        self._name = value

    @property
    def id(self) -> int:
        return self._id

    @id.setter
    def id(self, value: id) -> None:
        self._id = value
