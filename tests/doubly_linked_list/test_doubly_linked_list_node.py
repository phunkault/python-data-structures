from src.doubly_linked_list.doubly_linked_list_node import DoublyLinkedListNode


def test_creates_node_with_value():
    # Arrange
    node = DoublyLinkedListNode(1)

    # Assert
    assert node.data == 1
    assert not node.next
    assert not node.prev


def test_nodes_link_together():
    # Arrange
    node2 = DoublyLinkedListNode(2)

    # Act
    node1 = DoublyLinkedListNode(1, next=node2)

    # Act
    node3 = DoublyLinkedListNode(3, next=node1, prev=node2)

    # Assert
    assert node1.data == 1
    assert node1.next.data == 2
    assert not node1.next.next
    assert not node1.prev

    assert not node2.next
    assert not node2.prev

    assert node3.next.data == 1
    assert node3.prev.data == 2
