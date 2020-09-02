from linkedlist import LinkedList


def test_insertAtHead_method_adds_node_at_beginning_of_list():
    ll = LinkedList()
    ll.insertAtHead("10")
    ll.insertAtHead("20")
    assert ll.head.value == "20"
    assert ll.head.next.value == "10"
    assert ll.length == 2


def test_getByIndex_method_returns_None():
    ll = LinkedList()
    ll.insertMultipleValues(50, 40, 30, 20, 10)
    e = ll.getByIndex(-1)
    assert e is None
    e = ll.getByIndex(5)
    assert e is None


def test_getByIndex_method_returns_Node_value():
    ll = LinkedList()
    ll.insertMultipleValues(10, 20, 30, 40, 50)
    e = ll.getByIndex(0)
    assert e.value == 10
    e = ll.getByIndex(1)
    assert e.value == 20
    e = ll.getByIndex(4)
    assert e.value == 50


def test_insertAtIndex_method_with_index_less_than_0():
    ll = LinkedList()
    ll.insertMultipleValues(10, 20, 30, 40)
    ll.insertAtIndex(-1, 666)
    assert ll.length == 4


def test_insertAtIndex_method_with_index_greater_than_list_length():
    ll = LinkedList()
    ll.insertMultipleValues(10, 20, 30, 40)
    ll.insertAtIndex(666, 666)
    assert ll.length == 4


def test_insertAtIndex_method_with_index_0():
    ll = LinkedList()
    ll.insertMultipleValues(10, 20, 30, 40)
    ll.insertAtIndex(0, 44)
    assert ll.head.value == 44
    assert ll.head.next.value == 10
    assert ll.length == 5


def test_insertAtIndex_method_with_index_in_middle():
    ll = LinkedList()
    ll.insertMultipleValues(10, 20, 30, 40)
    ll.insertAtIndex(2, 44)
    assert ll.head.value == 10
    assert ll.head.next.value == 20
    assert ll.head.next.next.value == 44
    assert ll.length == 5


def test_insertAtIndex_method_with_index_at_end():
    ll = LinkedList()
    ll.insertMultipleValues(10, 20, 30, 40)
    ll.insertAtIndex(4, 44)
    assert ll.head.value == 10
    assert ll.head.next.value == 20
    assert ll.getByIndex(4).value == 44
    assert ll.length == 5


def test_removeAtHead_method():
    ll = LinkedList()
    ll.insertMultipleValues(10, 20, 30, 40)
    ll.removeAtHead()
    assert ll.head.value == 20
    assert ll.length == 3


def test_removeAtIndex_method_with_index_less_than_0():
    ll = LinkedList()
    ll.insertMultipleValues(10, 20, 30, 40)
    ll.removeAtIndex(-1)
    assert ll.head.value == 10
    assert ll.length == 4


def test_removeAtIndex_method_with_index_greater_than_list_length():
    ll = LinkedList()
    ll.insertMultipleValues(10, 20, 30, 40)
    ll.removeAtIndex(5)
    assert ll.head.value == 10
    assert ll.length == 4


def test_removeAtIndex_method_with_index_0():
    ll = LinkedList()
    ll.insertMultipleValues(10, 20, 30, 40)
    ll.removeAtIndex(0)
    assert ll.head.value == 20
    assert ll.length == 3


def test_removeAtIndex_method_with_index_in_middle():
    ll = LinkedList()
    ll.insertMultipleValues(10, 20, 30, 40)
    ll.removeAtIndex(2)
    assert ll.head.value == 10
    assert ll.head.next.value == 20
    assert ll.getByIndex(2).value == 40
    assert ll.length == 3


def test_removeAtIndex_method_with_index_at_end():
    ll = LinkedList()
    ll.insertMultipleValues(10, 20, 30, 40)
    ll.removeAtIndex(3)
    assert ll.head.value == 10
    assert ll.head.next.value == 20
    assert ll.getByIndex(3) is None
    assert ll.length == 3
