from __future__ import annotations

from typing import Optional, Any

from .binary_tree_node import BinaryTreeNode


class BinarySearchTree:
    def __init__(self, root: Optional[BinaryTreeNode] = None) -> None:
        self._root = root

    @property
    def root(self) -> Optional[BinaryTreeNode]:
        return self._root

    def insert(self, key: Any) -> BinarySearchTree:
        self._root = self._insert(self.root, key)
        return self

    def _insert(self, root: BinaryTreeNode, key: Any) -> BinaryTreeNode:
        if not root:
            return BinaryTreeNode(key)
        if key < root.value:
            root.left = self._insert(root.left, key)
        elif key > root.value:
            root.right = self._insert(root.right, key)

        return root
