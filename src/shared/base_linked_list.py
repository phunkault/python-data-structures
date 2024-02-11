from __future__ import annotations
from abc import ABC, abstractmethod
from typing import Optional, Any, List
from types import FunctionType

from .base_linked_list_node import BaseLinkedListNode


class BaseLinkedList(ABC):
    _head: Optional[BaseLinkedListNode] = None
    _tail: Optional[BaseLinkedListNode] = None
    _length: int = 0

    @staticmethod
    def _is_match(value: Any, arg: Any) -> bool:
        if type(arg) == FunctionType:
            return arg(value)
        else:
            return value == arg

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
        return not self._head

    def _find_node_by_index(self, index: int) -> Optional[BaseLinkedListNode]:
        current_node = self.head

        for i in range(index):
            current_node = current_node.next

        return current_node

    def __iter__(self) -> None:
        current_node = self._head
        while current_node:
            yield current_node
            current_node = current_node.next

    def __str__(self, separator: str = " -> ") -> str:
        values = [str(value) for value in self.to_array()]

        return f"{separator}".join(values)

    def from_array(self, array: List) -> BaseLinkedList:
        for value in array:
            self.append(value)

        return self

    def to_array(self) -> List:
        return [node.data for node in self]

    def find(self, value: Any) -> Optional[BaseLinkedListNode]:
        if not self.head:
            return None

        for current_node in self:
            if BaseLinkedList._is_match(current_node.data, value):
                return current_node

        return None

    def index_of(self, value: Any) -> int:
        index = 0

        for node in self:
            if BaseLinkedList._is_match(node.data, value):
                return index

            index += 1

        return -1

    def clear(self) -> None:
        self._head = None
        self._tail = None
        self._length = 0

    @abstractmethod
    def append(self, value: Any) -> BaseLinkedList:
        pass

    @abstractmethod
    def prepend(self, value: Any) -> BaseLinkedList:
        pass

    @abstractmethod
    def insert_at(self, index: int, value: Any) -> BaseLinkedList:
        pass

    @abstractmethod
    def delete(self, value: Any) -> Optional[BaseLinkedListNode]:
        pass

    @abstractmethod
    def delete_head(self) -> Optional[BaseLinkedListNode]:
        pass

    @abstractmethod
    def delete_tail(self) -> Optional[BaseLinkedListNode]:
        pass

    @abstractmethod
    def reverse(self) -> BaseLinkedList:
        pass
