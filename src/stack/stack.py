from __future__ import annotations
from typing import Any, Optional

from src.linked_list.linked_list import LinkedList


class Stack:
    def __init__(self) -> None:
        self._list: LinkedList = LinkedList()

    def __str__(self) -> str:
        return str(self._list)

    @property
    def length(self) -> int:
        return self._list.length

    @property
    def is_empty(self) -> bool:
        return self._list.is_empty

    def push(self, value: Any) -> None:
        self._list.append(value)

    def pop(self) -> Optional[Any]:
        popped_node = self._list.delete_tail()
        return popped_node.data if popped_node else None

    def clear(self) -> None:
        self._list.clear()
