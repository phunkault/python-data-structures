import pytest
from src.hash_table.hash_table import HashMap


# @pytest.fixture
# def hash_map():
#     return HashMap()


def test_initial_state():
    hash_map = HashMap()
    assert hash_map.size == 0


def test_set_values():
    hash_map = HashMap()
    # Act
    hash_map.set('one', 1)
    hash_map.set('two', 2)

    # Assert
    received = dict(hash_map.items())

    assert received == {
        'one': 1,
        'two': 2,
    }

    assert hash_map.size == 2


def test_update_existing_values():
    hash_map = HashMap()
    # Act
    hash_map.set('value', 1)
    hash_map.set('value', 2)

    # Assert
    assert hash_map.get('value') == 2


def test_keys_returns_iterator_with_all_keys():
    hash_map = HashMap()
    hash_map.set('one', 1)
    hash_map.set('two', 2)
    hash_map.set('three', 3)
    expected = ['one', 'two', 'three']

    # Act
    received = list(hash_map.keys())

    # Assert
    assert received == expected


def test_keys_returns_empty_iterator_for_empty_hash_map():
    # Arrange
    hash_map = HashMap()

    # Act
    empty_keys_iterator = hash_map.keys()

    # Assert
    assert list(empty_keys_iterator) == []
    assert len(list(empty_keys_iterator)) == 0


def test_keys_returns_unique_keys_even_with_duplicate_entries():
    # Arrange
    hash_map = HashMap()
    hash_map.set('one', 1)
    hash_map.set('two', 2)
    hash_map.set('one', 3)

    # Act
    keys_iterator = hash_map.keys()
    keys_array = list(keys_iterator)

    # Assert
    assert set(keys_array) == {'one', 'two'}
    assert len(keys_array) == 2


def test_keys_returns_iterator_with_all_keys_including_colliding_keys():
    # Arrange
    hash_map = HashMap(5)
    hash_map.set('one', 1)
    hash_map.set('two', 2)
    hash_map.set('three', 3)
    hash_map.set('neo', 4)  # Collision with 'one'

    # Act
    keys_iterator = hash_map.keys()
    keys_array = list(keys_iterator)

    # Assert
    assert set(keys_array) == {'one', 'two', 'three', 'neo'}
    assert len(keys_array) == 4


def test_keys_returns_iterator_with_all_unique_keys_for_colliding_entries():
    # Arrange
    hash_map = HashMap(5)
    hash_map.set('one', 1)
    hash_map.set('two', 2)
    hash_map.set('three', 3)
    hash_map.set('neo', 4)  # Collision with 'one'
    hash_map.set('one', 5)  # Addition with the same collision-causing key

    # Act
    keys_iterator = hash_map.keys()
    keys_array = list(keys_iterator)

    # Assert
    assert set(keys_array) == {'one', 'two', 'three', 'neo'}
    assert len(keys_array) == 4


def test_values_returns_iterator_with_all_values():
    # Arrange
    hash_map = HashMap()
    hash_map.set('one', 1)
    hash_map.set('two', 2)
    hash_map.set('three', 3)
    expected = [1, 2, 3]

    # Act
    received = list(hash_map.values())

    # Assert
    assert received == expected


def test_values_returns_empty_iterator_for_empty_hash_map():
    # Arrange
    hash_map = HashMap()

    # Act and Assert
    assert list(hash_map.values()) == []
