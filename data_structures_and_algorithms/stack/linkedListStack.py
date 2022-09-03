
class Node():
    def __init__(self, value = None):
        self.value = value
        self.next = next

class LinkedList():
    def __init__(self):
        self.head = None

    def __iter__(self):
        node = self.head
        while node:
            yield node
            node = node.next

class Stack():
    def __init__(self):
        self.linkedList = LinkedList()

    def __str__(self):
        
        values = [str(x.value) for x in self.linkedList]
        return '\n'.join(values)

    def isEmpty(self):
        if self.linkedList.head == None:
            return True
        else:
            return False

    def push(self, value):
        node = Node(value)
        node.next = self.linkedList.head
        self.linkedList.head = node

    def pop(self):
        if self.isEmpty():
            return "list empty"
        else:
            nodeValue = self.linkedList.head.value
            self.linkedList.head = self.linkedList.head.next
            return nodeValue
    
    def peek(self):
        if self.isEmpty():
            return "list empty"
        else:
            return self.linkedList.head.value

    def delete(self):
        self.linkedList.head = None

stack = Stack()
stack.push(1)
stack.push(2)
stack.push(3)
stack.pop()
print(stack)
