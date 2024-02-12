from typing import Any, Optional


class BinaryTreeNode:
    def __init__(self, value: Any = None) -> None:
        self.value = value
        self.left: Optional[BinaryTreeNode] = None
        self.right: Optional[BinaryTreeNode] = None
