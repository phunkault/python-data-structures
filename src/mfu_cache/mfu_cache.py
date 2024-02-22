from __future__ import annotations

from typing import Any

from src.doubly_linked_list.doubly_linked_list_node import DoublyLinkedListNode
from src.doubly_linked_list.doubly_linked_list import DoublyLinkedList


DEFAULT_CAPACITY = 3


class NodeData:
    def __init__(self, key: Any, value: Any) -> None:
        self.key = key
        self.value = value

    def __str__(self) -> str:
        return f"{self.key}, {self.value}"


class MFUCache:
    def __init__(self) -> None:
        self._capacity: int = DEFAULT_CAPACITY
        self._size: int = 0
        self._max_freq: int = 1
        self._node_map: dict[Any, DoublyLinkedListNode] = {}
        self._freq_map: dict[Any, int] = {}
        self._buckets: dict[int, DoublyLinkedList] = {
            self._max_freq: DoublyLinkedList()
        }

    @property
    def size(self) -> int:
        return self._size

    @property
    def capacity(self) -> int:
        return self._capacity

    def _delete_mfu_node(self):
        mfu_node_bucket = self._buckets[self._max_freq]
        mfu_node = mfu_node_bucket.delete_tail()

        del self._node_map[mfu_node.data.key]
        del self._freq_map[mfu_node.data.key]

        self._size -= 1

    def put(self, key: Any, value: Any) -> MFUCache:
        if key in self._node_map:
            # renew value
            node = self._node_map[key]
            node.data.value = value
            # update frequency
            return self

        # MFUCache is loaded
        if self._size == self.capacity:
            # delete MFU
            self._delete_mfu_node()

        new_node_data = NodeData(key, value)

        self._freq_map[key] = 1

        bucket = self._buckets[1]
        bucket.append(new_node_data)

        self._node_map[key] = bucket.tail

        self._size += 1

        return self
