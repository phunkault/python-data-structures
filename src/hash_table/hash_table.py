from __future__ import annotations

from typing import Any, Optional

from src.linked_list.linked_list import LinkedList

INITIAL_CAPACITY = 8
RESIZE_THRESHOLD = 0.7


class KeyValuePair:
    def __init__(self, key: Any, value: Any) -> None:
        self.key = key
        self.value = value


class HashMap:
    def __init__(self, capacity: int = INITIAL_CAPACITY) -> None:
        self._capacity = capacity
        self._buckets: list[LinkedList] = HashMap._create_buckets()
        self._size: int = 0

    @staticmethod
    def _create_buckets(capacity: int = INITIAL_CAPACITY) -> list[LinkedList]:
        buckets = [LinkedList() for _ in range(capacity)]
        return buckets

    @property
    def size(self) -> int:
        return self._size

    @staticmethod
    def _hash_code(key: Any) -> int:
        hash_string = str(key)

        prime = 31
        hash_code = 0

        i = 0
        while i < len(hash_string):
            code_point = ord(hash_string[i])

            # Invalid Unicode character.
            if not code_point:
                break

            hash_code = hash_code * prime + code_point

            # Move to the next code point.
            i += 2 if code_point >= 0x10000 else 1

        return hash_code

    @staticmethod
    def _get_index(hash_value: int, buckets_len: int) -> int:
        return hash_value % buckets_len

    def _find_bucket_by_key(self, key: Any) -> Any:
        hash_value = HashMap._hash_code(key)
        index = HashMap._get_index(hash_value, self._capacity)
        return self._buckets[index]

    def _is_loaded(self):
        load_factor = self._size / len(self._buckets)
        return load_factor > RESIZE_THRESHOLD

    def _resize_if_needed(self) -> None:
        if not self._is_loaded():
            return

        new_capacity = self._capacity * 2
        new_buckets = HashMap._create_buckets(new_capacity)

        # Rehash existing key-value pairs into the new buckets
        for bucket in self._buckets:
            for node in bucket:
                new_hash_value = HashMap._hash_code(node.data.key)
                new_index = self._get_index(new_hash_value, new_capacity)
                new_buckets[new_index].append(
                    KeyValuePair(node.data.key, node.data.value)
                )

        self._buckets = new_buckets
        self._capacity = new_capacity

    def set(self, key: Any, value: Any) -> HashMap:
        self._resize_if_needed()

        bucket = self._find_bucket_by_key(key)

        existing_node = bucket.find(lambda node: node.key == key)

        if existing_node:
            existing_node.data.value = value
        else:
            bucket.append(KeyValuePair(key, value))
            self._size += 1

        return self

    def keys(self) -> Any:
        for bucket in self._buckets:
            for node in bucket:
                yield node.data.key

    def values(self) -> Any:
        for bucket in self._buckets:
            for node in bucket:
                yield node.data.value

    def items(self) -> Any:
        for bucket in self._buckets:
            for node in bucket:
                yield node.data.key, node.data.value

    def get(self, key: Any) -> Optional[Any]:
        bucket = self._find_bucket_by_key(key)

        if not bucket:
            return None

        node = bucket.find(lambda pair: pair.key == key)

        return node.data.value if node else None

    def has(self, key: Any) -> bool:
        bucket = self._find_bucket_by_key(key)

        node = bucket.find(lambda pair: pair.key == key)

        return bool(node)

    def delete(self, key: Any) -> bool:
        bucket = self._find_bucket_by_key(key)

        if bucket:
            deleted_node = bucket.delete(lambda pair: pair.key == key)

            if deleted_node:
                self._size -= 1

                return True

        return False

    def clear(self) -> None:
        self._capacity = INITIAL_CAPACITY
        self._buckets = self._create_buckets()
        self._size = 0
