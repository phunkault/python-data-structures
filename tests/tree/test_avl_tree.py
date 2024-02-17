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
    avl_tree.insert(10)
    avl_tree.insert(5)
    avl_tree.insert(15)

    # Assert
    assert avl_tree.root.value == 10
    assert avl_tree.root.left.value == 5
    assert avl_tree.root.right.value == 15
    assert avl_tree.root.height == 2
    assert avl_tree.root.left.height == 1
    assert avl_tree.root.right.height == 1


def test_avl_tree_left_rotation(avl_tree):
    avl_tree.insert(10)
    avl_tree.insert(15)
    avl_tree.insert(20)

    # The expected structure after left rotation
    #     15
    #    / \
    #   10  20

    # Check the root and its values
    assert avl_tree.root.value == 15
    # Check the left child
    assert avl_tree.root.left.value == 10
    # Check the right child
    assert avl_tree.root.right.value == 20

    # Check the height of the root
    assert avl_tree.root.height == 2
    # Check the height of the left child
    assert avl_tree.root.left.height == 1
    # Check the height of the right child
    assert avl_tree.root.right.height == 1

    # Check the balance factor of the root
    assert avl_tree._balance_factor(avl_tree.root) == 0
    # Check the balance factor of the left child
    assert avl_tree._balance_factor(avl_tree.root.left) == 0
    # Check the balance factor of the right child
    assert avl_tree._balance_factor(avl_tree.root.right) == 0


def test_avl_tree_right_rotation(avl_tree):
    avl_tree.insert(20)
    avl_tree.insert(15)
    avl_tree.insert(10)

    assert avl_tree.root.value == 15
    assert avl_tree.root.left.value == 10
    assert avl_tree.root.right.value == 20


def test_avl_tree_double_rotation(avl_tree):
    avl_tree.insert(10)
    avl_tree.insert(5)
    avl_tree.insert(20)
    avl_tree.insert(15)

    assert avl_tree.root.value == 10
    assert avl_tree.root.left.value == 5
    assert avl_tree.root.right.value == 20
    assert avl_tree.root.right.left.value == 15


# Delete
def test_avl_tree_delete_leaf(avl_tree):
    # Arrange
    avl_tree.insert(10)
    avl_tree.insert(5)
    avl_tree.insert(15)

    # Act
    avl_tree.delete(5)

    # Assert
    assert avl_tree.root.value == 10
    assert avl_tree.root.left is None
    assert avl_tree.root.right.value == 15


def test_avl_tree_delete_node_with_one_child(avl_tree):
    # Arrange
    avl_tree.insert(10)
    avl_tree.insert(5)
    avl_tree.insert(15)
    avl_tree.insert(12)

    # Act
    avl_tree.delete(15)

    # Assert
    assert avl_tree.root.value == 10
    assert avl_tree.root.left.value == 5
    assert avl_tree.root.right.value == 12
    assert avl_tree.root.right.right is None


def test_avl_tree_delete_node_with_two_children(avl_tree):
    # Arrange
    avl_tree.insert(10)
    avl_tree.insert(5)
    avl_tree.insert(15)
    avl_tree.insert(12)
    avl_tree.insert(17)

    # Act
    avl_tree.delete(15)

    # Assert
    assert avl_tree.root.value == 10
    assert avl_tree.root.left.value == 5
    assert avl_tree.root.right.value == 17
    assert avl_tree.root.right.left.value == 12


def test_avl_tree_delete_root(avl_tree):
    # Arrange
    avl_tree.insert(10)
    avl_tree.insert(5)
    avl_tree.insert(15)

    # Act
    avl_tree.delete(10)

    # Assert
    assert avl_tree.root.value == 15
    assert avl_tree.root.left.value == 5
    assert avl_tree.root.right is None
