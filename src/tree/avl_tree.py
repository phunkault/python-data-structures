from typing import Optional

from src.tree.binary_search_tree import BinarySearchTree
from .avl_tree_node import AVLTreeNode


class AVLTree(BinarySearchTree):
    def __init__(self, root: Optional[AVLTreeNode] = None) -> None:
        super().__init__(root)

    @staticmethod
    def get_height(node: Optional[AVLTreeNode]) -> int:
        return 0 if not node else node.height
