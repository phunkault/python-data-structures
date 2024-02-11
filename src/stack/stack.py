from __future__ import annotations
from typing import Any

from src.linked_list.linked_list import LinkedList


class Stack:
    def __init__(self):
        self._list: LinkedList = LinkedList()

    @property
    def length(self) -> int:
        return self._list.length

    @property
    def is_empty(self) -> bool:
        return self._list.is_empty

    def push(self, value: Any):
        self._list.append(value)

    def __str__(self) -> str:
        return str(self._list)
