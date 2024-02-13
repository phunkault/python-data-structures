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


# Search
def test_search_in_empty_tree_returns_none(bst):
    # Act and Assert
    assert not bst.search(2)


def test_search_existing_node_returns_node(bst):
    # Arrange
    bst.insert(4).insert(3).insert(5)

    # Act and Assert
    assert bst.search(3).value == 3


def test_search_non_existing_node_returns_none(bst):
    # Arrange
    bst.insert(4).insert(3).insert(5)

    # Act and Assert
    assert not bst.search(7)


# Delete
def test_delete_leaf_node(bst):
    # Arrange
    bst.insert(10).insert(5).insert(15).insert(3).insert(7)

    # Act
    bst.delete(3)

    # Assert
    assert not bst.search(3)
    assert not bst.root.left.left
    assert bst.root.left.right.value == 7


def test_delete_node_with_one_child(bst):
    # Arrange
    bst.insert(10).insert(5).insert(15).insert(3).insert(8).insert(17)

    # Act
    bst.delete(15)

    # Assert
    assert not bst.search(15)
    assert bst.search(17).value == 17
    assert bst.root.right.value == 17


def test_delete_node_with_two_children(bst):
    # Arrange
    bst.insert(20).insert(5).insert(30).insert(3).insert(7).insert(29).insert(31)

    # Act
    bst.delete(30)

    # Assert
    assert not bst.search(30)
    assert bst.root.value == 20
    assert bst.root.right.value == 31
    assert bst.root.right.left.value == 29


def test_delete_root_node(bst):
    # Arrange
    bst.insert(10).insert(5).insert(15).insert(3).insert(7).insert(12).insert(18)

    # Act
    bst.delete(10)

    # Assert
    assert not bst.search(10)
    assert bst.root.value == 12
    assert bst.root.right.value == 15
    assert bst.root.right.right.value == 18


def test_delete_nonexistent_node(bst):
    # Arrange
    bst.insert(10).insert(5).insert(15).insert(3).insert(7)

    # Act
    bst.delete(20)

    # Assert
    assert bst.root.value == 10
    assert bst.root.left.value == 5
    assert bst.root.right.value == 15
    assert bst.root.left.left.value == 3
    assert bst.root.left.right.value == 7


# Traverse preorder
def test_traverse_preorder_empty_tree(bst):
    # Act and Assert
    assert bst.traverse_preorder() == []


def test_traverse_preorder_non_empty_tree(bst):
    # Arrange
    bst.insert(10).insert(5).insert(15).insert(3).insert(7)

    # Act and Assert
    assert bst.traverse_preorder() == [10, 5, 3, 7, 15]


# Traverse inorder
def test_traverse_inorder_empty_tree(bst):
    # Act and Assert
    assert bst.traverse_inorder() == []


def test_traverse_inorder_non_empty_tree(bst):
    # Arrange
    bst.insert(10).insert(5).insert(15).insert(3).insert(7)

    # Act and Assert
    assert bst.traverse_inorder() == [3, 5, 7, 10, 15]


# Traverse postorder
def test_traverse_postorder_empty_tree(bst):
    # Act and Assert
    assert bst.traverse_postorder() == []


def test_traverse_postorder_non_empty_tree(bst):
    # Arrange
    bst.insert(10).insert(5).insert(15).insert(3).insert(7)

    # Act and Assert
    assert bst.traverse_postorder() == [3, 7, 5, 15, 10]


# Find min
def find_min_in_empty_tree_returns_none(bst):
    # Act and Assert
    assert not bst.find_min()


def find_min_in_non_empty_tree_returns_min_node_value(bst):
    # Arrange
    bst.insert(10).insert(5).insert(15).insert(3).insert(7)

    # Act and Assert
    assert bst.find_min() == 3


# Find max
def find_max_in_empty_tree_returns_none(bst):
    # Act and Assert
    assert not bst.find_min()


def find_max_in_non_empty_tree_returns_max_node_value(bst):
    # Arrange
    bst.insert(10).insert(5).insert(15).insert(3).insert(7)

    # Act and Assert
    assert bst.find_max() == 15


# Stringify
def test_str_empty_tree(bst):
    # Act and Assert:
    assert str(bst) == "[]"


def test_str_non_empty_tree(bst):
    # Arrange
    bst.insert(10).insert(5).insert(15).insert(3).insert(7)

    # Act and Assert
    assert str(bst) == "[10, 5, 3, 7, 15]"
