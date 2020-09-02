class LinkedList:
    def __init__(self):
        self.head = None
        self.length = 0

    def insertAtHead(self, data):
        newNode = LinkedListNode(data, self.head)
        self.head = newNode
        self.length += 1

    def insertMultipleValues(self, *args):
        argsList = [a for a in args]
        argsList.reverse()
        for a in argsList:
            self.insertAtHead(a)

    def getByIndex(self, index):
        if index < 0 or index >= self.length:
            return
        current = self.head
        for i in range(index):
            current = current.next
        return current

    def print(self):
        current = self.head
        valueList = []
        for i in range(self.length):
            valueList.append(str(current.value))
            current = current.next
        print(" => ".join(valueList))

    def __str__(self):
        return "<LinkedList with {} elements>".format(self.length)

    def insertAtIndex(self, index, value):
        if index == 0:
            return self.insertAtHead(value)
        prev = self.getByIndex(index - 1)
        if prev is None:
            return None
        prev.next = LinkedListNode(value, prev.next)
        self.length += 1

    def removeAtHead(self):
        self.head = self.head.next
        self.length -= 1

    def removeAtIndex(self, index):
        if index == 0:
            self.removeAtHead()
        prev = self.getByIndex(index - 1)
        if prev is None:
            return None
        prev.next = prev.next.next  # toDelete.next
        self.length -= 1


class LinkedListNode:
    def __init__(self, value, next):
        self.value = value
        self.next = next
