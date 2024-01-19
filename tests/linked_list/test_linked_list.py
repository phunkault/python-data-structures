# import pytest


def test_initial_state(linked_list):
    assert linked_list.head is None
    assert linked_list.tail is None
    assert linked_list.size == 0
