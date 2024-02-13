from __future__ import annotations

from typing import Optional, Any

from .binary_tree_node import BinaryTreeNode


class BinarySearchTree:
    def __init__(self, root: Optional[BinaryTreeNode] = None) -> None:
        self._root = root

    @staticmethod
    def _get_min_value(root: BinaryTreeNode) -> Optional[Any]:
        while root.left:
            root = root.left
        return root.value

    @property
    def root(self) -> Optional[BinaryTreeNode]:
        return self._root

    def __str__(self) -> str:
        return str(self.traverse_preorder())

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

    def delete(self, value: Any) -> BinarySearchTree:
        self._root = self._delete(self.root, value)
        return self

    def _delete(
        self, root: BinaryTreeNode, value: Any
    ) -> Optional[BinaryTreeNode]:
        if not root:
            return None

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

            # Node with two children
            root.value = BinarySearchTree._get_min_value(root.right)
            # Delete the inorder successor
            root.right = self._delete(root.right, root.value)

        return root

    def traverse_preorder(self) -> list[Any]:
        result = []
        self._traverse_preorder(self.root, result)
        return result

    def _traverse_preorder(
        self, root: BinaryTreeNode, result: list[Any]
    ) -> None:
        if root:
            result.append(root.value)
            self._traverse_preorder(root.left, result)
            self._traverse_preorder(root.right, result)

    def traverse_inorder(self) -> list[Any]:
        result = []
        self._traverse_inorder(self.root, result)
        return result

    def _traverse_inorder(
        self, root: BinaryTreeNode, result: list[Any]
    ) -> None:
        if root:
            self._traverse_inorder(root.left, result)
            result.append(root.value)
            self._traverse_inorder(root.right, result)

    def traverse_postorder(self) -> list[Any]:
        result = []
        self._traverse_postorder(self.root, result)
        return result

    def _traverse_postorder(
        self, root: BinaryTreeNode, result: list[Any]
    ) -> None:
        if root:
            self._traverse_postorder(root.left, result)
            self._traverse_postorder(root.right, result)
            result.append(root.value)

    def find_min(self) -> Optional[Any]:
        if not self.root:
            return None
        return BinarySearchTree._get_min_value(self.root)

    def find_max(self) -> Optional[Any]:
        if not self.root:
            return None
        max_val_node = None
        while self.root.right:
            max_val_node = self.root.right
        return max_val_node.value
