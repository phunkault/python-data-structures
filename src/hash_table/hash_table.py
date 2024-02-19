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
        self._buckets: list[LinkedList] = [
            LinkedList() for _ in range(self._capacity)
        ]
        self._size: int = 0

    @property
    def size(self) -> int:
        return self._size

    def _hash_value(self, key: Any) -> int:
        hash_string = str(key)

        prime = 31
        hash_value = 0

        i = 0
        while i < len(hash_string):
            code_point = ord(hash_string[i])

            # Invalid Unicode character.
            if not code_point:
                break

            hash_value = hash_value * prime + code_point

            # Move to the next code point.
            i += 2 if code_point >= 0x10000 else 1

        return hash_value

    def _hash_code(self, hash_value: int, buckets_len: int) -> int:
        return hash_value % buckets_len

    def _resize_if_needed(self) -> None:
        load_factor = self._size / len(self._buckets)

        if load_factor < RESIZE_THRESHOLD:
            return

        new_capacity = self._capacity * 2
        new_buckets = [LinkedList() for _ in range(new_capacity)]

        # Rehash existing key-value pairs into the new buckets
        for bucket in self._buckets:
            for node in bucket:
                new_hash_value = self._hash_value(node.data.key)
                new_index = self._hash_code(new_hash_value, new_capacity)
                new_buckets[new_index].append(
                    KeyValuePair(node.data.key, node.data.value)
                )

        self._buckets = new_buckets
        self._capacity = new_capacity

    def set(self, key: Any, value: Any) -> HashMap:
        self._resize_if_needed()

        hash_val = self._hash_value(key)
        hash_code = self._hash_code(
            hash_value=hash_val, buckets_len=self._capacity
        )
        bucket = self._buckets[hash_code]
        existing_node = bucket.find(lambda node: node.key == key)

        if existing_node:
            existing_node.data.value = value
        else:
            bucket.append(KeyValuePair(key, value))
            self._size += 1

            if not self._buckets[hash_code]:
                self._buckets[hash_code] = bucket

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

    def _find_bucket_by_key(self, key: Any) -> Any:
        hash_value = self._hash_value(key)
        index = self._hash_code(hash_value, self._capacity)
        return self._buckets[index]

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

    def delete(self, key) -> bool:
        hash_value = self._hash_value(key)
        hash_code = self._hash_code(hash_value, self._capacity)
        # hash_value = self._hash_code(key)
        bucket = self._buckets[hash_code]

        if bucket:
            deleted_node = bucket.delete(lambda pair: pair.key == key)

            if deleted_node:
                self._size -= 1
                return True

        return False

    def clear(self) -> None:
        self._capacity = INITIAL_CAPACITY
        self._buckets = [LinkedList() for _ in range(self._capacity)]
        self._size = 0
