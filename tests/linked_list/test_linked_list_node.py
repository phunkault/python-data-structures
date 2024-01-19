import pytest
from src.linked_list.linked_list_node import LinkedListNode


test_values = (1, "1", 1.1, True, None, [1, 2, 3], {"1", "2", "3"}, {"key": 1})


@pytest.mark.parametrize("test_value", test_values)
def test_linked_list_node_init_with_primitive_value_type(test_value):
    # Act
    node = LinkedListNode(test_value)

    # Assert
    assert node.value == test_value
    assert node.next is None


@pytest.mark.parametrize("test_value", test_values)
def test_linked_list_node_to_str(test_value):
    # Arrange
    node = LinkedListNode(test_value)

    # Act and Assert
    assert str(node) == f"LinkedListNode({node.value})"


def test_linked_list_link_nodes_together():
    # Arrange
    node1 = LinkedListNode(1)
    node2 = LinkedListNode(2)

    # Act
    node1.next = node2

    # Assert
    assert node1.next == node2
    assert node2.next is None