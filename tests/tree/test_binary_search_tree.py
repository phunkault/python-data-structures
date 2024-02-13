import pytest

from src.tree.binary_search_tree import BinarySearchTree


# Arrange
@pytest.fixture()
def bst():
    return BinarySearchTree()


# Initial state
def test_initial_state_is_correct(bst):
    # Assert
    assert bst
    assert not bst.root
