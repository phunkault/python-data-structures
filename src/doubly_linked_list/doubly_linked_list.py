from typing import Any, Optional

from src.shared.base_linked_list import BaseLinkedList
from .doubly_linked_list_node import DoublyLinkedListNode


class DoublyLinkedList(BaseLinkedList):
    def append(self, value: Any) -> BaseLinkedList:
        pass

    def prepend(self, value: Any) -> BaseLinkedList:
        pass

    def insert_at(self, index: int, value: Any) -> BaseLinkedList:
        pass

    def delete(self, value: Any) -> Optional[DoublyLinkedListNode]:
        pass

    def delete_head(self) -> Optional[DoublyLinkedListNode]:
        pass

    def delete_tail(self) -> Optional[DoublyLinkedListNode]:
        pass

    def reverse(self) -> BaseLinkedList:
        pass
