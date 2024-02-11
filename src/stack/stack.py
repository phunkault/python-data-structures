from src.linked_list.linked_list import LinkedList


class Stack:
    def __init__(self):
        self._list = LinkedList()
        self._size = 0

    @property
    def size(self) -> int:
        return self._size

    @property
    def is_empty(self) -> bool:
        return self._list.is_empty
