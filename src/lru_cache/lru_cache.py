from __future__ import annotations

from typing import Any, Union

from src.doubly_linked_list.doubly_linked_list import DoublyLinkedList
from src.doubly_linked_list.doubly_linked_list_node import DoublyLinkedListNode


class LRUCache:
    def __init__(self, capacity: int) -> None:
        self.capacity = capacity
        self.list: DoublyLinkedList = DoublyLinkedList()
        self.node_map: dict = {}

    def put(self, data: Any) -> LRUCache:
        if data in self.node_map:
            self.list.delete(self.node_map[data])

        node = DoublyLinkedListNode(data)

        self.list.append(node)

        self.node_map[data] = node

        if self.list.length > self.capacity:
            self.list.delete_head()

            del self.node_map[data]

        return self

    def get(self, data: Any) -> Union[Any, int]:
        if data in self.node_map:
            node = self.node_map[data]

            self.list.delete_head()

            self.list.append(data)

            self.node_map[data] = node

            return node.data

        return -1
