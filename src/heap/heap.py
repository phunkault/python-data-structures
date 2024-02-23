from typing import List, Any


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
        return self._size

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

    def get_parent(self, child_index: int) -> Any:
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

    def heapify(self, target: List[int]) -> List[Any]:
        pass

    def push(self):
        pass

    def pop(self):
        pass

    def replace(self):
        pass

    def remove(self):
        pass

    def merge(self):
        pass
