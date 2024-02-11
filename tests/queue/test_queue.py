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
