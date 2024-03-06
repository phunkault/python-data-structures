import pytest

from src.mfu_cache.mfu_cache import MFUCache


# Arrange
@pytest.fixture()
def mfu_cache_cap_2():
    return MFUCache(2)


@pytest.fixture()
def mfu_cache_cap_3():
    return MFUCache(3)


# Initial state
def test_mfu_cache_initial_state(mfu_cache_cap_2):
    # Assert
    assert mfu_cache_cap_2
    assert mfu_cache_cap_2.size == 0
    assert mfu_cache_cap_2.capacity == 2
    assert mfu_cache_cap_2.max_freq == 1


# Put
def test_put_in_empty_mfu_cache(mfu_cache_cap_2):
    # Act
    mfu_cache_cap_2.put("one", 1)

    # Assert
    assert mfu_cache_cap_2.size == 1
    assert mfu_cache_cap_2.max_freq == 1


def test_put_in_non_loaded_cache(mfu_cache_cap_2):
    # Arrange
    mfu_cache_cap_2.put("one", 1)

    # Act
    mfu_cache_cap_2.put("two", 2)

    # Assert
    assert mfu_cache_cap_2.size == 2
    assert mfu_cache_cap_2.max_freq == 1


def test_put_in_loaded_mfu_cache(mfu_cache_cap_2):
    # Arrange
    mfu_cache_cap_2.put("one", 1)
    mfu_cache_cap_2.put("two", 2)

    # Act
    mfu_cache_cap_2.put("three", 3)

    # Assert
    assert mfu_cache_cap_2.size == 2
    assert mfu_cache_cap_2.max_freq == 1


def test_put_three_nodes_and_override_values(mfu_cache_cap_2):
    mfu_cache_cap_2.put("one", 1)
    mfu_cache_cap_2.put("two", 2)

    mfu_cache_cap_2.put("one", 11)
    mfu_cache_cap_2.put("two", 22)

    # Act
    mfu_cache_cap_2.put("three", 3)

    # Assert
    assert mfu_cache_cap_2.max_freq == 2
    assert mfu_cache_cap_2.to_array() == ["three", "two"]


def test_put_same_key_in_mfu_cache_overrides_value(mfu_cache_cap_2):
    # Arrange
    mfu_cache_cap_2.put("one", 1)

    # Act
    mfu_cache_cap_2.put("one", 10)

    # Assert
    assert mfu_cache_cap_2.size == 1
    assert mfu_cache_cap_2.max_freq == 2


def test_put_in_mfu_cache_call_chain(mfu_cache_cap_2):
    # Act
    mfu_cache_cap_2.put("one", 1).put("two", 2)
    # Assert
    assert mfu_cache_cap_2.size == 2
    assert mfu_cache_cap_2.max_freq == 1


# Get
def test_get_existing_node_value(mfu_cache_cap_2):
    # Arrange
    mfu_cache_cap_2.put("one", 1)

    # Act and assert
    assert mfu_cache_cap_2.get("one") == 1
    assert mfu_cache_cap_2.size == 1
    assert mfu_cache_cap_2.max_freq == 2


def test_get_non_existing_node_value(mfu_cache_cap_2):
    # Assert
    assert not mfu_cache_cap_2.get("one")
    assert mfu_cache_cap_2.size == 0


def test_get_all_existing_node_values(mfu_cache_cap_2):
    # Arrange
    mfu_cache_cap_2.put("one", 1).put("two", 2)

    # Act and assert
    assert mfu_cache_cap_2.get("one") == 1
    assert mfu_cache_cap_2.get("two") == 2

    assert mfu_cache_cap_2.max_freq == 2


def test_mfu_three_nodes_updates_max_freq_correctly(mfu_cache_cap_3):
    # Arrange
    mfu_cache_cap_3.put("one", 1)
    mfu_cache_cap_3.put("two", 2)
    mfu_cache_cap_3.put("three", 3)

    # Act
    mfu_cache_cap_3.put("three", 33)
    mfu_cache_cap_3.put("four", 4)

    # Assert
    assert mfu_cache_cap_3.max_freq == 1
    assert mfu_cache_cap_3.to_array() == ["one", "two", "four"]
