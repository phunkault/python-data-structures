from __future__ import annotations
from typing import Any


class LinkedListNode:
    def __init__(
        self, data: Any = None, next: LinkedListNode | None = None
    ) -> None:
        self.data = data
        self.next = next

    def __str__(self) -> str:
        return f"LinkedListNode({self.data})"
