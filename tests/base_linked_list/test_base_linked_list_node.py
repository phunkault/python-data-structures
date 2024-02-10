from src.shared.base_linked_list_node import BaseLinkedListNode

test_node1 = BaseLinkedListNode(1)


def test_creates_node_with_value():
    # Assert
    assert test_node1.data == 1
    assert test_node1.next is None


def test_to_string():
    # Act and Assert
    assert str(test_node1) == "1"


def test_nodes_link_together():
    # Arrange and Act
    test_node0 = BaseLinkedListNode(0, test_node1)

    # Assert
    assert test_node0.next == test_node1
    assert test_node1.next is None
    assert test_node0.data == 0
    assert test_node0.next.data == 1
