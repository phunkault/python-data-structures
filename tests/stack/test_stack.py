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
    # assert str(stack) == '1'


def test_push_multiple_elements(stack):
    # Act
    stack.push(10)
    stack.push(20)
    stack.push(30)

    # Assert
    assert stack.length == 3
    # assert str(stack) == '30,20,10'
