from typing import List, Any


class Heap:
    """Base Heap class"""

    pass

    def __init__(self) -> None:
        self._container: List[Any] = []
        self._size: int = 0
        self._is_empty: bool = True

    @property
    def container(self) -> List[Any]:
        return self._container

    @property
    def size(self) -> int:
        return self._size

    @property
    def is_empty(self) -> bool:
        return True if self._size == 0 else False

    def peek(self) -> Any:
        return self._container[0] if not self._is_empty else None

    def push(self):
        pass

    def pop(self):
        pass

    def replace(self):
        pass

    def remove(self):
        pass

    def merge(self):
        pass

    def find(self):
        pass

    def __str__(self):
        pass
