from src.tree.binary_tree_node import BinaryTreeNode

import pytest


# Arrange
@pytest.fixture()
def binary_tree_node():
    return BinaryTreeNode()


# Initial state
def test_initial_state_is_correct(binary_tree_node):
    # Assert
    assert binary_tree_node
    assert not binary_tree_node.value
    assert not binary_tree_node.left
    assert not binary_tree_node.right


def test_to_string(binary_tree_node):
    # Assert
    assert str(binary_tree_node) == "None"

    # Act and arrange
    node = BinaryTreeNode(1)

    # Assert
    assert str(node) == "1"


def test_nodes_link_together(binary_tree_node):
    # Act and arrange
    node = BinaryTreeNode(
        value=0,
        left=BinaryTreeNode(1),
        right=BinaryTreeNode(2)
    )

    # Assert
    assert node.left.value == 1
    assert node.right.value == 2

    assert not node.left.left
    assert not node.left.right

    assert not node.right.left
    assert not node.right.right
