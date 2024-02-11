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
    assert str(queue) == '10 -> 20 -> 30'
    assert queue.size == 3


# Dequeue
def test_dequeue_removes_and_returns_front_element(queue):
    # Arrange
    queue.enqueue(10)
    queue.enqueue(20)
    queue.enqueue(30)

    # Act
    removed_element = queue.dequeue()

    # Assert
    assert removed_element == 10
    assert str(queue) == '20 -> 30'
    assert queue.size == 2


def test_dequeue_returns_none_for_empty_queue(queue):
    # Act
    removed_element = queue.dequeue()

    # Assert
    assert not removed_element
    assert queue.size == 0
