from typing import Any

from src.doubly_linked_list.doubly_linked_list_node import DoublyLinkedListNode
from src.doubly_linked_list.doubly_linked_list import DoublyLinkedList


DEFAULT_CAPACITY = 3


class MFUCache:
    def __init__(self) -> None:
        self._capacity: int = DEFAULT_CAPACITY
        self._size: int = 0
        self._max_freq: int = 1
        self._node_map: dict[Any, DoublyLinkedListNode]
        self._freq_map: dict[Any, int]
        self._buckets: dict[int, DoublyLinkedList]

    @property
    def size(self) -> int:
        return self._size

    @property
    def capacity(self) -> int:
        return self._capacity
