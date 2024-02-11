from __future__ import annotations
from typing import Any, Optional

from src.shared.base_linked_list import BaseLinkedList
from .doubly_linked_list_node import DoublyLinkedListNode


class DoublyLinkedList(BaseLinkedList):
    def append(self, value: Any) -> DoublyLinkedList:
        new_node = DoublyLinkedListNode(value)

        if self._head is None:
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

        if self._head is None:
            self._head = new_node
            self._tail = new_node
        else:
            new_node.next = self._head
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
        elif index == self._length:
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
        if self._head is None:
            return None

        deleted_node: Optional[DoublyLinkedListNode] = None

        for current_node in self:
            if self._is_match(current_node.data, value):
                deleted_node = current_node
                break

        if deleted_node is None:
            return None

        if deleted_node.prev is not None:
            deleted_node.prev.next = deleted_node.next
        else:
            self._head = deleted_node.next

        if deleted_node.next is not None:
            deleted_node.next.prev = deleted_node.prev
        else:
            self._tail = deleted_node.prev

        deleted_node.prev = None
        deleted_node.next = None

        self._length -= 1

        return deleted_node

    def delete_head(self):
        if self._head is None:
            return None

        deleted_node = self._head

        if deleted_node.next:
            self._head = deleted_node.next
            self._head.prev = None
        else:
            self._head = None
            self._tail = None

        self._length -= 1

        return deleted_node

    def delete_tail(self) -> Optional[DoublyLinkedListNode]:
        if self._head is None:
            return None

        deleted_node = self._tail

        if self._head == self._tail:
            self._head = None
            self._tail = None
        else:
            self._tail = deleted_node.prev
            self._tail.next = None

        self._length -= 1

        return deleted_node

    def reverse(self) -> BaseLinkedList:
        if self._head is None or self._head.next is None:
            return self

        prev_node = None
        current_node = self._head

        while current_node is not None:
            next_node = current_node.next
            current_node.next = prev_node
            current_node.prev = next_node
            prev_node = current_node

            current_node = next_node

        self._tail = self._head
        self._head = prev_node

        return self
