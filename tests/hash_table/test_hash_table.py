import pytest
from src.hash_table.hash_table import HashMap


# Arrange
@pytest.fixture
def hash_map():
    return HashMap()


# Initial state
def test_initial_state(hash_map):
    # Assert
    assert hash_map.size == 0


# Set
def test_set_values(hash_map):
    # Act
    hash_map.set("one", 1)
    hash_map.set("two", 2)

    received = dict(hash_map.items())
    expected = {"one": 1, "two": 2}

    # Assert
    assert received == expected


def test_update_existing_values(hash_map):
    # Act
    hash_map.set("one", 1)
    hash_map.set("one", 2)

    # Assert
    received = dict(hash_map.items())
    expected = {"one": 2}

    assert received == expected


# Keys
def test_keys_returns_iterator_with_all_keys(hash_map):
    # Arrange
    hash_map.set("one", 1)
    hash_map.set("two", 2)
    hash_map.set("three", 3)

    received = list(hash_map.keys())

    # Assert
    assert "one" in received
    assert "two" in received
    assert "three" in received


def test_keys_returns_empty_iterator_for_empty_hash_map(hash_map):
    # Act
    empty_keys_iterator = hash_map.keys()

    # Assert
    assert list(empty_keys_iterator) == []


def test_keys_returns_unique_keys_even_with_duplicate_items(hash_map):
    # Arrange
    hash_map.set("one", 1)
    hash_map.set("two", 2)
    hash_map.set("one", 3)

    # Act
    keys_list = list(hash_map.keys())

    # Assert

    assert len(keys_list) == 2
    assert "one" in keys_list
    assert "two" in keys_list


def test_keys_returns_iterator_with_all_keys_including_colliding_keys(hash_map):
    # Arrange
    # hash_map = HashMap(5)
    hash_map.set("one", 1)
    hash_map.set("two", 2)
    hash_map.set("three", 3)
    hash_map.set("neo", 4)  # Collision with 'one'

    # Act
    keys_list = list(hash_map.keys())

    # Assert
    assert len(keys_list) == 4

    assert "one" in keys_list
    assert "two" in keys_list
    assert "three" in keys_list
    assert "neo" in keys_list


def test_keys_returns_iterator_with_colliding_entries(hash_map):
    # Arrange
    # hash_map = HashMap(5)
    hash_map.set("one", 1)
    hash_map.set("two", 2)
    hash_map.set("three", 3)
    hash_map.set("neo", 4)  # Collision with 'one'
    hash_map.set("one", 5)  # Addition with the same collision-causing key

    # Act
    keys_list = list(hash_map.keys())

    # Assert
    assert len(keys_list) == 4

    assert "one" in keys_list
    assert "two" in keys_list
    assert "three" in keys_list
    assert "neo" in keys_list


# Values
def test_values_returns_iterator_with_all_values(hash_map):
    # Arrange
    hash_map.set("one", 1)
    hash_map.set("two", 2)
    hash_map.set("three", 3)

    # Act
    values_list = list(hash_map.values())

    # Assert
    assert 1 in values_list
    assert 2 in values_list
    assert 3 in values_list


def test_values_returns_empty_iterator_for_empty_hash_map(hash_map):
    # Act and Assert
    assert list(hash_map.values()) == []


# Items
def test_items_returns_iterator_with_all_items(hash_map):
    # Arrange
    hash_map.set("one", 1)
    hash_map.set("two", 2)
    hash_map.set("three", 3)

    # Act
    items_list = list(hash_map.items())

    # Assert
    assert ("one", 1) in items_list
    assert ("two", 2) in items_list
    assert ("three", 3) in items_list


def test_items_returns_empty_iterator_for_empty_hash_map(hash_map):
    # Act and Assert
    assert list(hash_map.items()) == []


# Get
def test_get_handles_non_existing_key_in_empty_hash_map(hash_map):
    # Act and Assert
    assert not hash_map.get("one")
    assert hash_map.size == 0


def test_get_handles_non_existing_key_in_non_empty_hash_map(hash_map):
    hash_map.set("one", 1)

    # Act and Assert
    assert not hash_map.get("two")
    assert hash_map.size == 1


def test_get_returns_value_for_existing_key_in_non_empty_hash_map(hash_map):
    # Arrange
    hash_map.set("one", 1)

    # Act and Assert
    assert hash_map.get("one") == 1
    assert hash_map.size == 1


# Has
def test_has_checks_if_key_exists_using_has_method(hash_map):
    # Arrange
    hash_map.set("one", 1)
    hash_map.set("two", 2)

    # Act and Assert
    assert hash_map.size == 2
    assert hash_map.has("one")
    assert hash_map.has("two")
    assert not hash_map.has("three")


# Delete
def test_delete_none_existing_value_in_an_empty_hash_map(hash_map):
    # Act and Assert
    assert hash_map.size == 0
    assert not hash_map.delete("one")


def test_delete_existing_values_for_existing_keys_in_a_non_empty_hash_map(hash_map):
    # Arrange
    hash_map.set("one", 1)
    hash_map.set("two", 2)

    # Act and Assert
    assert hash_map.delete("one")
    assert hash_map.size == 1
    assert hash_map.delete("two")
    assert hash_map.size == 0


# Clear
def test_clears_the_hash_map(hash_map):
    # Arrange
    hash_map.set("one", 1)
    hash_map.set("two", 2)

    # Act
    hash_map.clear()

    # Assert
    assert not hash_map.get("one")
    assert not hash_map.get("two")
    assert hash_map.size == 0


# Resize
def test_resize_on_overflow(hash_map):
    # Arrange
    hash_map.set("one", 1)
    hash_map.set("two", 2)
    hash_map.set("three", 3)
    hash_map.set("four", 4)
    hash_map.set("five", 5)
    hash_map.set("six", 6)

    # Act
    hash_map.set("seven", 7)

    # Assert
    assert hash_map.get("one") == 1
    assert hash_map.get("two") == 2
    assert hash_map.get("three") == 3
    assert hash_map.get("four") == 4
    assert hash_map.get("five") == 5
    assert hash_map.get("six") == 6
    assert hash_map.get("seven") == 7

    assert hash_map.size == 7

    assert hash_map._capacity == 16
