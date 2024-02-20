from __future__ import annotations
from typing import Any, Optional

from src.shared.base_linked_list import BaseLinkedList
from .doubly_linked_list_node import DoublyLinkedListNode


class DoublyLinkedList(BaseLinkedList):
    def __init__(self):
        self._head: Optional[DoublyLinkedListNode] = None
        self._tail: Optional[DoublyLinkedListNode] = None
        self._length: int = 0

    @property
    def head(self) -> DoublyLinkedListNode:
        return self._head

    @property
    def tail(self) -> DoublyLinkedListNode:
        return self._tail

    @property
    def length(self) -> int:
        return self._length

    def append(self, value: Any) -> DoublyLinkedList:
        new_node = DoublyLinkedListNode(value)

        if not self.head:
            self._head = new_node
            self._tail = new_node
        else:
            self._tail.next = new_node
            new_node.prev = self._tail
            self._tail = new_node

        self._length += 1

        return self

    def prepend(self, value: Any) -> DoublyLinkedList:
        new_node = DoublyLinkedListNode(value)

        if not self.head:
            self._head = new_node
            self._tail = new_node
        else:
            new_node.next = self.head
            self._head.prev = new_node
            self._head = new_node

        self._length += 1

        return self

    def insert_at(self, index: int, value: Any) -> DoublyLinkedList:
        is_invalid_index = index < 0 or index > self.length

        if is_invalid_index:
            raise ValueError("Index should be >= 0 and <= list length.")

        if index == 0:
            self.prepend(value)
        elif index == self.length:
            self.append(value)
        else:
            prev_node = self._find_node_by_index(index - 1)
            new_node = DoublyLinkedListNode(value)
            new_node.next = prev_node.next
            new_node.prev = prev_node
            prev_node.next = new_node

            self._length += 1

        return self

    def delete(self, value: Any) -> Optional[DoublyLinkedListNode]:
        if not self.head:
            return None

        deleted_node = None

        for current_node in self:
            if DoublyLinkedList._is_match(current_node.data, value):
                deleted_node = current_node
                break

        if not deleted_node:
            return None

        if deleted_node.prev:
            deleted_node.prev.next = deleted_node.next
        else:
            self._head = deleted_node.next

        if deleted_node.next:
            deleted_node.next.prev = deleted_node.prev
        else:
            self._tail = deleted_node.prev

        deleted_node.prev = None
        deleted_node.next = None

        self._length -= 1

        return deleted_node

    def delete_by_ref(self, node: DoublyLinkedListNode) -> None:
        if node.prev:
            node.prev.next = node.next
        else:
            self._head = node.next

        if node.next:
            node.next.prev = node.prev
        else:
            self._tail = node.prev

        self._length -= 1

    def delete_head(self) -> Optional[DoublyLinkedListNode]:
        if not self.head:
            return None

        deleted_node = self.head

        if deleted_node.next:
            self._head = deleted_node.next
            self._head.prev = None
        else:
            self._head = None
            self._tail = None

        self._length -= 1

        return deleted_node

    def delete_tail(self) -> Optional[DoublyLinkedListNode]:
        if not self.head:
            return None

        deleted_node = self.tail

        if self.head == self.tail:
            self._head = None
            self._tail = None
        else:
            self._tail = deleted_node.prev
            self._tail.next = None

        self._length -= 1

        return deleted_node

    def reverse(self) -> DoublyLinkedList:
        if not self.head or not self.head.next:
            return self

        prev_node = None
        current_node = self.head

        while current_node:
            next_node = current_node.next
            current_node.next = prev_node
            current_node.prev = next_node
            prev_node = current_node

            current_node = next_node

        self._tail = self.head
        self._head = prev_node

        return self
