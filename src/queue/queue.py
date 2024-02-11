from src.linked_list.linked_list import LinkedList


class Queue:
    def __init__(self) -> None:
        self._list: LinkedList = LinkedList()

    @property
    def size(self) -> int:
        return self._list.length
