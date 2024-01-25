import pytest
from src.linked_list.linked_list import LinkedList


# Arrange
@pytest.fixture
def empty_linked_list():
    return LinkedList()


# Arrange
@pytest.fixture
def non_empty_linked_list():
    return LinkedList().append(1)


def test_initial_state(empty_linked_list):
    # Assert
    assert empty_linked_list.head is None

    assert empty_linked_list.tail is None

    assert empty_linked_list.length == 0


def test_append_empty_list(empty_linked_list):
    # Act
    empty_linked_list.append(1)

    # Assert
    assert empty_linked_list.head.data == 1
    assert empty_linked_list.head.next is None

    assert empty_linked_list.tail.data == 1
    assert empty_linked_list.tail.next is None

    assert empty_linked_list.length == 1


def test_append_call_chain(empty_linked_list):
    # Act
    empty_linked_list.append(1).append(2).append(3)

    # Assert
    assert empty_linked_list.head.data == 1
    assert empty_linked_list.head.next.data == 2
    assert empty_linked_list.head.next.next.data == 3

    assert empty_linked_list.tail.data == 3
    assert empty_linked_list.tail.next is None

    assert empty_linked_list.length == 3


def test_append_non_empty_list(non_empty_linked_list):
    # Act
    non_empty_linked_list.append(2)

    # Assert
    assert non_empty_linked_list.head.data == 1
    assert non_empty_linked_list.head.next.data == 2

    assert non_empty_linked_list.tail.data == 2
    assert non_empty_linked_list.tail.next is None

    assert non_empty_linked_list.length == 2


def test_prepend_empty_list(empty_linked_list):
    # Act
    empty_linked_list.prepend(1)

    # Assert
    assert empty_linked_list.head.data == 1
    assert empty_linked_list.head.next is None

    assert empty_linked_list.tail.data == 1
    assert empty_linked_list.tail.next is None
    assert empty_linked_list.length == 1


def test_prepend_non_empty_list(empty_linked_list):
    # Arrange
    empty_linked_list.append(2)

    # Act
    empty_linked_list.prepend(1)

    # Assert
    assert empty_linked_list.head.data == 1
    assert empty_linked_list.head.next.data == 2

    assert empty_linked_list.tail.data == 2
    assert empty_linked_list.tail.next is None

    assert empty_linked_list.length == 2


def test_prepend_call_chain(empty_linked_list):
    # Act
    empty_linked_list.prepend(3).prepend(2).prepend(1)

    # Assert
    assert empty_linked_list.length == 3


def test_returns_empty_string_for_empty_list(empty_linked_list):
    # Act and Assert
    assert str(empty_linked_list) == ""


def test_returns_non_empty_string_for_non_empty_list(non_empty_linked_list):
    # Arrange
    non_empty_linked_list.append(2)

    # Act and Assert
    assert str(non_empty_linked_list) == "1 -> 2"


def test_empty_array_creates_empty_list(empty_linked_list):
    # Act
    empty_linked_list.from_array([])

    # Assert
    assert empty_linked_list.length == 0


def test_non_empty_array_creates_list_with_same_nodes(empty_linked_list):
    # Act
    empty_linked_list.from_array([1, 2, 3])

    # Assert
    assert str(empty_linked_list) == "1 -> 2 -> 3"


def test_to_array_empty_list(empty_linked_list):
    # Act and Assert
    assert empty_linked_list.to_array() == []
    assert empty_linked_list.head is None
    assert empty_linked_list.tail is None
    assert empty_linked_list.length == 0


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
    assert empty_linked_list.head.data == 1
    assert empty_linked_list.tail.data == 2
    assert empty_linked_list.tail.next is None
    assert str(empty_linked_list) == "1 -> 2"
    assert empty_linked_list.length == 2


def test_deletes_the_node_from_the_singular_node_list(non_empty_linked_list):
    # Act
    deleted_element = non_empty_linked_list.delete(1)

    # Assert
    assert deleted_element.data == 1
    assert non_empty_linked_list.head is None
    assert non_empty_linked_list.tail is None
    assert non_empty_linked_list.length == 0


def test_deletes_the_first_node_from_the_multi_node_list(empty_linked_list):
    # Arrange
    empty_linked_list.from_array([1, 2, 3])

    # Act
    deleted_node = empty_linked_list.delete(1)

    # Assert
    assert deleted_node.data == 1
    assert empty_linked_list.head.data == 2
    assert empty_linked_list.head.next.data == 3
    assert empty_linked_list.tail.data == 3
    assert str(empty_linked_list) == "2 -> 3"
    assert empty_linked_list.length == 2


def test_deletes_an_element_in_the_middle(empty_linked_list):
    # Arrange
    empty_linked_list.from_array([1, 2, 3])

    # Act
    deleted_element = empty_linked_list.delete(2)

    # Assert
    assert deleted_element.data == 2
    assert empty_linked_list.head.data == 1
    assert empty_linked_list.head.next.data == 3
    assert empty_linked_list.tail.data == 3
    assert str(empty_linked_list) == "1 -> 3"
    assert empty_linked_list.length == 2


def test_deletes_the_last_element(empty_linked_list):
    # Arrange
    empty_linked_list.from_array([1, 2, 3])

    # Act
    deleted_element = empty_linked_list.delete(3)

    # Assert
    assert deleted_element.data == 3
    assert empty_linked_list.head.data == 1
    assert empty_linked_list.head.next.data == 2
    assert empty_linked_list.tail.data == 2
    assert empty_linked_list.tail.next is None
    assert str(empty_linked_list) == "1 -> 2"
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
    assert non_empty_linked_list.head.data == 0
    assert non_empty_linked_list.head.next.data == 1
    assert non_empty_linked_list.tail.data == 1
    assert non_empty_linked_list.tail.next is None
    assert str(non_empty_linked_list) == "0 -> 1"
    assert non_empty_linked_list.length == 2


def test_insert_at_end_of_list(non_empty_linked_list):
    # Act
    non_empty_linked_list.insert_at(1, 2)

    # Assert
    assert non_empty_linked_list.head.data == 1
    assert non_empty_linked_list.head.next.data == 2
    assert non_empty_linked_list.tail.data == 2
    assert non_empty_linked_list.tail.next is None
    assert str(non_empty_linked_list) == "1 -> 2"
    assert non_empty_linked_list.length == 2


def test_insert_in_middle_of_list(empty_linked_list):
    # Arrange
    empty_linked_list.append(1).append(3)

    # Act
    empty_linked_list.insert_at(1, 2)

    # Assert
    assert empty_linked_list.head.data == 1
    assert empty_linked_list.head.next.next.data == 3
    assert empty_linked_list.tail.data == 3
    assert empty_linked_list.tail.next is None
    assert str(empty_linked_list) == "1 -> 2 -> 3"
    assert empty_linked_list.length == 3


def test_insert_at_call_chain(empty_linked_list):
    # Act
    empty_linked_list.insert_at(0, 1).insert_at(1, 2)

    # Assert
    assert empty_linked_list.head.data == 1
    assert empty_linked_list.tail.data == 2
    assert str(empty_linked_list) == "1 -> 2"
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
    assert empty_linked_list.length == 0


def test_get_length_non_empty_list(non_empty_linked_list):
    # Act and Assert
    assert non_empty_linked_list.length == 1


def test_get_length_after_append(empty_linked_list):
    # Arrange
    empty_linked_list.append(2)

    # Act and Assert
    assert empty_linked_list.length == 1


def test_get_length_after_delete(non_empty_linked_list):
    # Arrange
    non_empty_linked_list.delete(1)

    # Act and Assert
    assert non_empty_linked_list.length == 0


def test_delete_head_empty_list(empty_linked_list):
    # Act
    deleted_head = empty_linked_list.delete_head()

    # Assert
    assert deleted_head is None
    assert empty_linked_list.head is None
    assert empty_linked_list.tail is None
    assert empty_linked_list.length == 0


def test_delete_head_list_with_multiple_nodes(empty_linked_list):
    # Arrange
    empty_linked_list.from_array([1, 2, 3])

    # Act
    deleted_head = empty_linked_list.delete_head()

    # Assert
    assert deleted_head.data == 1

    assert empty_linked_list.head.data == 2
    assert empty_linked_list.head.next.data == 3

    assert empty_linked_list.tail.data == 3
    assert empty_linked_list.tail.next is None

    assert str(empty_linked_list) == "2 -> 3"

    assert empty_linked_list.length == 2


def test_delete_tail_empty_list(empty_linked_list):
    # Act
    deleted_tail = empty_linked_list.delete_tail()

    # Assert
    assert deleted_tail is None
    assert empty_linked_list.head is None
    assert empty_linked_list.tail is None
    assert empty_linked_list.length == 0


def test_delete_tail_list_with_single_node(empty_linked_list):
    # Arrange
    empty_linked_list.append(1)

    # Act
    deleted_tail = empty_linked_list.delete_tail()

    # Assert
    assert deleted_tail.data == 1

    assert empty_linked_list.head is None
    assert empty_linked_list.tail is None

    assert empty_linked_list.length == 0


def test_delete_tail_list_with_multiple_nodes(empty_linked_list):
    # Arrange
    empty_linked_list.from_array([1, 2, 3])

    # Act
    deleted_tail = empty_linked_list.delete_tail()

    # Assert
    assert deleted_tail.data == 3

    assert empty_linked_list.head.data == 1

    assert empty_linked_list.tail.data == 2
    assert empty_linked_list.tail.next is None

    assert str(empty_linked_list) == "1 -> 2"


def test_reverse_empty_list(empty_linked_list):
    # Act
    empty_linked_list.reverse()

    # Assert
    assert empty_linked_list.head is None
    assert empty_linked_list.tail is None
    assert empty_linked_list.length == 0


def test_reverse_list_with_single_node(empty_linked_list):
    # Arrange
    empty_linked_list.append(1)

    # Act
    empty_linked_list.reverse()

    # Assert
    assert empty_linked_list.head.data == 1

    assert empty_linked_list.tail.data == 1

    assert str(empty_linked_list) == "1"

    assert empty_linked_list.length == 1


def test_reverse_list_with_multiple_nodes(empty_linked_list):
    # Arrange
    empty_linked_list.from_array([1, 2, 3])

    # Act
    empty_linked_list.reverse()

    # Assert
    assert empty_linked_list.head.data == 3
    assert empty_linked_list.head.next.data == 2

    assert empty_linked_list.tail.data == 1
    assert empty_linked_list.tail.next is None

    assert str(empty_linked_list) == "3 -> 2 -> 1"

    assert empty_linked_list.length == 3


def test_reverse_call_chain(empty_linked_list):
    # Act
    empty_linked_list.from_array([1, 2, 3]).reverse().append(4)

    # Assert
    assert empty_linked_list.head.data == 3

    assert empty_linked_list.tail.data == 4

    assert empty_linked_list.tail.next is None

    assert str(empty_linked_list) == "3 -> 2 -> 1 -> 4"

    assert empty_linked_list.length == 4


def test_find_empty_list(empty_linked_list):
    # Act and Assert
    assert empty_linked_list.find(1) is None


def test_find_list_with_single_node(empty_linked_list):
    # Arrange
    empty_linked_list.from_array([1])

    # Act
    founded_node = empty_linked_list.find(1)

    # Assert
    assert founded_node.data == 1


def test_find_list_with_multiple_node(empty_linked_list):
    # Arrange
    empty_linked_list.from_array([1, 2, 2, 4])

    # Act
    founded_node = empty_linked_list.find(2)

    # Assert
    assert founded_node.data == 2


def test_clear_empty_linked_list(empty_linked_list):
    # Act
    empty_linked_list.clear()

    # Assert
    assert empty_linked_list.head is None
    assert empty_linked_list.tail is None
    assert empty_linked_list.length == 0
    assert empty_linked_list.is_empty()


def test_clear_non_empty_linked_list(non_empty_linked_list):
    # Act
    non_empty_linked_list.clear()

    # Assert
    assert non_empty_linked_list.head is None
    assert non_empty_linked_list.tail is None
    assert non_empty_linked_list.length == 0
    assert non_empty_linked_list.is_empty()


def test_delete_by_predicate():
    # Arrange
    class Value:
        def __init__(self, key, value):
            self.key = key
            self.value = value

        def __str__(self):
            return f"({self.key}, {self.value})"

    values = [
        Value("one", 1),
        Value("two", 2),
        Value("three", 3),
        Value("four", 4),
    ]

    linked_list = LinkedList()
    linked_list.from_array(values)

    # Act
    deleted_node = linked_list.delete(lambda node: node.key == "two")

    # Assert
    assert deleted_node.data.value == 2

    assert linked_list.head.data.value == 1
    assert linked_list.head.next.data.value == 3
    assert linked_list.tail.data.value == 4
    assert str(linked_list) == "(one, 1) -> (three, 3) -> (four, 4)"
    assert linked_list.length == 3
