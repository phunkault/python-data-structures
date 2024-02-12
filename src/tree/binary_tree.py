from __future__ import annotations

from typing import Optional, Any

from .binary_tree_node import BinaryTreeNode


class BinaryTree:
    def __init__(self, root: Optional[BinaryTreeNode] = None) -> None:
        self._root = root

    @staticmethod
    def _find_successor(node):
        while node.left:
            node = node.left

        return node

    @property
    def root(self) -> BinaryTreeNode:
        return self._root

    def insert(self, value: Any) -> BinaryTree:
        if not self.root:
            self._root = BinaryTreeNode(value)
        else:
            self._insert_recursive(self.root, value)
        return self

    def _insert_recursive(self, root: BinaryTreeNode, value: Any) -> None:
        if not root.left:
            root.left = BinaryTreeNode(value)
        elif not root.right:
            root.right = BinaryTreeNode(value)
        else:
            self._insert_recursive(root.left, value)

    def search(self, value: Any) -> Optional[BinaryTreeNode]:
        return self._search(self.root, value)

    def _search(
        self, node: BinaryTreeNode, value: Any
    ) -> Optional[BinaryTreeNode]:
        if not node:
            return None  # Value not found
        elif node.value == value:
            return node  # Value found
        left_size = self._search(node.left, value)
        if left_size:
            return left_size
        return self._search(node.right, value)
