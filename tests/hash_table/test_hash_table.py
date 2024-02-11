import pytest
from src.hash_table.hash_table import HashMap  # Import your HashMap class implementation


@pytest.fixture
def hash_map():
    return HashMap()


def test_initial_state(hash_map):
    assert hash_map.size == 0
