import pytest
from src.linked_list.linked_list import LinkedList


# Arrange
@pytest.fixture
def empty_linked_list():
    return LinkedList()


# Arrange
@pytest.fixture
def non_empty_linked_list():
    return LinkedList(1)


def test_initial_state(empty_linked_list):
    # Assert
    assert empty_linked_list.head is None

    assert empty_linked_list.tail is None

    assert empty_linked_list.size == 0


def test_append_empty_list(empty_linked_list):
    # Act
    empty_linked_list.append(1)

    # Assert
    assert empty_linked_list.head.value == 1
    assert empty_linked_list.head.next is None

    assert empty_linked_list.tail.value == 1
    assert empty_linked_list.tail.next is None

    assert empty_linked_list.size == 1


def test_append_call_chain(empty_linked_list):
    # Act
    empty_linked_list.append(1).append(2).append(3)

    # Assert
    assert empty_linked_list.head.value == 1
    assert empty_linked_list.head.next.value == 2
    assert empty_linked_list.head.next.next.value == 3

    assert empty_linked_list.tail.value == 3
    assert empty_linked_list.tail.next is None

    assert empty_linked_list.size == 3


def test_append_non_empty_list(non_empty_linked_list):
    # Act
    non_empty_linked_list.append(2)

    # Assert
    assert non_empty_linked_list.head.value == 1
    assert non_empty_linked_list.head.next.value == 2

    assert non_empty_linked_list.tail.value == 2
    assert non_empty_linked_list.tail.next is None

    assert non_empty_linked_list.size == 2


def test_prepend_empty_list(empty_linked_list):
    # Act
    empty_linked_list.prepend(1)

    # Assert
    assert empty_linked_list.head.value == 1
    assert empty_linked_list.head.next is None

    assert empty_linked_list.tail.value == 1
    assert empty_linked_list.tail.next is None
    assert empty_linked_list.size == 1


def test_prepend_non_empty_list(empty_linked_list):
    # Arrange
    empty_linked_list.append(2)

    # Act
    empty_linked_list.prepend(1)

    # Assert
    assert empty_linked_list.head.value == 1
    assert empty_linked_list.head.next.value == 2

    assert empty_linked_list.tail.value == 2
    assert empty_linked_list.tail.next is None

    assert empty_linked_list.size == 2


def test_prepend_call_chain(empty_linked_list):
    # Act
    empty_linked_list.prepend(3).prepend(2).prepend(1)

    # Assert
    assert empty_linked_list.size == 3


def test_returns_empty_string_for_empty_list(empty_linked_list):
    # Act and Assert
    assert empty_linked_list.to_string() == ""


def test_returns_non_empty_string_for_non_empty_list(non_empty_linked_list):
    # Arrange
    non_empty_linked_list.append(2)

    # Act and Assert
    assert (
        non_empty_linked_list.to_string()
        == "LinkedListNode(1) -> LinkedListNode(2)"
    )
