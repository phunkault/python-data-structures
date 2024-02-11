from __future__ import annotations
from typing import Any
from src.linked_list.linked_list import LinkedList

INITIAL_CAPACITY = 10


class KeyValuePair:
    def __init__(self, key: Any, value: Any) -> None:
        self.key = key
        self.value = value


class HashMap:
    def __init__(self, capacity: int = INITIAL_CAPACITY) -> None:
        self._capacity = capacity
        self._buckets: list[LinkedList] = [
            LinkedList() for _ in range(self._capacity)
        ]
        self._size: int = 0

    @property
    def size(self) -> int:
        return self._size

    def _hash_code(self, key: Any):
        hash_string = str(key)

        prime = 31
        hash_value = 0

        i = 0
        while i < len(hash_string):
            code_point = ord(hash_string[i])

            # Invalid Unicode character.
            if code_point is None:
                break

            hash_value = (hash_value * prime + code_point) % len(self._buckets)

            # Move to the next code point.
            i += 2 if code_point >= 0x10000 else 1

        return hash_value

    def _resize_if_needed(self):
        RESIZE_THRESHOLD = 0.7
        load_factor = self._size / len(self._buckets)

        if load_factor < RESIZE_THRESHOLD:
            return

        new_capacity = self._capacity * 2
        new_buckets = [LinkedList() for _ in range(new_capacity)]

        # Rehash existing key-value pairs into the new buckets
        for bucket in self._buckets:
            for node in bucket:
                new_index = self._hash_code(node.data.key) % new_capacity
                new_buckets[new_index].append(
                    KeyValuePair(node.data.key, node.data.value)
                )

        self._buckets = new_buckets
        self._capacity = new_capacity

    def set(self, key: Any, value: Any) -> HashMap:
        self._resize_if_needed()

        hash_val = self._hash_code(key)
        bucket = self._buckets[hash_val] or LinkedList()
        existing_node = bucket.find(lambda node: node.key == key)

        if existing_node:
            existing_node.data.value = value
        else:
            bucket.append(KeyValuePair(key, value))
            self._size += 1

            if self._buckets[hash_val] is None:
                self._buckets[hash_val] = bucket

        return self

    def keys(self):
        for bucket in self._buckets:
            for node in bucket:
                yield node.data.key

    def values(self):
        for bucket in self._buckets:
            for node in bucket:
                yield node.data.value

    def items(self):
        for bucket in self._buckets:
            for node in bucket:
                yield node.data.key, node.data.value

    def _find_bucket_by_key(self, key: Any):
        index = self._hash_code(key)
        return self._buckets[index]

    def get(self, key: Any):
        bucket = self._find_bucket_by_key(key)

        if not bucket:
            return None

        node = bucket.find(lambda pair: pair.key == key)

        return node.data.value if node else None

    def has(self, key: Any):
        bucket = self._find_bucket_by_key(key)

        node = bucket.find(lambda pair: pair.key == key)

        return bool(node)

    def delete(self, key):
        hash_value = self._hash_code(key)
        bucket = self._buckets[hash_value]

        if bucket:
            deleted_node = bucket.delete(lambda pair: pair.key == key)

            if deleted_node:
                self._size -= 1
                return True

        return False
