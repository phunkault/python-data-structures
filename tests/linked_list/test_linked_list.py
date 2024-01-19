import pytest
from src.linked_list.linked_list import LinkedList


@pytest.fixture
def get_test_linked_list():
    return LinkedList()


def test_initial_state(get_test_linked_list):
    assert get_test_linked_list.head is None
    assert get_test_linked_list.tail is None
    assert get_test_linked_list.size == 0
