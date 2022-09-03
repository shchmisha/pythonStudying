
class Node():
    def __init__(self, value = None):
        self.value = value
        self.next = None

    def __str__(self):
        return str(self.value)

class LinkedList():
    def __init__(self):
        self.head = None
        self.tail = None

    def __iter__(self):
        node = self.head
        while node is not None:
            yield node
            node = node.next

class Queue():
    def __init__(self):
        self.linkedList = LinkedList()

    def __str__(self):
        values = [str(x) for x in self.linkedList]
        return ' '.join(values)

    def isEmpty(self):
        if self.linkedList.head == None:
            return True
        else:
            return False

    def enqueue(self, value):
        node = Node(value)
        if self.linkedList.head == None:
            self.linkedList.head = node
            self.linkedList.tail = node
        else:
            self.linkedList.tail.next = node
            self.linkedList.tail = node
        
    def dequeue(self):
        if self.isEmpty():
            return "list is empty"
        else:
            node = self.linkedList.head
            if self.linkedList.head == self.linkedList.tail:
                self.linkedList.head = None
                self.linkedList.tail = None
            else:
                self.linkedList.head = self.linkedList.head.next
            return node

    def peek(self):
        if self.isEmpty():
            return "list is empty"
        else:
            return self.linkedList.head

queue = Queue()
queue.enqueue(1)
queue.enqueue(2)
queue.enqueue(3)

