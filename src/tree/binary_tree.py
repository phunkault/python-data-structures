from .binary_tree_node import BinaryTreeNode


class BinaryTree:
    def __init__(self, root: BinaryTreeNode = None) -> None:
        self._root = root

    @property
    def root(self):
        return self._root
