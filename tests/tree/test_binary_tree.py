import pytest

from src.tree.binary_tree import BinaryTree
from src.tree.binary_tree_node import BinaryTreeNode


# Arrange
@pytest.fixture()
def binary_tree():
    return BinaryTree()


@pytest.fixture()
def sample_binary_tree():
    tree = BinaryTree()
    tree.insert(5)
    tree.insert(3)
    tree.insert(7)
    tree.insert(2)
    tree.insert(4)
    tree.insert(6)
    tree.insert(8)
    tree.delete(7)
    return tree


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


# Search
def test_search_in_empty_tree_returns_none(binary_tree):
    # Act and assert
    result = binary_tree.search(1)
    assert not result


def test_search_for_existing_node_returns_node(binary_tree):
    # Arrange
    binary_tree.insert(1)

    # Act and assert
    result = binary_tree.search(1)
    assert result.value == 1


def test_search_for_non_existing_node_returns_none(binary_tree):
    # Arrange
    binary_tree.insert(1)
    binary_tree.insert(2)
    binary_tree.insert(3)

    # Act and assert
    result = binary_tree.search(4)
    assert not result


# Delete
def test_delete_leaf_node(binary_tree):
    # Arrange
    binary_tree.insert(5)

    # Act
    binary_tree.delete(5)

    # Assert
    assert not binary_tree.search(5)
    # assert tree.inorder_traversal() == []


def test_delete_node_with_one_child(binary_tree):
    # Arrange
    binary_tree.insert(5)
    binary_tree.insert(3)

    # Actr
    binary_tree.delete(5)

    # Assert
    assert not binary_tree.search(5)
    assert binary_tree.root.value == 3
    # assert tree.inorder_traversal() == [3]


def test_delete_node_with_two_children(sample_binary_tree):
    # Act
    sample_binary_tree.delete(7)

    # Assert
    assert not sample_binary_tree.search(7)
    # assert tree.inorder_traversal() == [2, 3, 4, 5, 6, 8]


def test_delete_root_node(sample_binary_tree):
    # Act
    sample_binary_tree.delete(5)

    # Assert
    assert not sample_binary_tree.search(5)
    # assert tree.inorder_traversal() == [2, 3, 4, 6, 7, 8]


def test_delete_nonexistent_node(sample_binary_tree):
    # Act
    sample_binary_tree.delete(42)
    # assert tree.inorder_traversal() == [2, 3, 4, 5, 6, 7, 8]


def test_delete_empty_tree(binary_tree):
    # Actt
    binary_tree.delete(42)
    # assert tree.inorder_traversal() == []
