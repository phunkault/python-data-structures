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


# Put
def test_put_in_empty_mfu_cache(mfu_cache):
    # Act
    mfu_cache.put("one", 1)

    # Assert
    assert mfu_cache.size == 1


def test_put_in_non_loaded_cache(mfu_cache):
    # Arrange
    mfu_cache.put("one", 1)
    mfu_cache.put("two", 2)

    # Act
    mfu_cache.put("three", 3)

    # Assert
    assert mfu_cache.size == 3


def test_put_in_loaded_mfu_cache(mfu_cache):
    # Arrange
    mfu_cache.put("one", 1)
    mfu_cache.put("two", 2)
    mfu_cache.put("three", 3)

    # Act
    mfu_cache.put("four", 4)

    # Assert
    assert mfu_cache.size == 3


def test_put_same_key_in_mfu_cache_renews_value(mfu_cache):
    # Arrange
    mfu_cache.put("one", 1)

    # Act
    mfu_cache.put("one", 10)

    # Assert
    assert mfu_cache.size == 1


def test_put_in_mfu_cache_call_chain(mfu_cache):
    # Act
    mfu_cache.put("one", 1).put("two", 2).put("three", 3)

    # Assert
    assert mfu_cache.size == 3


# Get
def test_get_existing_node_value(mfu_cache):
    # Arrange
    mfu_cache.put("one", 1)

    # Act and assert
    assert mfu_cache.get("one") == 1
    assert mfu_cache.size == 1


def test_get_non_existing_node_value(mfu_cache):
    # Assert
    assert not mfu_cache.get("one")
    assert mfu_cache.size == 0


def test_get_all_existing_node_values(mfu_cache):
    # Arrange
    mfu_cache.put("one", 1).put("two", 2).put("three", 3)

    # Act and assert
    assert mfu_cache.get("one") == 1
    assert mfu_cache.get("two") == 2
    assert mfu_cache.get("three") == 3


# Update frequency
def test_update_frequency(mfu_cache):
    # Arrange
    mfu_cache.put("one", 1).put("two", 2).put("three", 3)

    cache_str = "Freq 1: one, 1 -> two, 2 -> three, 3\n"
    assert str(mfu_cache) == cache_str

    mfu_cache.get("one")
    mfu_cache.get("two")
    mfu_cache.get("three")

    cache_str = "Freq 1: \nFreq 2: one, 1 -> two, 2 -> three, 3\n"
    assert str(mfu_cache) == cache_str

    # Act
    mfu_cache.get("three")

    cache_str = "Freq 1: \nFreq 2: one, 1 -> two, 2\nFreq 3: three, 3\n"
    assert str(mfu_cache) == cache_str

    mfu_cache.put("four", 4)

    cache_str = "Freq 1: four, 4\nFreq 2: one, 1 -> two, 2\nFreq 3: \n"
    assert str(mfu_cache) == cache_str
