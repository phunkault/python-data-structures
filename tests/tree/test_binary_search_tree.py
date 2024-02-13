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


# Insert
def test_insert_in_empty_tree(bst):
    # Act
    bst.insert(1)

    # Assert
    assert bst.root.value == 1
    assert not bst.root.left
    assert not bst.root.right


def test_insert_call_chain(bst):
    # Act
    bst.insert(8).insert(3).insert(10).insert(1).insert(6)

    # Assert
    assert bst.root.value == 8
    assert bst.root.left.value == 3
    assert bst.root.right.value == 10
    assert bst.root.left.left.value == 1
    assert bst.root.left.right.value == 6
