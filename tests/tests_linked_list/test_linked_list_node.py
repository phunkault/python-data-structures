import pytest
from src.linked_list.linked_list_node import LinkedListNode


test_values_primitive = (1, "1", 1.1, True)
test_values_reference = ([1, 2, 3], {"1", "2", "3"}, {"key": 1})


@pytest.mark.parametrize("test_value", test_values_primitive)
def test_linked_list_node_init_with_value_primitive(test_value):
    # Act
    node = LinkedListNode(test_value)

    # Assert
    assert node.value == test_value
    assert node.next is None


@pytest.mark.parametrize("test_value", test_values_reference)
def test_linked_list_node_init_with_value_reference(test_value):
    # Act
    node = LinkedListNode(test_value)

    # Assert
    assert node.value == test_value
    assert node.next is None


def test_linked_list_node_init_without_value():
    # Act
    node = LinkedListNode(None)

    # Assert
    assert node.value is None
    assert node.next is None


def test_linked_list_node_equality():
    # Arrange
    node1 = LinkedListNode(1)
    node2 = LinkedListNode(1)
    node3 = LinkedListNode(2)

    # Act and Assert
    assert node1 == node2
    assert node1 != node3
    assert node2 != node3


@pytest.mark.parametrize("test_value", test_values_primitive)
def test_linked_list_node_str(test_value):
    # Arrange
    node = LinkedListNode(test_value)

    # Act and Assert
    assert str(node) == f"LinkedListNode({node.value})"


def test_linked_list_node_set_next():
    # Arrange
    node1 = LinkedListNode(1)
    node2 = LinkedListNode(2)

    # Act
    node1.next = node2

    # Assert
    assert node1.next == node2
    assert node2.next is None
