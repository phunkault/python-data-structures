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
    assert not binary_tree.root.left
    assert not binary_tree.root.right


def test_insert_chain(binary_tree):
    binary_tree.insert(1).insert(3).insert(2).insert(5).insert(4)

    assert binary_tree.root.value == 1
    assert binary_tree.root.left.value == 3
    assert binary_tree.root.right.value == 2
    assert binary_tree.root.left.left.value == 5
    assert binary_tree.root.left.right.value == 4
