from __future__ import annotations

from typing import Any, Optional


from src.doubly_linked_list.doubly_linked_list import DoublyLinkedList
from src.doubly_linked_list.doubly_linked_list_node import DoublyLinkedListNode


DEFAULT_CAPACITY = 3


class NodeData:
    def __init__(self, key: Any, value: Any) -> None:
        self.key = key
        self.value = value

    def __str__(self):
        return f"({self.key}, {self.value})"


class LFUCache:
    def __init__(self, capacity: int = DEFAULT_CAPACITY) -> None:
        self._capacity = capacity
        self._size: int = 0
        self._min_freq: int = 1
        self._node_map: dict[Any, DoublyLinkedListNode] = {}
        self._freq_map: dict[Any, int] = {}
        self._buckets: dict[int, DoublyLinkedList] = {
            self._min_freq: DoublyLinkedList()
        }

    @property
    def capacity(self) -> int:
        return self._capacity

    @property
    def size(self) -> int:
        return self._size

    def _delete_lfu(self):
        bucket = self._buckets[self._min_freq]

        deleted_node = bucket.delete_head()

        del self._node_map[deleted_node.data.key]

        del self._freq_map[deleted_node.data.key]

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

        if old_bucket.length == 0 and old_freq == self._min_freq:
            self._min_freq += 1

    def put(self, key: Any, value: Any) -> LFUCache:
        if self.size == self.capacity:
            # delete LFU
            self._delete_lfu()

        if key in self._node_map:
            # renew value
            node = self._node_map[key]
            node.data.value = value
            # update frequency
            self._update_frequency(key)

            return self

        else:
            # add new node
            node_data = NodeData(key, value)

            bucket = self._buckets[1]
            bucket.append(node_data)

            self._freq_map[key] = self._min_freq

            self._node_map[key] = bucket.tail

            self._size += 1

            self._min_freq = 1

            return self

    def get(self, key: Any) -> Optional[Any]:
        if key not in self._node_map:
            return None

        node = self._node_map[key]
        value = node.data.value

        # update frequency
        self._update_frequency(key)

        return value

    def __str__(self):
        string = "Cache:\n"
        for bucket in self._buckets:
            freq_str = f"Freq {bucket}: {str(self._buckets[bucket])}\n"
            string += freq_str
        return string
