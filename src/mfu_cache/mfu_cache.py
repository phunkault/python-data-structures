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

    def __str__(self) -> str:
        string = ""
        for bucket in self._buckets:
            freq_str = f"Freq {bucket}: {str(self._buckets[bucket])}\n"
            string += freq_str
        return string

    @property
    def size(self) -> int:
        return self._size

    @property
    def capacity(self) -> int:
        return self._capacity

    def _delete_mfu_node(self) -> None:
        mfu_node_bucket = self._buckets[self._max_freq]
        mfu_node = mfu_node_bucket.delete_tail()

        del self._node_map[mfu_node.data.key]
        del self._freq_map[mfu_node.data.key]

        self._size -= 1

    def _update_frequency(self, key: Any) -> None:
        node = self._node_map[key]
        node_data = NodeData(node.data.key, node.data.value)

        old_freq = self._freq_map[key]

        old_bucket = self._buckets[old_freq]
        old_bucket.delete_by_ref(node)

        new_freq = old_freq + 1

        try:
            new_bucket = self._buckets[new_freq]
        except KeyError:
            new_bucket = DoublyLinkedList()
            self._buckets[new_freq] = new_bucket

        new_bucket.append(node_data)

        self._node_map[key] = new_bucket.tail
        self._freq_map[key] = new_freq

        if new_freq > self._max_freq:
            self._max_freq = new_freq

    def put(self, key: Any, value: Any) -> MFUCache:
        if key in self._node_map:
            # renew value
            node = self._node_map[key]
            node.data.value = value
            # update frequency
            self._update_frequency(key)

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

    def get(self, key: Any) -> Any:
        # key doesn't exist
        if key not in self._node_map:
            return None

        node = self._node_map[key]
        value = node.data.value
        # update frequency
        self._update_frequency(key)

        return value
