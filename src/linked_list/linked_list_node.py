class LinkedListNode:
    def __init__(self, value=None, next=None) -> None:
        self.value = value
        self.next = next

    def __str__(self) -> str:
        return f"LinkedListNode({self.value})"
