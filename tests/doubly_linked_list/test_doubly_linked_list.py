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
