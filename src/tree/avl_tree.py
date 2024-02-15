from __future__ import annotations

from typing import Optional, Any

from .binary_tree_node import BinaryTreeNode
from .binary_search_tree import BinarySearchTree


class AVLTree(BinarySearchTree):
    def __init__(self, root: Optional[BinaryTreeNode] = None) -> None:
        super().__init__(root)

    def insert(self, value: Any) -> AVLTree:
        self._root = self._insert(self.root, value)
        return self

    def _insert(self, root: BinaryTreeNode, value: Any) -> BinaryTreeNode:
        # Perform the standard BST insert
        if not root:
            return BinaryTreeNode(value)
        if value < root.value:
            root.left = self._insert(root.left, value)
        elif value > root.value:
            root.right = self._insert(root.right, value)
        else:
            return root

        # Update height of the current node
        root.height = 1 + max(
            self._height(root.left), self._height(root.right)
        )

        balance = self._balance(root)

        # Perform rotations if the tree is unbalanced
        if balance > 1:
            if value < root.left.value:
                # Left-Left Case
                return self._rotate_right(root)
            else:
                # Left-Right Case
                root.left = self._rotate_left(root.left)
                return self._rotate_right(root)

        if balance < -1:
            if value > root.right.value:
                # Right-Right Case
                return self._rotate_left(root)
            else:
                # Right-Left Case
                root.right = self._rotate_right(root.right)
                return self._rotate_left(root)

        return root

    def _height(self, node: BinaryTreeNode) -> int:
        return node.height if node else 0

    def _balance(self, node: BinaryTreeNode) -> int:
        return (
            0
            if not node
            else (self._height(node.left) - self._height(node.right))
        )

    def _rotate_left(self, y: BinaryTreeNode) -> BinaryTreeNode:
        x = y.right
        T2 = x.left

        x.left = y
        y.right = T2

        # Update heights
        y.height = 1 + max(self._height(y.left), self._height(y.right))
        x.height = 1 + max(self._height(x.left), self._height(x.right))

        return x

    def _rotate_right(self, x: BinaryTreeNode) -> BinaryTreeNode:
        y = x.left
        T2 = y.right

        y.right = x
        x.left = T2

        # Update heights
        x.height = 1 + max(self._height(x.left), self._height(x.right))
        y.height = 1 + max(self._height(y.left), self._height(y.right))

        return y
