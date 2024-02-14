import pytest

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
