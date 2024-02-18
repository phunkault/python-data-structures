from src.doubly_linked_list.doubly_linked_list import DoublyLinkedList


class LRUCache:
    def __init__(self, capacity: int) -> None:
        self.size: int = 0
        self.capacity = capacity
        self.list: DoublyLinkedList = DoublyLinkedList()
        self.node_map: dict = {}
