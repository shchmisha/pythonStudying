
class Node:
    def __init__(self, value=None):
        self.value = value
        self.next = None

class CircularLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def iter(self):
        node = self.head
        while node:
            yield node
            if node.next == self.head:
                break
            node = node.next

    def createSSL(self, value):
        node = Node(value)
        node.next = node
        self.head = node
        self.tail = node
        return "list created"
        

            
    