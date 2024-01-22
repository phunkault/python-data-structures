from __future__ import annotations

from src.linked_list.linked_list_node import LinkedListNode
from typing import Any


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
