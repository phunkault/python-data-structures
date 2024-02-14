from typing import Optional

from src.tree.binary_search_tree import BinarySearchTree
from .avl_tree_node import AVLTreeNode


class AVLTree(BinarySearchTree):
    def __init__(self, root: Optional[AVLTreeNode] = None) -> None:
        super().__init__(root)

    @staticmethod
    def get_height(node: Optional[AVLTreeNode]) -> int:
        return 0 if not node else node.height

    def get_balance_factor(self, node: Optional[AVLTreeNode]) -> int:
        bf = self.get_height(node.left) - self.get_height(node.right)

        return 0 if not node else bf

    def get_min_node(self, node: Optional[AVLTreeNode]) -> AVLTreeNode:
        if not node or not node.left:
            return node
        else:
            return self.get_min_node(node.left)
