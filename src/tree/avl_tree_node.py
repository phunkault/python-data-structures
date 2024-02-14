from src.tree.binary_tree_node import BinaryTreeNode


class AVLTreeNode(BinaryTreeNode):
    def __init__(self, value=None, left=None, right=None) -> None:
        super().__init__(value, left, right)
        self.height: int = 1
