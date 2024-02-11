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
    assert dequeue.is_empty
    assert str(dequeue) == ''


# Add front
def test_add_front_adds_elements_to_the_front_in_correct_order(dequeue):
    # Act
    dequeue.add_front(2)

    # Assert
    assert str(dequeue) == '2'
    assert dequeue.size == 1

    # Act
    dequeue.add_front(1)

    # Assert
    assert str(dequeue) == '1 -> 2'
    assert dequeue.size == 2
