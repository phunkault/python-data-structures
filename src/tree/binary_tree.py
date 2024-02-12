from __future__ import annotations

from typing import Any, Optional


class BinaryTreeNode:
    def __init__(
        self,
        value: Any = None,
        left: Optional[BinaryTreeNode] = None,
        right: Optional[BinaryTreeNode] = None,
    ) -> None:
        self.value = value
        self.left = left
        self.right = right

    def __str__(self):
        return f"{self.value}"
