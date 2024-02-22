import pytest

from src.lfu_cache.lfu_cache import LFUCache


# Arrange
@pytest.fixture()
def lfu_cache():
    return LFUCache()


# Initial state
def test_lfu_cache_initial_state(lfu_cache):
    # Assert
    assert lfu_cache
    assert lfu_cache.size == 0
    assert lfu_cache.capacity == 3


# Put
def test_put_in_non_loaded_cache(lfu_cache):
    # Arrange
    lfu_cache.put("one", 1)
    lfu_cache.put("two", 2)

    # Act
    lfu_cache.put("three", 3)

    # Assert
    assert lfu_cache.size == 3
    assert lfu_cache.capacity == 3

    assert lfu_cache.get("one") == 1
    assert lfu_cache.get("two") == 2
    assert lfu_cache.get("three") == 3


def test_put_in_loaded_cache(lfu_cache):
    # Arrange
    lfu_cache.put("one", 1)
    lfu_cache.put("two", 2)
    lfu_cache.put("three", 3)
    # Act

    lfu_cache.put("four", 4)
    # Assert

    assert lfu_cache.size == 3
    assert lfu_cache.capacity == 3

    assert not lfu_cache.get("one")
    assert lfu_cache.get("two") == 2
    assert lfu_cache.get("three") == 3
    assert lfu_cache.get("four") == 4


# Get
def test_get_non_existing_key(lfu_cache):
    # Arrange
    lfu_cache.put("one", 1)

    # Act and Assert
    assert not lfu_cache.get("two")


def test_get_existing_key(lfu_cache):
    # Arrange
    lfu_cache.put("one", 1)

    # Act and Assert
    assert lfu_cache.get("one") == 1


def test_get_node_two_times(lfu_cache):
    # Arrange
    lfu_cache.put("three", 3)
    lfu_cache.put("seven", 7)
    lfu_cache.put("eleven", 11)

    assert str(lfu_cache) == "Cache:\nFreq 1: (three, 3) -> (seven, 7) -> (eleven, 11)\n"

    # Act and assert
    assert lfu_cache.get("three") == 3
    assert lfu_cache.get("seven") == 7
    assert lfu_cache.get("eleven") == 11

    assert str(lfu_cache) == "Cache:\nFreq 1: \nFreq 2: (three, 3) -> (seven, 7) -> (eleven, 11)\n"

    lfu_cache.get("eleven")

    assert lfu_cache.size == 3

    lfu_cache.put("one", 1)

    assert str(lfu_cache) == "Cache:\nFreq 1: (one, 1)\nFreq 2: (seven, 7)\nFreq 3: (eleven, 11)\n"
