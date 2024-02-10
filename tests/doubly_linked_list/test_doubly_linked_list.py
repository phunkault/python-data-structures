import pytest
from src.doubly_linked_list.doubly_linked_list import DoublyLinkedList


# Arrange
@pytest.fixture
def doubly_linked_list():
    return DoublyLinkedList()


# Initial State
def test_initial_state(doubly_linked_list):
    # Assert
    assert doubly_linked_list.head is None
    assert doubly_linked_list.tail is None
    assert doubly_linked_list.length == 0
    assert str(doubly_linked_list) == ''
    assert doubly_linked_list.is_empty


# Append
def test_append_to_empty_list(doubly_linked_list):
    # Act
    doubly_linked_list.append(1)

    # Assert
    assert doubly_linked_list.head.data == 1
    assert doubly_linked_list.head.prev is None

    assert doubly_linked_list.tail.data == 1
    assert doubly_linked_list.tail.next is None

    assert doubly_linked_list.length == 1


def test_append_to_non_empty_list(doubly_linked_list):
    # Act
    doubly_linked_list.append(1)
    doubly_linked_list.append(2)

    # Assert
    assert doubly_linked_list.head.data == 1
    assert doubly_linked_list.head.next.data == 2
    assert doubly_linked_list.head.next.prev.data == 1

    assert doubly_linked_list.tail.data == 2
    assert doubly_linked_list.tail.next is None

    assert doubly_linked_list.length == 2


def test_append_in_call_chain(doubly_linked_list):
    # Act
    doubly_linked_list.append(1).append(2)

    # Assert
    assert doubly_linked_list.head.data == 1
    assert doubly_linked_list.head.next.data == 2
    assert doubly_linked_list.head.prev is None

    assert doubly_linked_list.head.next.next is None
    assert doubly_linked_list.head.next.prev.data == 1

    assert doubly_linked_list.length == 2


# Prepend
def test_prepend_empty_list(doubly_linked_list):
    # Act
    doubly_linked_list.prepend(1)

    # Assert
    assert doubly_linked_list.head.data == 1
    assert doubly_linked_list.head.next is None
    assert doubly_linked_list.head.prev is None
    assert doubly_linked_list.length == 1


def test_prepend_non_empty_list(doubly_linked_list):
    # Arrange
    doubly_linked_list.append(2)

    # Act
    doubly_linked_list.prepend(1)

    # Assert
    assert doubly_linked_list.head.data == 1
    assert doubly_linked_list.head.next.data == 2
    assert doubly_linked_list.head.prev is None

    assert doubly_linked_list.tail.data == 2
    assert doubly_linked_list.tail.next is None
    assert doubly_linked_list.tail.prev.data == 1

    assert str(doubly_linked_list) == '1 -> 2'
    assert doubly_linked_list.length == 2


def test_prepend_call_chain(doubly_linked_list):
    # Act
    doubly_linked_list.prepend(2).prepend(1)

    # Assert
    assert str(doubly_linked_list) == '1 -> 2'
    assert doubly_linked_list.length == 2


# Delete
def test_delete_non_existing_node(doubly_linked_list):
    # Act
    deleted_node = doubly_linked_list.delete(5)

    # Assert
    assert deleted_node is None
    assert doubly_linked_list.head is None
    assert doubly_linked_list.tail is None
    assert doubly_linked_list.length == 0


def test_delete_element_outside_list(doubly_linked_list):
    # Arrange
    doubly_linked_list.from_array([1, 2])

    # Act
    deleted_node = doubly_linked_list.delete(3)

    assert deleted_node is None
    assert doubly_linked_list.head.data == 1
    assert doubly_linked_list.head.prev is None

    assert doubly_linked_list.tail.data == 2
    assert doubly_linked_list.tail.next is None

    assert str(doubly_linked_list) == '1 -> 2'
    assert doubly_linked_list.length == 2


def test_delete_node_from_singular_node_list(doubly_linked_list):
    # Arrange
    doubly_linked_list.append(1)

    # Act
    deleted_node = doubly_linked_list.delete(1)

    # Assert
    assert deleted_node.data == 1
    assert doubly_linked_list.head is None
    assert doubly_linked_list.tail is None
    assert doubly_linked_list.length == 0


def test_delete_first_element(doubly_linked_list):
    # Arrange
    doubly_linked_list.from_array([1, 2])

    # Act
    deleted_node = doubly_linked_list.delete(1)

    # Assert
    assert deleted_node.data == 1
    assert doubly_linked_list.head.data == 2
    assert doubly_linked_list.head.next is None
    assert doubly_linked_list.head.prev is None

    assert doubly_linked_list.tail.data == 2
    assert doubly_linked_list.tail.next is None

    assert str(doubly_linked_list) == '2'
    assert doubly_linked_list.length == 1


def test_delete_element_in_the_middle(doubly_linked_list):
    # Arrange
    doubly_linked_list.from_array([1, 2, 3])

    # Act
    deleted_node = doubly_linked_list.delete(2)

    # Assert
    assert deleted_node.data == 2
    assert doubly_linked_list.head.data == 1
    assert doubly_linked_list.head.next.data == 3

    assert doubly_linked_list.tail.next is None
    assert doubly_linked_list.tail.prev.data == 1

    assert str(doubly_linked_list) == '1 -> 3'
    assert doubly_linked_list.length == 2


def test_delete_last_element(doubly_linked_list):
    # Arrange
    doubly_linked_list.from_array([1, 2])

    # Act
    deleted_node = doubly_linked_list.delete(2)

    # Assert
    assert deleted_node.data == 2
    assert doubly_linked_list.head.data == 1
    assert doubly_linked_list.head.next is None

    assert doubly_linked_list.tail.data == 1
    assert doubly_linked_list.tail.next is None
    assert doubly_linked_list.tail.prev is None

    assert str(doubly_linked_list) == '1'
    assert doubly_linked_list.length == 1


def test_delete_node_with_object_value():
    doubly_linked_list = DoublyLinkedList()
    values = [
        {'key': 'one', 'value': 1},
        {'key': 'two', 'value': 2},
        {'key': 'three', 'value': 3}
    ]
    doubly_linked_list.from_array(values)

    deleted_node = doubly_linked_list.delete({'key': 'two', 'value': 2})

    assert deleted_node.data['value'] == 2
    assert doubly_linked_list.head.data['value'] == 1
    assert doubly_linked_list.head.next.data['value'] == 3
    assert doubly_linked_list.head.next.prev.data['value'] == 1

    assert doubly_linked_list.tail.data['value'] == 3
    assert doubly_linked_list.tail.next is None
    assert doubly_linked_list.length == 2
