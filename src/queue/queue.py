from src.linked_list.linked_list import LinkedList


class Queue:
    def __init__(self) -> None:
        self._list: LinkedList = LinkedList()

    @property
    def size(self) -> int:
        return self._list.length

    @property
    def is_empty(self):
        return self._list.is_empty
