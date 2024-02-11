import pytest

from src.queue.queue import Queue


# Arrange
@pytest.fixture
def queue():
    return Queue()


# Initial state
def test_initial_state(queue):
    # Act and Assert
    assert queue
    assert queue.is_empty
    assert queue.size == 0


# Enqueue
def test_enqueue_single_element(queue):
    # Act
    queue.enqueue(10)

    # Assert
    assert queue.size == 1


def test_enqueue_multiple_elements(queue):
    # Act
    queue.enqueue(10)
    queue.enqueue(20)
    queue.enqueue(30)

    # Assert
    assert str(queue) == '30 -> 20 -> 10'
    assert queue.size == 3
