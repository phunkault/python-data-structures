from __future__ import annotations

from src.linked_list.linked_list_node import LinkedListNode
from typing import Any, List


class LinkedList:
    def __init__(self, initial: Any = None) -> None:
        self.head = None
        self.tail = None
        self.size = 0

        if initial:
            node = LinkedListNode(initial)

            self.head = node
            self.tail = node
            self.size = 1

    def append(self, value: Any) -> LinkedList:
        node = LinkedListNode(value)

        if not self.head:
            self.head = node
            self.tail = node
        else:
            self.tail.next = node
            self.tail = node
        self.size += 1

        return self

    def prepend(self, value: Any) -> LinkedList:
        node = LinkedListNode(value)

        if not self.head:
            self.head = node
            self.tail = node
        else:
            node.next = self.head
            self.head = node
        self.size += 1

        return self

    def to_string(self, separator: str = " -> ") -> str:
        string = ""
        current = self.head
        while current:
            string += str(current)
            if current.next:
                string += separator
            current = current.next
        return string

    def from_array(self, array: List[Any]) -> LinkedList:
        for value in array:
            self.append(value)

        return self

    def delete_by_value(self, value: Any) -> LinkedListNode | None:
        current_node = self.head
        # deleted_node = None

        if current_node and current_node.value == value:
            deleted_node = current_node
            self.head = current_node.next
            if self.head is None:
                self.tail = None
            # current_node = None
            self.size -= 1
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
        self.size -= 1
        return deleted_node
