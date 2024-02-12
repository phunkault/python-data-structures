import pytest

from src.tree.binary_tree import BinaryTree
from src.tree.binary_tree_node import BinaryTreeNode


# Arrange
@pytest.fixture()
def binary_tree():
    return BinaryTree()


# Initial state
def test_initial_state(binary_tree):
    # Assert
    assert binary_tree
    assert not binary_tree.root


# Insert
def test_insert_in_empty_tree(binary_tree):
    # Act
    binary_tree.insert(1)

    # Assert
    assert binary_tree.root.value == 1


def test_insert_in_non_empty_tree():
    # Arrange
    tree = BinaryTree(BinaryTreeNode(1))

    # Act
    tree.insert(2)
    tree.insert(3)
    tree.insert(4)

    # Assert
    assert tree.root.value == 1
    assert tree.root.left.value == 2
    assert tree.root.right.value == 3
    assert tree.root.left.left.value == 4
