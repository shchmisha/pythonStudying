class Node():
    def  __init__(self, value=None):
        self.value = value
        self.next = None

class LinkedList():
    def __init__(self):
        self.head = None
        self.tail = None
        self.length = 0

    def __iter__(self):
        node = self.head
        while node:
            yield node.value
            node = node.next


    def insertSLL(self, value, location=-1):
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
        self.length+=1

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

    # def deleteNode(self, location):
    #     if self.head is None:
    #         print('list is empty')
    #     else:
    #         if location == 0:
    #             if self.head == self.tail:
    #                 self.head = None
    #                 self.tail = None
    #             else:
    #                 self.head = self.head.next
    #         elif location == -1:
    #             if self.head == self.tail:
    #                 self.head = None
    #                 self.tail = None
    #             else:
    #                 node = self.head
    #                 while node is not None:
    #                     if node.next == self.tail:
    #                         break
    #                     node = node.next
    #                 node.next = None
    #                 self.tail = node
    #         else:
    #             tempNode = self.head
    #             index = 0
    #             while index<location-1:
    #                 tempNode = tempNode.next
    #                 index+=1
    #             nextNode = tempNode.next
    #             tempNode.next = nextNode.next

if __name__ == '__main__':
    linkedList = LinkedList()
    linkedList.insertSLL(1)
    linkedList.insertSLL(2)
    linkedList.insertSLL(3)
    linkedList.insertSLL(4)

    print([node for node in linkedList])
    # linkedList.traverseSLL()

    print(linkedList.searchSLL(3))