from __future__ import annotations

from typing import Optional, Any

from .binary_tree_node import BinaryTreeNode
from .binary_search_tree import BinarySearchTree


class AVLTree(BinarySearchTree):
    def __init__(self, root: Optional[BinaryTreeNode] = None) -> None:
        super().__init__(root)

    def _height(self, node: BinaryTreeNode) -> int:
        return node.height if node else 0

    def _balance_factor(self, node: BinaryTreeNode) -> int:
        bf = self._height(node.left) - self._height(node.right)
        return 0 if not node else bf

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
        max_subtree_height = max(
            self._height(root.left), self._height(root.right)
        )
        root.height = 1 + max_subtree_height

        # Perform rotations if the tree is unbalanced
        new_root = self._balance(root, value)

        # Update the root after rotations
        if root != new_root:
            self._root = new_root

        return new_root

    def _balance(self, node: BinaryTreeNode, value: Any) -> BinaryTreeNode:
        balance = self._balance_factor(node)

        if balance > 1:
            if value < node.left.value:
                # Left-Left Case
                return self._rotate_right(node)
            else:
                # Left-Right Case
                node.left = self._rotate_left(node.left)
                return self._rotate_right(node)

        if balance < -1:
            if value > node.right.value:
                # Right-Right Case
                return self._rotate_left(node)
            else:
                # Right-Left Case
                node.right = self._rotate_right(node.right)
                return self._rotate_left(node)

        return node

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
