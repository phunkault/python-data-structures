import pytest

from src.mfu_cache.mfu_cache import MFUCache


# Arrange
@pytest.fixture()
def mfu_cache():
    return MFUCache()


# Initial state
def test_mfu_cache_initial_state(mfu_cache):
    # Assert
    assert mfu_cache
    assert mfu_cache.size == 0
    assert mfu_cache.capacity == 3
