from typing import Optional

from .binary_tree_node import BinaryTreeNode


class BinarySearchTree:
    def __init__(self, root: Optional[BinaryTreeNode] = None) -> None:
        self.root = root
