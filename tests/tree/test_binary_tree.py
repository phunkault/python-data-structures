from src.tree.binary_tree import BinaryTreeNode

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
