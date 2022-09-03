

class Node():
    def  __init__(self, value=None):
        self.value = value
        self.next = None

class SingleLinkedList():
    def __init__(self):
        self.head = None
        self.tail = None
        
    def __iter__(self):
        node = self.head
        while node:
            yield node
            node = node.next

    def insertSLL(self, value, location):
        newNode = Node(value)
        if self.head == None:
            self.head = newNode
            self.tail = newNode
        else:
            if location == 0:
                newNode.next = self.head
                self.head = newNode
            if location == -1:
                newNode.next = None
                self.tail.next = newNode
                self.tail = newNode
            else:
                tempNode = self.head
                index = 0
                while index<location-1:
                    tempNode = tempNode.next
                    index+=1
                nextNode = tempNode.next
                tempNode.next = newNode
                newNode.next = nextNode
                if tempNode == self.tail:
                    self.tail = newNode
                    
    def traverseSLL(self):
        if self.head is None:
            print('list is empty')
        else:
            node = self.head
            while node is not None:
                print(node.value)
                node = node.next

    def searchSLL(self, value):
        if self.head == None:
            return "the list is empty"
        else:
            node = self.head
            while node is not None:
                if node.value == value:
                    return node.value
                node = node.next
            return "value not found"

    def deleteNode(self, location):
        if self.head is None:
            print('list is empty')
        else:
            if location == 0:
                if self.head == self.tail:
                    self.head = None
                    self.tail = None
                else:
                    self.head = self.head.next
            elif location == -1:
                if self.head == self.tail:
                    self.head = None
                    self.tail = None
                else:
                    node = self.head
                    while node is not None:
                        if node.next == self.tail:
                            break
                        node = node.next
                    node.next = None
                    self.tail = node
            else:
                tempNode = self.head
                index = 0
                while index<location-1:
                    tempNode = tempNode.next
                    index+=1 
                nextNode = tempNode.next
                tempNode.next = nextNode.next

    def reverseSLL(self):
        if self.head is None:
            print('list is empty')
        else:
            prev=None
            node = self.head
            while node is not None:
                next = node.next
                node.next = prev
                prev = node
                node = next
            self.head = prev


linkedList = SingleLinkedList()
linkedList.insertSLL(1, -1)
linkedList.insertSLL(2, -1)
linkedList.insertSLL(3, -1)
linkedList.insertSLL(4, -1)
linkedList.insertSLL(4, -1)

linkedList.insertSLL(4, -1)
linkedList.insertSLL(1, -1)
linkedList.insertSLL(5, -1)
linkedList.insertSLL(3, -1)
linkedList.insertSLL(9, -1)

linkedList.insertSLL(8, -1)
linkedList.insertSLL(5, -1)
linkedList.insertSLL(7, -1)


print([node.value for node in linkedList])
# linkedList.traverseSLL()
linkedList.reverseSLL()
print([node.value for node in linkedList])

print(linkedList.searchSLL(3))