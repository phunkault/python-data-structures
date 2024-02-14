import pytest

from src.tree.avl_tree_node import AVLTreeNode
from src.tree.avl_tree import AVLTree


# Arrange
@pytest.fixture()
def avl_tree():
    return AVLTree()


# Initial state
def test_avl_tree_initial_state(avl_tree):
    # Assert
    assert avl_tree
    assert not avl_tree.root


# Get height
def test_get_height_of_empty_tree(avl_tree):
    # Assert
    assert not avl_tree.get_height(avl_tree.root)


def test_get_height_of_tree_with_one_node():
    # Arrange
    tree = AVLTree(AVLTreeNode(1))

    # Assert
    assert tree.get_height(tree.root) == 1
