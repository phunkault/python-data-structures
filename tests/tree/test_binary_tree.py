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
    # Act
    binary_tree.insert(1).insert(3).insert(2).insert(5).insert(4)

    # Assert
    assert binary_tree.root.value == 1
    assert binary_tree.root.left.value == 3
    assert binary_tree.root.right.value == 2
    assert binary_tree.root.left.left.value == 5
    assert binary_tree.root.left.right.value == 4


# Search
def test_search_in_empty_tree_returns_none(binary_tree):
    # Act and Assert
    assert not binary_tree.search(1)


def test_search_existing_node_returns_node(binary_tree):
    # Arrange
    binary_tree.insert(1).insert(3).insert(2)

    # Act and Assert
    assert binary_tree.search(3).value == 3


def test_search_non_existing_node_returns_none(binary_tree):
    # Arrange
    binary_tree.insert(1).insert(3).insert(2)

    # Act and Assert
    assert not binary_tree.search(4)


# Traverse_preorder
def traverse_preorder_empty_tree(binary_tree):
    # Assert
    assert binary_tree.traverse_preorder == []


def traverse_preorder_non_empty_tree(binary_tree):
    # Arrange
    binary_tree.insert(1).insert(3).insert(2).insert(5).insert(4)

    # Assert
    assert binary_tree.traverse_preorder == [1, 3, 2, 5, 4]
