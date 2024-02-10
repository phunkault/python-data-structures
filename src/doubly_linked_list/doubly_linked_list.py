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
        pass

    def insert_at(self, index: int, value: Any) -> DoublyLinkedList:
        pass

    def delete(self, value: Any) -> Optional[DoublyLinkedListNode]:
        pass

    def delete_head(self) -> Optional[DoublyLinkedListNode]:
        pass

    def delete_tail(self) -> Optional[DoublyLinkedListNode]:
        pass

    def reverse(self) -> BaseLinkedList:
        pass
