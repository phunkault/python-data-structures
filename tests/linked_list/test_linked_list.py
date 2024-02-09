import pytest
from src.linked_list.linked_list import LinkedList


# Arrange
@pytest.fixture
def linked_list():
    return LinkedList()


# Initial State
def test_returns_correct_initial_state(linked_list):
    # Assert
    assert linked_list.head is None
    assert linked_list.tail is None
    assert linked_list.is_empty
    assert linked_list.length == 0


# Is Empty
def test_is_empty_returns_false_for_the_non_empty_list(linked_list):
    # Arrange
    linked_list.append(1)

    # Assert
    assert not linked_list.is_empty
    assert linked_list.length == 1


# Append
def test_append_adds_nodes_to_the_end_of_the_list_correctly(linked_list):
    # Act
    linked_list.append(1)

    # Assert
    assert linked_list.head.data == 1
    assert linked_list.tail.data == 1
    assert linked_list.tail.next is None
    assert linked_list.length == 1

    # Act
    linked_list.append(2)

    # Assert
    assert linked_list.head.data == 1
    assert linked_list.head.next.data == 2
    assert linked_list.tail.data == 2
    assert linked_list.tail.next is None

    assert linked_list.length == 2


def test_append_can_be_used_in_call_chain(linked_list):
    # Act
    linked_list.append(1).append(2).append(3)

    # Assert
    assert linked_list.head.data == 1
    assert linked_list.head.next.data == 2
    assert linked_list.head.next.next.data == 3

    assert linked_list.tail.data == 3
    assert linked_list.tail.next is None

    assert linked_list.length == 3


# From Array
def test_from_array_creates_an_empty_list_when_an_empty_array_is_passed(linked_list):
    # Act
    linked_list.from_array([])

    assert linked_list.is_empty
    assert linked_list.length == 0


def test_from_array_creates_list_with_the_same_nodes_as_the_input_array(linked_list):
    # Act
    linked_list.from_array([1, 2, 3])

    # Assert
    assert linked_list.head.data == 1
    assert linked_list.head.next.data == 2
    assert linked_list.head.next.next.data == 3

    assert linked_list.tail.data == 3
    assert linked_list.tail.next is None

    assert linked_list.length == 3


# To Array
def test_to_array_returns_an_empty_array_for_the_empty_list(linked_list):
    # Act and Assert
    assert linked_list.to_array() == []
    assert linked_list.head is None
    assert linked_list.tail is None
    assert linked_list.length == 0


def test_to_array_returns_the_array_with_the_same_items_from_the_linked_list(linked_list):
    # Arrange
    array = [1, 2, 3]
    linked_list.from_array(array)

    # Act
    assert linked_list.to_array() == array


# Stringifier
def test_str_converts_the_single_node_list_to_a_string(linked_list):
    # Arrange
    linked_list.append(1)

    # Assert
    assert linked_list.head.data == 1
    assert linked_list.tail.data == 1
    assert linked_list.tail.next is None
    assert str(linked_list) == "1"
    assert linked_list.length == 1


def test_str_converts_the_multiple_node_list_to_a_string(linked_list):
    # Arrange
    linked_list.from_array([1, 2, 3])

    # Assert
    assert str(linked_list) == "1 -> 2 -> 3"


# Prepend
def test_prepend_a_node_to_the_beginning_of_the_empty_list(linked_list):
    # Act
    linked_list.prepend(1)

    # Assert
    assert linked_list.tail.data == 1
    assert linked_list.tail.next is None
    assert str(linked_list) == "1"
    assert linked_list.length == 1


def test_prepend_a_node_at_the_beginning_of_the_multi_node_list(linked_list):
    # Act
    linked_list.prepend(2)
    linked_list.prepend(1)

    # Assert
    assert linked_list.tail.data == 2
    assert linked_list.tail.next is None
    assert str(linked_list) == "1 -> 2"
    assert linked_list.length == 2


def test_prepend_can_be_used_in_call_chain(linked_list):
    # Act
    linked_list.prepend(3).prepend(2).prepend(1)

    # Assert
    assert str(linked_list) == "1 -> 2 -> 3"
    assert linked_list.tail.data == 3
    assert linked_list.tail.next is None
    assert linked_list.length == 3


# Delete
def test_delete_returns_none_when_deleting_a_non_existing_node(linked_list):
    # Act
    deleted_node = linked_list.delete(3)

    # Assert
    assert deleted_node is None
    assert linked_list.length == 0


def test_deletes_the_element_outside_the_list(linked_list):
    # Arrange
    linked_list.from_array([1, 2])

    # Act
    delete_node = linked_list.delete(3)

    # Assert
    assert delete_node is None
    assert str(linked_list) == '1 -> 2'

    assert linked_list.tail.data == 2
    assert linked_list.tail.next is None
    assert linked_list.length == 2


def test_deletes_the_node_from_the_singular_node_list(linked_list):
    # Arrange
    linked_list.append(1)

    # Act
    deleted_node = linked_list.delete(1)

    # Assert
    assert deleted_node.data == 1
    assert linked_list.head is None
    assert linked_list.tail is None
    assert linked_list.length == 0


def test_deletes_the_first_node_from_the_multi_node_list(linked_list):
    # Arrange
    linked_list.from_array([1, 2, 3])

    # Act
    deleted_node = linked_list.delete(1)

    # Assert
    assert deleted_node.data == 1
    assert str(linked_list) == '2 -> 3'

    assert linked_list.tail.data == 3
    assert linked_list.tail.next is None
    assert linked_list.length == 2


def test_deletes_node_from_the_middle_of_the_list(linked_list):
    # Arrange
    linked_list.from_array([1, 2, 3])

    # Act
    deleted_node = linked_list.delete(2)

    # Assert
    assert deleted_node.data == 2
    assert str(linked_list) == '1 -> 3'

    assert linked_list.tail.data == 3
    assert linked_list.tail.next is None
    assert linked_list.length == 2


def test_deletes_the_last_element(linked_list):
    # Arrange
    linked_list.from_array([1, 2])

    # Act
    deleted_node = linked_list.delete(2)

    # Assert
    assert deleted_node.data == 2

    assert str(linked_list) == '1'
    assert linked_list.tail.data == 1
    assert linked_list.tail.next is None
    assert linked_list.length == 1


def test_deletes_node_by_predicate():
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
    ]

    linked_list = LinkedList().from_array(values)

    assert str(linked_list) == "(one, 1) -> (two, 2) -> (three, 3)"
    assert linked_list.tail.data.key == "three"
    assert linked_list.tail.next is None
    assert linked_list.length == 3

    # Act
    deleted_node = linked_list.delete(lambda node: node.key == 'two')

    # Assert
    assert deleted_node.data.key == 'two'
    assert str(linked_list) == "(one, 1) -> (three, 3)"
    assert linked_list.length == 2


# Reverse
def test_reverse_the_empty_list(linked_list):
    # Act
    linked_list.reverse()

    # Assert
    assert linked_list.head is None
    assert linked_list.tail is None
    assert linked_list.length == 0


def test_reverse_the_singular_node(linked_list):
    # Arrange
    linked_list.append(1)

    assert str(linked_list) == "1"
    assert linked_list.tail.data == 1
    assert linked_list.tail.next is None
    assert linked_list.length == 1

    # Act
    linked_list.reverse()

    # Assert
    assert str(linked_list) == "1"
    assert linked_list.tail.data == 1
    assert linked_list.tail.next is None
    assert linked_list.length == 1


def test_reverse_the_multi_node_list(linked_list):
    # Arrange
    linked_list.from_array([1, 2])

    assert linked_list.length == 2

    # Act
    linked_list.reverse()

    # Assert
    assert str(linked_list) == "2 -> 1"
    assert linked_list.tail.data == 1
    assert linked_list.tail.next is None
    assert linked_list.length == 2


def test_reverse_can_be_used_in_call_chain(linked_list):
    # Act
    linked_list.from_array([3, 2, 1]).reverse().append(4)

    assert linked_list.length == 4

    # Assert
    assert str(linked_list) == '1 -> 2 -> 3 -> 4'
    assert linked_list.tail.data == 4
    assert linked_list.tail.next is None
    assert linked_list.length == 4


# Insert At
def test_insert_at_throws_an_exception_if_the_index_is_less_than_the_list_length(linked_list):
    # Act and Assert
    with pytest.raises(
        IndexError,
        match="Index should be >= 0 and <= list length.",
    ):
        linked_list.insert_at(-1, 1)


def test_insert_at_throws_an_exception_if_the_index_is_greater_than_the_list_length(linked_list):
    # Act and Assert
    with pytest.raises(
        IndexError,
        match="Index should be >= 0 and <= list length.",
    ):
        linked_list.insert_at(10, 1)


def test_inserts_a_node_into_the_empty_list(linked_list):
    # Act
    linked_list.insert_at(0, 1)

    # Assert
    assert str(linked_list) == "1"
    assert linked_list.tail.data == 1
    assert linked_list.tail.next is None
    assert linked_list.length == 1


def test_inserts_at_the_beginning_of_the_list(linked_list):
    # Arrange
    linked_list.append(2)

    # Act
    linked_list.insert_at(0, 1)

    # Assert
    assert str(linked_list) == '1 -> 2'
    assert linked_list.tail.data == 2
    assert linked_list.tail.next is None
    assert linked_list.length == 2


def test_inserts_into_the_middle_of_the_list(linked_list):
    # Arrange
    linked_list.from_array([1, 3])

    # Act
    linked_list.insert_at(1, 2)

    # Assert
    assert str(linked_list) == '1 -> 2 -> 3'
    assert linked_list.tail.data == 3
    assert linked_list.tail.next is None
    assert linked_list.length == 3


def test_inserts_at_the_end_of_the_list(linked_list):
    # Arrange
    linked_list.append(1)

    # Act
    linked_list.insert_at(1, 2)

    # Assert
    assert str(linked_list) == "1 -> 2"
    assert linked_list.tail.data == 2
    assert linked_list.tail.next is None
    assert linked_list.length == 2


def test_insert_at_can_be_used_in_a_call_chain(linked_list):
    # Act
    linked_list.insert_at(0, 1).insert_at(1, 2)

    # Assert
    assert str(linked_list) == "1 -> 2"
    assert linked_list.tail.data == 2
    assert linked_list.tail.next is None
    assert linked_list.length == 2


# Delete Head
def test_delete_the_head_from_the_empty_list(linked_list):
    # Act
    deleted_head = linked_list.delete_head()

    # Assert
    assert deleted_head is None

    assert linked_list.head is None
    assert linked_list.tail is None
    assert linked_list.length == 0


def test_delete_the_head_from_the_singular_node_list(linked_list):
    # Arrange
    linked_list.append(1)

    # Act
    deleted_head = linked_list.delete_head()

    # Assert
    assert deleted_head.data == 1

    assert linked_list.head is None
    assert linked_list.tail is None
    assert linked_list.length == 0


def test_delete_the_head_from_the_multy_node_list_corretly(linked_list):
    # Arrange
    linked_list.from_array([1, 2])

    # Act and Assert
    assert linked_list.delete_head().data == 1
    assert linked_list.length == 1


# Delete Tail
def test_delete_the_tail_from_the_empty_list(linked_list):
    # Act
    deleted_tail = linked_list.delete_tail()

    # Assert
    assert deleted_tail is None
    assert linked_list.length == 0


def test_delete_the_tail_from_the_singular_node_list(linked_list):
    # Arrange
    linked_list.append(1)

    # Act
    deleted_tail = linked_list.delete_tail()

    # Assert
    assert deleted_tail.data == 1

    assert linked_list.head is None
    assert linked_list.tail is None
    assert linked_list.length == 0


def test_delete_the_tail_from_the_multi_node_list(linked_list):
    # Arrange
    linked_list.from_array([1, 2])

    # Act
    delete_tail = linked_list.delete_tail()

    # Assert
    assert delete_tail.data == 2
    assert linked_list.tail.data == 1
    assert linked_list.tail.next is None
    assert linked_list.length == 1


# Find
def test_find_returns_non_for_a_not_found_node(linked_list):
    # Act and Assert
    assert linked_list.find(1) is None
    assert linked_list.find(lambda node: node == 100) is None


def test_find_a_node_by_value(linked_list):
    # Arrange
    linked_list.from_array([1, 2])

    # Act
    founded_node = linked_list.find(1)

    # Assert
    assert founded_node.data == 1


def test_found_a_node_by_predicate(linked_list):
    # Arrange
    linked_list.from_array([1, 2, 3])

    # Act
    founded_node = linked_list.find(lambda node: node > 2)

    # Assert
    assert founded_node.data == 3


# Clear
def test_clear_the_linked_list_correctly(linked_list):
    # Arrange
    linked_list.from_array([1, 2, 3])

    # Act
    linked_list.clear()

    # Assert
    assert linked_list.head is None
    assert linked_list.tail is None
    assert linked_list.length == 0
    assert linked_list.is_empty
