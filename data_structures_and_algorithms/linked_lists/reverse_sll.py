class Node:
    def __init__(self, value=None):
        self.value = value
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def __iter__(self):
        node = self.head
        while node:
            yield node
            node = node.next

    def insert(self, value, location):
        node = Node(value)
        if self.head is None:
            self.head = node
            self.tail = node
        else:
            if location == 0:
                node.next = self.head
                self.head = node
            if location == -1:
                self.tail.next = node
                node.next = None
                self.tail = node
            else:
                index = 0
                temp = self.head
                while index < location-1:
                    index+=1
                    temp = temp.next
                next = temp.next
                temp.next = node
                node.next = next
                if temp.next == self.tail:
                    self.tail = node


    def reverse(self):
        node = self.head
        prev = None
        while node is not None:
            next = node.next
            node.next = prev
            prev = node
            node = next
        self.head = prev
        node = self.head
        

linkedList = LinkedList()
linkedList.insert(1, -1)
linkedList.insert(2, -1)
linkedList.insert(3, 2)
linkedList.insert(4, 1)
linkedList.insert(4, 1)

linkedList.insert(4, -1)
linkedList.insert(1, -1)
linkedList.insert(5, -1)
linkedList.insert(3, -1)
linkedList.insert(9, -1)

linkedList.insert(8, -1)
linkedList.insert(5, -1)
linkedList.insert(7, -1)

print([node.value for node in linkedList])
linkedList.reverse()
print([node.value for node in linkedList])
