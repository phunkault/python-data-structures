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


# Insert
def test_avl_tree_insertion(avl_tree):
    # Act
    avl_tree.insert(10).insert(5).insert(15)

    # Assert
    assert avl_tree.root.value == 10
    assert avl_tree.root.height == 2

    assert avl_tree.root.left.value == 5
    assert avl_tree.root.left.height == 1

    assert avl_tree.root.right.value == 15
    assert avl_tree.root.right.height == 1


def test_avl_tree_left_rotation(avl_tree):
    # Arrange
    avl_tree.insert(10).insert(15).insert(20)

    assert avl_tree.root.value == 15
    assert avl_tree.root.height == 2

    assert avl_tree.root.left.value == 10
    assert avl_tree.root.left.height == 1

    assert avl_tree.root.right.value == 20
    assert avl_tree.root.right.height == 1

    assert avl_tree._balance_factor(avl_tree.root) == 0
    assert avl_tree._balance_factor(avl_tree.root.left) == 0
    assert avl_tree._balance_factor(avl_tree.root.right) == 0


def test_avl_tree_right_rotation(avl_tree):
    # Arrange
    avl_tree.insert(20).insert(15).insert(10)

    # Assert
    assert avl_tree.root.value == 15
    assert avl_tree.root.left.value == 10
    assert avl_tree.root.right.value == 20


def test_avl_tree_double_rotation(avl_tree):
    # Arrange
    avl_tree.insert(10).insert(5).insert(20).insert(15)

    # Assert
    assert avl_tree.root.value == 10
    assert avl_tree.root.left.value == 5
    assert avl_tree.root.right.value == 20
    assert avl_tree.root.right.left.value == 15


# Delete
def test_avl_tree_delete_leaf(avl_tree):
    # Arrange
    avl_tree.insert(10).insert(5).insert(15)

    # Act
    avl_tree.delete(5)

    # Assert
    assert avl_tree.root.value == 10
    assert not avl_tree.root.left
    assert avl_tree.root.right.value == 15


def test_avl_tree_delete_node_with_one_child(avl_tree):
    # Arrange
    avl_tree.insert(10).insert(5).insert(15).insert(12)

    # Act
    avl_tree.delete(15)

    # Assert
    assert avl_tree.root.value == 10
    assert avl_tree.root.left.value == 5
    assert avl_tree.root.right.value == 12
    assert not avl_tree.root.right.right


def test_avl_tree_delete_node_with_two_children(avl_tree):
    # Arrange
    avl_tree.insert(10).insert(5).insert(15).insert(12).insert(17)

    # Act
    avl_tree.delete(15)

    # Assert
    assert avl_tree.root.value == 10
    assert avl_tree.root.left.value == 5
    assert avl_tree.root.right.value == 17
    assert avl_tree.root.right.left.value == 12


def test_avl_tree_delete_root(avl_tree):
    # Arrange
    avl_tree.insert(10).insert(5).insert(15)

    # Act
    avl_tree.delete(10)

    # Assert
    assert avl_tree.root.value == 15
    assert avl_tree.root.left.value == 5
    assert avl_tree.root.right is None
