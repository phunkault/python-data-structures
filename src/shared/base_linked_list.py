from __future__ import annotations
from abc import ABC, abstractmethod
from typing import Optional, Any, List

from .base_linked_list_node import BaseLinkedListNode


class BaseLinkedList(ABC):
    _head: Optional[BaseLinkedListNode] = None
    _tail: Optional[BaseLinkedListNode] = None
    _length: int = 0

    @property
    def head(self) -> Optional[BaseLinkedListNode]:
        return self._head

    @property
    def tail(self) -> Optional[BaseLinkedListNode]:
        return self._tail

    @property
    def length(self) -> int:
        return self._length

    @property
    def is_empty(self) -> bool:
        return self._head is None

    def _find_node_by_index(self, index) -> Optional[BaseLinkedListNode]:
        current_node = self._head

        for i in range(index):
            current_node = current_node.next

        return current_node

    def __iter__(self) -> None:
        current_node = self._head
        while current_node is not None:
            yield current_node
            current_node = current_node.next

    def __str__(self, separator: str = " -> ") -> str:
        values = [str(value) for value in self.to_array()]

        return f"{separator}".join(values)

    def _is_match(self, value: Any, arg: Any) -> bool:
        if callable(arg):
            return arg(value)
        else:
            return value == arg

    def from_array(self, array) -> BaseLinkedList:
        for value in array:
            self.append(value)

        return self

    def to_array(self) -> List:
        return [node.data for node in self]

    def find(self, arg: Any) -> Optional[BaseLinkedListNode]:
        if not self.head:
            return None

        for current_node in self:
            if self._is_match(current_node.data, arg):
                return current_node

        return None

    def index_of(self, value) -> int:
        index = 0

        for node in self:
            if node.data == value:
                return index
            index += 1

        return -1

    def clear(self) -> None:
        self._head = None
        self._tail = None
        self._length = 0

    @abstractmethod
    def append(self, value):
        pass

    @abstractmethod
    def prepend(self, value):
        pass

    @abstractmethod
    def insert_at(self, index, value):
        pass

    @abstractmethod
    def delete(self, value):
        pass

    @abstractmethod
    def delete_head(self):
        pass

    @abstractmethod
    def delete_tail(self):
        pass

    @abstractmethod
    def reverse(self):
        pass
