from src.linked_list.linked_list import LinkedList


class HashMap:
    _capacity: int = 10
    _buckets: list = [LinkedList() for _ in range(_capacity)]
    _size: int = 0

    @property
    def size(self) -> int:
        return self._size
