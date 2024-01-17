class LinkedListNode:
    def __init__(self, value=None, next=None) -> None:
        self.value = value
        self.next = next

    def __str__(self) -> str:
        return f"LinkedListNode({self.value})"

    def __eq__(self, other) -> bool:
        if isinstance(other, LinkedListNode):
            return self.value == other.value and self.next == other.next
        return False
