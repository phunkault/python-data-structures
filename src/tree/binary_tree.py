from typing import Optional, Any

from .binary_tree_node import BinaryTreeNode


class BinaryTree:
    def __init__(self, root: Optional[BinaryTreeNode] = None) -> None:
        self._root = root

    @staticmethod
    def _find_successor(node):
        while not node.left:
            node = node.left

        return node

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

    def _search(
        self, node: BinaryTreeNode, value: Any
    ) -> Optional[BinaryTreeNode]:
        if not node:
            return None  # Value not found
        if node.value == value:
            return node  # Value found
        elif value < node.value:
            return self._search(node.left, value)
        else:
            return self._search(node.right, value)

    def delete(self, value: Any) -> None:
        self._root = self._delete(self.root, value)

    def _delete(
        self, node: BinaryTreeNode, value: Any
    ) -> Optional[BinaryTreeNode]:
        if not node:
            return None

        if value < node.value:
            node.left = self._delete(node.left, value)
        elif value > node.value:
            node.right = self._delete(node.right, value)
        else:
            if not node.left:
                return node.right
            elif not node.right:
                return node.left

            successor = BinaryTree._find_successor(node.right)
            node = successor
            node.right = self._delete(node.right, successor.value)

        return node
