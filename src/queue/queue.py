from typing import Any

from src.linked_list.linked_list import LinkedList


class Queue:
    def __init__(self) -> None:
        self._list: LinkedList = LinkedList()

    def __str__(self) -> str:
        return str(self._list)

    @property
    def size(self) -> int:
        return self._list.length

    @property
    def is_empty(self):
        return self._list.is_empty

    def enqueue(self, value: Any):
        self._list.prepend(value)
