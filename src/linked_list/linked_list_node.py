from __future__ import annotations
from typing import Any


class LinkedListNode:
    def __init__(
        self, value: Any = None, next: LinkedListNode | None = None
    ) -> None:
        self.value = value
        self.next = next

    def __str__(self) -> str:
        return f"LinkedListNode({self.value})"
