from __future__ import annotations

from src.linked_list.linked_list_node import LinkedListNode
from typing import Any, List


class LinkedList:
    def __init__(self, initial: Any = None) -> None:
        self.head = None
        self.tail = None
        self.length = 0

        if initial:
            node = LinkedListNode(initial)

            self.head = node
            self.tail = node
            self.length = 1

    def is_empty(self) -> bool:
        return self.head is None

    def get_length(self) -> int:
        return self.length

    def append(self, value: Any) -> LinkedList:
        node = LinkedListNode(value)

        if not self.head:
            self.head = node
            self.tail = node
        else:
            self.tail.next = node
            self.tail = node
        self.length += 1

        return self

    def prepend(self, value: Any) -> LinkedList:
        node = LinkedListNode(value)

        if not self.head:
            self.head = node
            self.tail = node
        else:
            node.next = self.head
            self.head = node
        self.length += 1

        return self

    def from_array(self, array: List[Any]) -> LinkedList:
        for value in array:
            self.append(value)

        return self

    def to_array(self) -> List[Any]:
        values = []

        current = self.head

        while current is not None:
            values.append(current.value)
            current = current.next

        return values

    def __str__(self, separator: str = " -> ") -> str:
        values = [str(value) for value in self.to_array()]

        return f"{separator}".join(values)

    def delete(self, value: Any) -> LinkedListNode | None:
        current_node = self.head
        # deleted_node = None

        if current_node and current_node.value == value:
            deleted_node = current_node
            self.head = current_node.next
            if self.head is None:
                self.tail = None
            # current_node = None
            self.length -= 1
            return deleted_node

        prev_node = None
        while current_node and current_node.value != value:
            prev_node = current_node
            current_node = current_node.next

        if current_node is None:
            return None

        deleted_node = current_node
        prev_node.next = current_node.next
        if current_node == self.tail:
            self.tail = prev_node
        # current_node = None
        self.length -= 1
        return deleted_node

    def insert_at(self, index: int, value: Any) -> LinkedList:
        if index < 0 or index > self.length:
            raise IndexError("Index should be >= 0 and <= list length.")

        if index == 0:
            self.prepend(value)
        elif index == self.length:
            self.append(value)
        else:
            prev_node = self._find_node_by_index(index - 1)
            new_node = LinkedListNode(value)

            new_node.next = prev_node.next
            prev_node.next = new_node

            self.length += 1
        return self

    def _find_node_by_index(self, index: int) -> LinkedListNode:
        current_node = self.head

        for i in range(index):
            current_node = current_node.next

        return current_node
