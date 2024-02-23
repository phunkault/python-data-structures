from __future__ import annotations

from typing import List, Any, Optional


class Heap:
    """Base Heap class"""

    pass

    def __init__(self) -> None:
        self._container: List[Any] = []
        self._size: int = 0
        self._is_empty: bool = True

    def __str__(self) -> str:
        return str(self._container)

    @property
    def container(self) -> List[Any]:
        return self._container

    @property
    def size(self) -> int:
        return len(self._container)

    @property
    def is_empty(self) -> bool:
        return True if self._size == 0 else False

    @staticmethod
    def _get_left_child_index(parent_index: int) -> int:
        return 2 * parent_index + 1

    @staticmethod
    def _get_right_child_index(parent_index: int) -> int:
        return 2 * parent_index + 2

    @staticmethod
    def _get_parent_index(child_index: int) -> int:
        return (child_index - 1) // 2

    def _has_left_child(self, parent_index: int) -> bool:
        return self._get_left_child_index(parent_index) < len(self.container)

    def _has_right_child(self, parent_index: int) -> bool:
        return self._get_right_child_index(parent_index) < len(self.container)

    def _has_parent(self, index: int) -> bool:
        return self._get_parent_index(index) >= 0

    def _get_left_child(self, parent_index: int) -> Any:
        return self.container[self._get_left_child_index(parent_index)]

    def _get_right_child(self, parent_index: int) -> Any:
        return self.container[self._get_right_child_index(parent_index)]

    def _get_parent(self, child_index: int) -> Any:
        if not self._has_parent(child_index):
            return None

        return self.container[self._get_parent_index(child_index)]

    def _swap(self, first_idx: int, second_idx: int) -> None:
        if first_idx >= self.size:
            raise IndexError(f"{first_idx} is out of heap.")
        elif second_idx >= self.size:
            raise IndexError(f"{second_idx} is out of heap.")
        else:
            tmp = self.container[first_idx]
            self.container[first_idx] = self.container[second_idx]
            self.container[second_idx] = tmp

    def peek(self) -> Any:
        return self._container[0] if not self._is_empty else None

    def find(self, value: Any) -> List[int]:
        found_indices = []

        for el in self.container:
            if el == value:
                found_indices.append(self.container.index(el))

        return found_indices

    def push(self, value: Any) -> Heap:
        self._container.append(value)
        self.heapify_up()

        return self

    def replace(self) -> Any:
        if not self.container:
            return None

        if self.size == 1:
            return self.container.pop()

        replaced = self.container[0]

        self.container[0] = self.container.pop()
        self.heapify_down()

        return replaced

    def heapify_up(self, custom_start_index: Optional[int] = None) -> None:
        cur_idx = custom_start_index or len(self.container) - 1

        while self._has_parent(cur_idx) and not self._correct_order(
            self._get_parent(cur_idx), self.container[cur_idx]
        ):
            self._swap(cur_idx, self._get_parent_index(cur_idx))
            cur_idx = self._get_parent_index(cur_idx)

    def heapify_down(self) -> None:
        cur_idx = 0

        while self._has_left_child(cur_idx):
            if self._has_right_child(cur_idx) and self._correct_order(
                self._get_right_child(cur_idx), self._get_left_child(cur_idx)
            ):
                next_index = self._get_right_child_index(cur_idx)
            else:
                next_index = self._get_left_child_index(cur_idx)

            if self._correct_order(
                self.container[cur_idx], self.container[next_index]
            ):
                break

            self._swap(cur_idx, next_index)

            cur_idx = next_index

    def remove(self):
        pass

    def merge(self):
        pass

    def _correct_order(self, first_element, second_element):
        pass
