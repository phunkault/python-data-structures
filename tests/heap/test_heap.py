import pytest

from src.heap.heap import Heap


# Arrange
@pytest.fixture()
def heap():
    return Heap()


# Initial state
def test_heap_initial_state(heap):
    # Assert
    assert heap
    assert not heap.container
    assert heap.size == 0
    assert heap.is_empty
    assert not heap.peek()
