import pytest
from src.doubly_linked_list.doubly_linked_list import DoublyLinkedList


@pytest.fixture
def doubly_linked_list():
    return DoublyLinkedList()


def test_initial_state(doubly_linked_list):
    assert doubly_linked_list.head is None
    assert doubly_linked_list.tail is None
    assert doubly_linked_list.length == 0
    assert str(doubly_linked_list) == ''
    assert doubly_linked_list.is_empty
