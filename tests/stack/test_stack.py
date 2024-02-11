import pytest

from src.stack.stack import Stack


# Arrange
@pytest.fixture
def stack():
    return Stack()


# Initial state
def test_initial_state(stack):
    # Act and Assert
    assert stack
    assert stack.length == 0
    assert stack.is_empty


# Push
def test_push_single_element(stack):
    # Act
    stack.push(1)

    # Assert
    assert stack.length == 1
    assert str(stack) == '1'


def test_push_multiple_elements(stack):
    # Act
    stack.push(10)
    stack.push(20)
    stack.push(30)

    # Assert
    assert stack.length == 3
    assert str(stack) == '30 -> 20 -> 10'


# Pop
def test_pop_removes_and_returns_top_element(stack):
    # Arrange
    stack.push(7)
    stack.push(14)
    stack.push(21)

    # Act
    popped_element = stack.pop()

    # Assert
    assert popped_element == 21
    assert str(stack) == '14 -> 7'
    assert stack.length == 2


def test_pop_returns_none_for_empty_stack(stack):
    # Act
    popped_element = stack.pop()

    # Assert
    assert not popped_element
    assert stack.length == 0
