from src.doubly_linked_list.doubly_linked_list import DoublyLinkedList


class Dequeue:
    def __init__(self) -> None:
        self._list: DoublyLinkedList = DoublyLinkedList()

    @property
    def size(self) -> int:
        return self._list.length

    @property
    def is_empty(self) -> bool:
        return self._list.is_empty
