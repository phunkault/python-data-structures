from __future__ import annotations

from typing import Any, List

from src.doubly_linked_list.doubly_linked_list_node import DoublyLinkedListNode
from src.doubly_linked_list.doubly_linked_list import DoublyLinkedList


DEFAULT_CAPACITY = 3


class NodeData:
    def __init__(self, key: Any, value: Any) -> None:
        self.key = key
        self.value = value


class MFUCache:
    def __init__(self, capacity: int = DEFAULT_CAPACITY) -> None:
        self._capacity = capacity
        self._size: int = 0
        self._max_freq: int = 1
        self._key_node_map: dict[Any, DoublyLinkedListNode] = {}
        self._key_freq_map: dict[Any, int] = {}
        self._freq_list_map: dict[int, DoublyLinkedList] = {}
        self._buckets: DoublyLinkedList = DoublyLinkedList()
        self._add_first_bucket()

    def _add_first_bucket(self):
        # bucket is a key-value pair – {frequency: DLL}
        first_freq_list = DoublyLinkedList()
        first_bucket = {self.max_freq: first_freq_list}
        self._buckets.append(first_bucket)
        self._freq_list_map[self.max_freq] = first_freq_list

    @property
    def size(self) -> int:
        return self._size

    @property
    def capacity(self) -> int:
        return self._capacity

    @property
    def max_freq(self) -> int:
        return self._max_freq

    def _delete_mfu_node(self) -> None:
        mfu_node_freq_list = self._buckets.tail.data[self._max_freq]

        mfu_node = mfu_node_freq_list.delete_head()

        del self._key_node_map[mfu_node.data.key]
        del self._key_freq_map[mfu_node.data.key]

        # update max_freq if mfu_bucket becomes empty
        if mfu_node_freq_list.is_empty:
            # delete the reference of mfu_node_freq_list first
            del self._freq_list_map[self._max_freq]
            # get previous max frequency, means the previous bucket frequency
            prev_max_freq = next(iter(self._buckets.tail.prev.data))
            # override max frequency
            self._max_freq = prev_max_freq
            # delete the current max frequency bucket
            self._buckets.delete_tail()

        self._size -= 1

    def _update_frequency(self, key: Any) -> None:
        node = self._key_node_map[key]
        node_data = NodeData(node.data.key, node.data.value)

        old_freq = self._key_freq_map[key]

        old_freq_list = self._freq_list_map[old_freq]
        old_freq_list.delete_by_ref(node)

        new_freq = old_freq + 1

        try:
            new_freq_list = self._freq_list_map[new_freq]
        except KeyError:
            # if there is no new_freq_list we must create it
            new_freq_list = DoublyLinkedList()
            self._freq_list_map[new_freq] = new_freq_list

            # and add a new bucket to buckets
            new_bucket = {new_freq: new_freq_list}
            self._buckets.append(new_bucket)

        # add node to a new freq_list
        new_freq_list.append(node_data)

        # override node's references
        self._key_node_map[key] = new_freq_list.tail
        self._key_freq_map[key] = new_freq

        # if new_freq > current max frequency, means we must override it
        if new_freq > self._max_freq:
            self._max_freq = new_freq

    def put(self, key: Any, value: Any) -> MFUCache:
        if key in self._key_node_map:
            # override value
            node = self._key_node_map[key]
            node.data.value = value
            # update frequency
            self._update_frequency(key)

            return self

        # MFUCache is loaded, means we should delete the MFU
        if self._size == self.capacity:
            self._delete_mfu_node()

        # new nodes always go to the first bucket (with frequency 1)
        new_node_data = NodeData(key, value)

        freq_list = self._freq_list_map[1]
        freq_list.append(new_node_data)

        # add node's references
        self._key_freq_map[key] = 1
        self._key_node_map[key] = freq_list.tail

        self._size += 1

        return self

    def get(self, key: Any) -> Any:
        # key doesn't exist
        if key not in self._key_node_map:
            return None

        node = self._key_node_map[key]
        value = node.data.value
        # update frequency
        self._update_frequency(key)

        return value

    def to_array(self) -> List[Any]:
        array = []
        for bucket in self._buckets:
            freq_list = list(bucket.data.values())[0]
            for node in freq_list:
                array.append(node.data.key)
        return array
