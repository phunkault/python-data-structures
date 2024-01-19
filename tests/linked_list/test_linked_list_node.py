import pytest
from src.linked_list.linked_list_node import LinkedListNode


test_values = (1, "1", 1.1, True, None, [1, 2, 3], {"1", "2", "3"}, {"key": 1})


@pytest.mark.parametrize("test_value", test_values)
def test_creates_node_with_value(test_value):
    # Act
    node = LinkedListNode(test_value)

    # Assert
    assert node.value == test_value
    assert node.next is None


@pytest.mark.parametrize("test_value", test_values)
def test_to_string_method(test_value):
    # Arrange
    node = LinkedListNode(test_value)

    # Act and Assert
    assert str(node) == f"LinkedListNode({node.value})"


def test_links_nodes_together():
    # Arrange
    node2 = LinkedListNode(1)

    # Act
    node1 = LinkedListNode(2, node2)

    # Assert
    assert node1.next is not None
    assert node2.next is None
    assert node1.value == 2
    assert node1.next.value == 1
