from __future__ import annotations

from typing import Optional, Any

from .binary_tree_node import BinaryTreeNode
from .binary_search_tree import BinarySearchTree


class AVLTree(BinarySearchTree):
    def __init__(self, root: Optional[BinaryTreeNode] = None) -> None:
        super().__init__(root)

    @staticmethod
    def _height(node: BinaryTreeNode) -> int:
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

    def _rotate_left(self, node: BinaryTreeNode) -> BinaryTreeNode:
        node_r = node.right
        node_r_l = node_r.left

        node_r.left = node
        node.right = node_r_l

        # Update heights
        node.height = 1 + max(
            self._height(node.left), self._height(node.right)
        )
        node_r.height = 1 + max(
            self._height(node_r.left), self._height(node_r.right)
        )

        return node_r

    def _rotate_right(self, node: BinaryTreeNode) -> BinaryTreeNode:
        node_l = node.left
        node_l_r = node_l.right

        node_l.right = node
        node.left = node_l_r

        # Update heights
        node.height = 1 + max(
            self._height(node.left), self._height(node.right)
        )
        node_l.height = 1 + max(
            self._height(node_l.left), self._height(node_l.right)
        )

        return node_l

    def delete(self, value: Any) -> AVLTree:
        self._root = self._delete(self.root, value)
        return self

    def _delete(
        self, root: BinaryTreeNode, value: Any
    ) -> Optional[BinaryTreeNode]:
        if not root:
            return None

        # Perform standard BST delete
        if value < root.value:
            root.left = self._delete(root.left, value)
        elif value > root.value:
            root.right = self._delete(root.right, value)
        else:
            # Node with only one child or no child
            if not root.left:
                return root.right
            elif not root.right:
                return root.left

            # Node with two children, get the inorder successor
            successor_value = BinarySearchTree._get_min_value(root.right)

            # Copy the inorder successor's value to this node
            root.value = successor_value

            # Delete the inorder successor
            root.right = self._delete(root.right, successor_value)

        # Update height of the current node
        root.height = 1 + max(
            self._height(root.left), self._height(root.right)
        )

        # Perform rotations if the tree is unbalanced
        return self._balance(root, value)
