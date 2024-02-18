import pytest

from src.lru_cache.lru_cache import LRUCache


# Arrange
@pytest.fixture
def lru_cache():
    return LRUCache(3)


# Initial state
def test_lru_cache_initial_state(lru_cache):
    # Assert
    assert lru_cache
    assert lru_cache.size == 0
    assert lru_cache.capacity == 3
    assert lru_cache.list.is_empty
    assert not lru_cache.node_map
