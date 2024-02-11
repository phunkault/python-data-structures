import pytest

from src.dequeue.dequeue import Dequeue


# Arrange
@pytest.fixture
def dequeue():
    return Dequeue()


# Initial state
def test_dequeue_returns_initial_state_correctly(dequeue):
    # Act and Assert
    assert dequeue
    assert dequeue.size == 0
    # assert str(dequeue) == ''
    # assert dequeue.is_empty
