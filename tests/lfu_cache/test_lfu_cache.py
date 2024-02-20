import pytest

from src.lfu_cache.lfu_cache import LFUCache


# Arrange
@pytest.fixture()
def lfu_cache():
    return LFUCache(2)


# Initial state
def test_lfu_cache_initial_state(lfu_cache):
    # Assert
    assert lfu_cache
    assert lfu_cache.size == 0
    assert lfu_cache.capacity == 2
