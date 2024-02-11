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


# Remove front
def test_remove_front_removes_elements_from_the_front_in_correct_order(dequeue):
    # Arrange
    dequeue.add_front(1).add_front(2)

    # Act and Assert
    assert dequeue.remove_front().data == 2
    assert dequeue.remove_front().data == 1
    assert not dequeue.remove_front()
    assert dequeue.size == 0


# Peek front
def test_peek_front_peeks_elements_from_the_front_without_removing_it(dequeue):
    # Act and Assert
    assert not dequeue.peek_front()

    # Act and Assert
    dequeue.add_front(2)
    assert dequeue.peek_front().data == 2

    # Act and Assert
    dequeue.add_front(1)
    assert dequeue.peek_front().data == 1


# Add rear
def test_add_rear_adds_elements_to_the_rear_in_correct_order(dequeue):
    # Act
    dequeue.add_rear(1)

    # Assert
    assert str(dequeue) == '1'
    assert dequeue.size == 1

    # Act
    dequeue.add_rear(2)

    # Assert
    assert str(dequeue) == '1 -> 2'
    assert dequeue.size == 2


# Remove rear
def test_remove_rear_removes_elements_from_the_rear_in_correct_order(dequeue):
    # Arrange
    dequeue.add_rear(1).add_rear(2)

    # Act and Assert
    assert dequeue.remove_rear().data == 2
    assert dequeue.remove_rear().data == 1
    assert not dequeue.remove_rear()
    assert dequeue.size == 0
