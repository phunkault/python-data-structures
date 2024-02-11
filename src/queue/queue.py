from typing import Any, Optional

from src.linked_list.linked_list import LinkedList


class Queue:
    def __init__(self) -> None:
        self._list: LinkedList = LinkedList()

    def __str__(self) -> str:
        return str(self._list)

    @property
    def size(self) -> int:
        return self._list.length

    @property
    def is_empty(self) -> bool:
        return self._list.is_empty

    def enqueue(self, value: Any):
        self._list.append(value)

    def dequeue(self) -> Optional[Any]:
        dequeued_node = self._list.delete_head()
        return dequeued_node.data if dequeued_node else None

    def peek(self) -> Optional[Any]:
        front_element = self._list.head
        return front_element.data if front_element else None
