from src.tree.avl_tree_node import AVLTreeNode


# Initial state
def test_avl_tree_node_initial_state():
    # Arrange
    node = AVLTreeNode()

    # Assert
    assert node
    assert not node.value
    assert not node.left
    assert not node.right
    assert node.height == 1
    assert str(node) == "None"
