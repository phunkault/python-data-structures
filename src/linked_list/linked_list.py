from __future__ import annotations
from typing import Any, Optional

from src.linked_list.linked_list_node import LinkedListNode
from src.shared.base_linked_list import BaseLinkedList


class LinkedList(BaseLinkedList):
    def append(self, data: Any) -> LinkedList:
        node = LinkedListNode(data)

        if not self.head:
            self._head = node
            self._tail = node
        else:
            self._tail.next = node
            self._tail = node

        self._length += 1

        return self

    def prepend(self, data: Any) -> LinkedList:
        node = LinkedListNode(data)

        if not self.head:
            self._head = node
            self._tail = node
        else:
            node.next = self.head
            self._head = node

        self._length += 1

        return self

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

    def delete(self, arg: Any) -> Optional[LinkedListNode]:
        if self._head is None:
            return None

        deleted_node = None
        prev_node = None

        for current_node in self:
            if self._is_match(current_node.data, arg):
                deleted_node = current_node
                break

            prev_node = current_node

        if deleted_node:
            self._delete_node_and_update_tail(deleted_node, prev_node)
            deleted_node.next = None
            self._length -= 1

        return deleted_node

    def _delete_node_and_update_tail(
        self, deleted_node: LinkedListNode, prev_node: Optional[LinkedListNode]
    ) -> None:
        if prev_node is None:
            self._head = deleted_node.next
        else:
            prev_node.next = deleted_node.next

        if deleted_node.next is None:
            self._tail = prev_node

    def delete_head(self) -> Optional[LinkedListNode]:
        if self.head is None:
            return None

        deleted_node = self.head

        if deleted_node.next:
            self._head = deleted_node.next
        else:
            self._head = None
            self._tail = None

        self._length -= 1

        return deleted_node

    def delete_tail(self) -> Optional[LinkedListNode]:
        if self.head is None:
            return None

        deleted_tail = self.tail

        # Linked list with one node.
        if self.head == self.tail:
            self._head = None
            self._tail = None
        else:
            # Linked list with multiple nodes.
            prev_node = None

            for current_node in self:
                if current_node.next:
                    prev_node = current_node
                else:
                    prev_node.next = None
                    self._tail = prev_node
                    break

        self._length -= 1

        return deleted_tail

    def reverse(self) -> LinkedList:
        if not self.head or not self.head.next:
            return self

        current_node = self.head
        prev_node = None

        while current_node:
            next_node = current_node.next
            current_node.next = prev_node

            prev_node = current_node
            current_node = next_node

        self._tail = self.head
        self._head = prev_node

        return self
