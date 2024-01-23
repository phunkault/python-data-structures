from __future__ import annotations

from src.linked_list.linked_list_node import LinkedListNode
from typing import Any, List, Optional


class LinkedList:
    def __init__(self) -> None:
        self._head: Optional[LinkedListNode] = None
        self._tail: Optional[LinkedListNode] = None
        self._length: int = 0

    @property
    def head(self) -> Optional[LinkedListNode]:
        return self._head

    @property
    def tail(self) -> Optional[LinkedListNode]:
        return self._tail

    @property
    def length(self) -> int:
        return self._length

    def is_empty(self) -> bool:
        return self.head is None

    def append(self, value: Any) -> LinkedList:
        node = LinkedListNode(value)

        if not self.head:
            self._head = node
            self._tail = node
        else:
            self.tail.next = node
            self._tail = node
        self._length += 1

        return self

    def prepend(self, value: Any) -> LinkedList:
        node = LinkedListNode(value)

        if not self.head:
            self._head = node
            self._tail = node
        else:
            node.next = self.head
            self._head = node
        self._length += 1

        return self

    def from_array(self, array: List[Any]) -> LinkedList:
        for value in array:
            self.append(value)

        return self

    def to_array(self) -> List[Any]:
        values = []
        current = self.head

        while current:
            values.append(current.value)
            current = current.next

        return values

    def __str__(self, separator: str = " -> ") -> str:
        values = [str(value) for value in self.to_array()]

        return f"{separator}".join(values)

    def delete(self, value: Any) -> Optional[LinkedListNode]:
        if not self.head:
            return None

        if self.head.value == value:
            deleted_node = self._delete_head_update_tail()
        else:
            current_node = self.head

            while current_node.next and current_node.next.value != value:
                current_node = current_node.next

            deleted_node = self._delete_node_update_tail(current_node)

        if deleted_node:
            deleted_node.next = None
            self._length -= 1

        return deleted_node

    def _delete_head_update_tail(self) -> LinkedListNode:
        deleted_node = self.head

        if deleted_node.next:
            self._head = deleted_node.next
        else:
            self._head = None
            self._tail = None

        return deleted_node

    def _delete_node_update_tail(
        self, prev_node: LinkedListNode
    ) -> LinkedListNode:
        deleted_node = None

        if prev_node.next:
            deleted_node = prev_node.next
            prev_node.next = deleted_node.next

            if not prev_node.next:
                self._tail = prev_node

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

            self._length += 1

        return self

    def _find_node_by_index(self, index: int) -> LinkedListNode:
        current_node = self.head

        for i in range(index):
            current_node = current_node.next

        return current_node
