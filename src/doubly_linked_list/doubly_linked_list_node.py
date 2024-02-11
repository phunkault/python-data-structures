from __future__ import annotations
from typing import Optional
from src.shared.base_linked_list_node import BaseLinkedListNode


class DoublyLinkedListNode(BaseLinkedListNode):
    def __init__(
        self,
        data=None,
        next=None,
        prev: Optional[DoublyLinkedListNode] = None,
    ) -> None:
        super().__init__(data, next)
        self.prev = prev
