from typing import Any

from src.doubly_linked_list.doubly_linked_list import DoublyLinkedList


class Dequeue:
    def __init__(self) -> None:
        self._list: DoublyLinkedList = DoublyLinkedList()

    def __str__(self) -> str:
        return str(self._list)

    @property
    def size(self) -> int:
        return self._list.length

    @property
    def is_empty(self) -> bool:
        return self._list.is_empty

    def add_front(self, value: Any):
        self._list.prepend(value)
