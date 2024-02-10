from __future__ import annotations
from typing import Any, Optional


class BaseLinkedListNode:
    def __init__(
        self,
        data: Optional[Any] = None,
        next: Optional[BaseLinkedListNode] = None,
    ) -> None:
        self.data = data
        self.next = next

    def __str__(self) -> str:
        return f"{self.data}"
