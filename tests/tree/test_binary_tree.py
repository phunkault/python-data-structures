import pytest

from src.tree.binary_tree import BinaryTree


# Arrange
@pytest.fixture()
def binary_tree():
    return BinaryTree()


# Initial state
def test_initial_state(binary_tree):
    # Assert
    assert binary_tree
    assert not binary_tree.root
