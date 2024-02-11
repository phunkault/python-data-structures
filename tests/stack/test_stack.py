import pytest

from src.stack.stack import Stack


# Arrange
@pytest.fixture
def stack():
    return Stack()


def test_initial_state(stack):
    # Act and Assert
    assert stack
    assert stack.size == 0
    # assert stack.is_empty
