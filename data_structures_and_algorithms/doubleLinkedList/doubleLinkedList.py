class Node:
    def __init__(self, value=None):
        self.value = value
        self.next = None
        self.prev = None

class DoubleLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def __iter__(self):
        temp = self.head
        while temp is not None:
            yield temp
            temp = temp.next

    def createDLL(self, value):
        node = Node(value)
        node.prev = None
        node.head = None
        self.head = node
        self.tail = node
        return 'created successfully'

    def insertNode(self, value, location):
        if self.head is None:
            print('node cannot be inserted')
        else:
            node = Node(value)
            if location == 0:
                node.prev = None
                node.next = self.head
                self.head.prev = node
                self.head = node
            elif location == -1:
                node.next = None
                self.tail.next = node
                node.prev = self.tail
                self.tail = node
            else:
                temp = self.head
                index = 0
                while index < location-1:
                    temp = temp.next
                    index+=1
                node.next = temp.next
                node.prev = temp
                temp.next.prev = node
                temp.next = node

    def traverseDLL(self):
        if self.head is None:
            print('the lsit is empty')
        else:
            temp = self.head
            while temp is not None:
                print(temp.value)
                temp = temp.next

    def reverseTraversalDLL(self):
        if self.tail is None:
            print('list is empty')
        else:
            temp = self.tail
            while temp is not None:
                print(temp.value)
                temp = temp.prev

    def searchDLL(self, value):
        if self.tail is None:
            print('list is empty')
        else:
            node = self.head
            while node is not None:
                if self.head == value:
                    return 'found'
                node = node.next
            return 'not found'

    def deleteNode(self, location):
        if self.tail is None:
            print('list is empty')
        else:
            if location == 0:
                if self.head == self.tail:
                    self.head = None
                    self.tail = None
                else:
                    self.head = self.head.next
                    self.head.prev = None
            elif location == -1:
                if self.head == self.tail:
                    self.head = None
                    self.tail = None
                else:
                    self.tail = self.tail.prev
                    self.tail.next = None
            else:
                temp = self.head
                index = 0
                while index < location - 1:
                    temp = temp.next
                    index+=1
                temp.next = temp.next.next
                temp.next.prev = temp
            return 'deleted'
            

                
                    

dll = DoubleLinkedList()
dll.createDLL(5)

print([x.value for x in dll])
