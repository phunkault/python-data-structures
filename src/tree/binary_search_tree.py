from __future__ import annotations

from typing import Optional, Any

from .binary_tree_node import BinaryTreeNode


class BinarySearchTree:
    def __init__(self, root: Optional[BinaryTreeNode] = None) -> None:
        self._root = root

    @property
    def root(self) -> Optional[BinaryTreeNode]:
        return self._root

    def insert(self, value: Any) -> BinarySearchTree:
        self._root = self._insert(self.root, value)
        return self

    def _insert(self, root: BinaryTreeNode, value: Any) -> BinaryTreeNode:
        if not root:
            return BinaryTreeNode(value)
        if value < root.value:
            root.left = self._insert(root.left, value)
        elif value > root.value:
            root.right = self._insert(root.right, value)

        return root

    def search(self, value: Any) -> Optional[BinaryTreeNode]:
        return self._search(self.root, value)

    def _search(
        self, root: BinaryTreeNode, value: Any
    ) -> Optional[BinaryTreeNode]:
        if not root:
            return None
        if root.value == value:
            return root

        if value < root.value:
            return self._search(root.left, value)
        else:
            return self._search(root.right, value)
