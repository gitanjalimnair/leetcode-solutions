
class Node:
    def __init__(self, val=0):
        self.val = val
        self.next = None


class MyLinkedList:

    def __init__(self):
        self.head = Node()  # Dummy head
        self.size = 0

    def get(self, index):
        if index < 0 or index >= self.size:
            return -1

        curr = self.head.next
        for _ in range(index):
            curr = curr.next

        return curr.val

    def addAtHead(self, val):
        self.addAtIndex(0, val)

    def addAtTail(self, val):
        self.addAtIndex(self.size, val)

    def addAtIndex(self, index, val):
        if index < 0:
            index = 0

        if index > self.size:
            return

        curr = self.head
        for _ in range(index):
            curr = curr.next

        node = Node(val)
        node.next = curr.next
        curr.next = node
        self.size += 1

    def deleteAtIndex(self, index):
        if index < 0 or index >= self.size:
            return

        curr = self.head
        for _ in range(index):
            curr = curr.next

        curr.next = curr.next.next
        self.size -= 1
