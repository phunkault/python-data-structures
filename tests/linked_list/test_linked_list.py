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

    assert empty_linked_list.length == 0


def test_append_empty_list(empty_linked_list):
    # Act
    empty_linked_list.append(1)

    # Assert
    assert empty_linked_list.head.value == 1
    assert empty_linked_list.head.next is None

    assert empty_linked_list.tail.value == 1
    assert empty_linked_list.tail.next is None

    assert empty_linked_list.length == 1


def test_append_call_chain(empty_linked_list):
    # Act
    empty_linked_list.append(1).append(2).append(3)

    # Assert
    assert empty_linked_list.head.value == 1
    assert empty_linked_list.head.next.value == 2
    assert empty_linked_list.head.next.next.value == 3

    assert empty_linked_list.tail.value == 3
    assert empty_linked_list.tail.next is None

    assert empty_linked_list.length == 3


def test_append_non_empty_list(non_empty_linked_list):
    # Act
    non_empty_linked_list.append(2)

    # Assert
    assert non_empty_linked_list.head.value == 1
    assert non_empty_linked_list.head.next.value == 2

    assert non_empty_linked_list.tail.value == 2
    assert non_empty_linked_list.tail.next is None

    assert non_empty_linked_list.length == 2


def test_prepend_empty_list(empty_linked_list):
    # Act
    empty_linked_list.prepend(1)

    # Assert
    assert empty_linked_list.head.value == 1
    assert empty_linked_list.head.next is None

    assert empty_linked_list.tail.value == 1
    assert empty_linked_list.tail.next is None
    assert empty_linked_list.length == 1


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

    assert empty_linked_list.length == 2


def test_prepend_call_chain(empty_linked_list):
    # Act
    empty_linked_list.prepend(3).prepend(2).prepend(1)

    # Assert
    assert empty_linked_list.length == 3


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


def test_empty_array_creates_empty_list(empty_linked_list):
    # Act
    empty_linked_list.from_array([])

    # Assert
    assert empty_linked_list.length == 0


def test_non_empty_array_creates_list_with_same_nodes(empty_linked_list):
    # Act
    empty_linked_list.from_array([1, 2, 3])

    # Assert
    assert (
        empty_linked_list.to_string()
        == "LinkedListNode(1) -> LinkedListNode(2) -> LinkedListNode(3)"
    )


def test_returns_null_when_deleting_a_non_existing_node(empty_linked_list):
    # Act
    deleted_node = empty_linked_list.delete(2)

    # Assert
    assert deleted_node is None
    assert empty_linked_list.head is None
    assert empty_linked_list.tail is None
    assert empty_linked_list.length == 0


def test_deletes_the_element_outside_the_list(empty_linked_list):
    # Arrange
    empty_linked_list.from_array([1, 2])

    # Act
    deleted_node = empty_linked_list.delete(3)

    # Assert
    assert deleted_node is None
    assert empty_linked_list.head.value == 1
    assert empty_linked_list.tail.value == 2
    assert empty_linked_list.tail.next is None
    assert (
        empty_linked_list.to_string()
        == "LinkedListNode(1) -> LinkedListNode(2)"
    )
    assert empty_linked_list.length == 2


def test_deletes_the_node_from_the_singular_node_list(non_empty_linked_list):
    # Act
    deleted_element = non_empty_linked_list.delete(1)

    # Assert
    assert deleted_element.value == 1
    assert non_empty_linked_list.head is None
    assert non_empty_linked_list.tail is None
    assert non_empty_linked_list.length == 0


def test_deletes_the_first_node_from_the_multi_node_list(empty_linked_list):
    # Arrange
    empty_linked_list.from_array([1, 2, 3])

    # Act
    deleted_node = empty_linked_list.delete(1)

    # Assert
    assert deleted_node.value == 1
    assert empty_linked_list.head.value == 2
    assert empty_linked_list.head.next.value == 3
    assert empty_linked_list.tail.value == 3
    assert (
        empty_linked_list.to_string()
        == "LinkedListNode(2) -> LinkedListNode(3)"
    )
    assert empty_linked_list.length == 2


def test_deletes_an_element_in_the_middle(empty_linked_list):
    # Arrange
    empty_linked_list.from_array([1, 2, 3])

    # Act
    deleted_element = empty_linked_list.delete(2)

    # Assert
    assert deleted_element.value == 2
    assert empty_linked_list.head.value == 1
    assert empty_linked_list.head.next.value == 3
    assert empty_linked_list.tail.value == 3
    assert (
        empty_linked_list.to_string()
        == "LinkedListNode(1) -> LinkedListNode(3)"
    )
    assert empty_linked_list.length == 2


def test_deletes_the_last_element(empty_linked_list):
    # Arrange
    empty_linked_list.from_array([1, 2, 3])

    # Act
    deleted_element = empty_linked_list.delete(3)

    # Assert
    assert deleted_element.value == 3
    assert empty_linked_list.head.value == 1
    assert empty_linked_list.head.next.value == 2
    assert empty_linked_list.tail.value == 2
    assert empty_linked_list.tail.next is None
    assert (
        empty_linked_list.to_string()
        == "LinkedListNode(1) -> LinkedListNode(2)"
    )
    assert empty_linked_list.length == 2


def test_insert_at_throws_exception_if_index_less_than_list_length(
    empty_linked_list
):
    # Act and Assert
    with pytest.raises(
        IndexError,
        match="Index should be >= 0 and <= list length.",
    ):
        empty_linked_list.insert_at(-1, 1)


def test_insert_at_throws_exception_if_index_greater_than_list_length(
    empty_linked_list
):
    # Act and Assert
    with pytest.raises(
        IndexError,
        match="Index should be >= 0 and <= list length.",
    ):
        empty_linked_list.insert_at(10, 1)


def test_insert_at_beginning_of_list(non_empty_linked_list):
    # Act
    non_empty_linked_list.insert_at(0, 0)

    # Assert
    assert non_empty_linked_list.head.value == 0
    assert non_empty_linked_list.head.next.value == 1
    assert non_empty_linked_list.tail.value == 1
    assert non_empty_linked_list.tail.next is None
    assert (
        non_empty_linked_list.to_string()
        == "LinkedListNode(0) -> LinkedListNode(1)"
    )
    assert non_empty_linked_list.length == 2


def test_insert_at_end_of_list(non_empty_linked_list):
    # Act
    non_empty_linked_list.insert_at(1, 2)

    # Assert
    assert non_empty_linked_list.head.value == 1
    assert non_empty_linked_list.head.next.value == 2
    assert non_empty_linked_list.tail.value == 2
    assert non_empty_linked_list.tail.next is None
    assert (
        non_empty_linked_list.to_string()
        == "LinkedListNode(1) -> LinkedListNode(2)"
    )
    assert non_empty_linked_list.length == 2


def test_insert_in_middle_of_list(empty_linked_list):
    # Arrange
    empty_linked_list.append(1).append(3)

    # Act
    empty_linked_list.insert_at(1, 2)

    # Assert
    assert empty_linked_list.head.value == 1
    assert empty_linked_list.head.next.next.value == 3
    assert empty_linked_list.tail.value == 3
    assert empty_linked_list.tail.next is None
    assert (
        empty_linked_list.to_string()
        == "LinkedListNode(1) -> LinkedListNode(2) -> LinkedListNode(3)"
    )
    assert empty_linked_list.length == 3


def test_insert_at_call_chain(empty_linked_list):
    # Act
    empty_linked_list.insert_at(0, 1).insert_at(1, 2)

    # Assert
    assert empty_linked_list.head.value == 1
    assert empty_linked_list.tail.value == 2
    assert (
        empty_linked_list.to_string()
        == "LinkedListNode(1) -> LinkedListNode(2)"
    )
    assert empty_linked_list.length == 2


def test_is_empty_empty_list(empty_linked_list):
    # Act and Assert
    assert empty_linked_list.is_empty()


def test_is_empty_non_empty_list(non_empty_linked_list):
    # Act and Assert
    assert not non_empty_linked_list.is_empty()


def test_is_empty_after_append(empty_linked_list):
    # Act and Assert
    empty_linked_list.append(1)
    assert not empty_linked_list.is_empty()


def test_is_empty_after_delete(non_empty_linked_list):
    # Act and Assert
    non_empty_linked_list.delete(1)
    assert non_empty_linked_list.is_empty()


def test_get_length_empty_list(empty_linked_list):
    # Act and Assert
    assert empty_linked_list.get_length() == 0


def test_get_length_non_empty_list(non_empty_linked_list):
    # Act and Assert
    assert non_empty_linked_list.get_length() == 1


def test_get_length_after_append(empty_linked_list):
    # Arrange
    empty_linked_list.append(2)

    # Act and Assert
    assert empty_linked_list.get_length() == 1


def test_get_length_after_delete(non_empty_linked_list):
    # Arrange
    non_empty_linked_list.delete(1)

    # Act and Assert
    assert non_empty_linked_list.get_length() == 0
