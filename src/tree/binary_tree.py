from typing import Optional, Any

from .binary_tree_node import BinaryTreeNode


class BinaryTree:
    def __init__(self, root: Optional[BinaryTreeNode] = None) -> None:
        self._root = root

    @property
    def root(self) -> BinaryTreeNode:
        return self._root

    def insert(self, value: Any) -> None:
        self._root = self._insert(self.root, value=value)

    def _insert(self, node: BinaryTreeNode, value: Any) -> BinaryTreeNode:
        if not node:
            return BinaryTreeNode(value)
        if not node.left:
            node.left = self._insert(node.left, value)
        elif not node.right:
            node.right = self._insert(node.right, value)
        else:
            node.left = self._insert(node.left, value)
        return node

    def search(self, value: Any) -> Optional[BinaryTreeNode]:
        return self._search(self.root, value)

    def _search(self, node, value):
        if node is None:
            return None  # Value not found
        if node.value == value:
            return node  # Value found
        elif value < node.value:
            return self._search(node.left, value)
        else:
            return self._search(node.right, value)
