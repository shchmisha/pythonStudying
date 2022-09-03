# if x is the position of a node in the list
# left child of the node is placed at 2x
# right child of the node is placed at 2x+1

class BinaryTree:
    def __init__(self,size):
        self.list = size * [None]
        self.lastUsedIndex = 0
        self.size = size
    
    def insertNode(self,value):
        # in here, insteead of just inserting at the end, start from the start and compare the values
        # temp = 1
        # e.i. if value > self.list[temp-1], check if list.len > (temp-1)*2, check if self.list[(temp-1)*2] is taken
        # if self.list[(temp-1)*2] is taken, then recursively call the insert function again
        # s
        if self.lastUsedIndex + 1 == self.size:
            return "Binary tree is full"
        self.list[self.lastUsedIndex+1] = value
        self.lastUsedIndex+=1
        return 'value inserted'

    def searchNode(self, value):
        for i in range(len(self.list)):
            if self.list[i] == value:
                return 'node found'
        return 'not found'

    def preOrderTraversal(self, index):
        if index > self.lastUsedIndex:
            return 
        print(self.list[index])
        self.preOrderTraversal(index*2)
        self.preOrderTraversal(index*2+1)
    
    def inOrderTraversal(self, index):
        if index > self.lastUsedIndex:
            return 
        self.preOrderTraversal(index*2)
        print(self.list[index])
        self.preOrderTraversal(index*2+1)

    def postOrderTraversal(self, index):
        if index > self.lastUsedIndex:
            return 
        self.preOrderTraversal(index*2)
        self.preOrderTraversal(index*2+1)
        print(self.list[index])

    def levelOrderTraversal(self,index):
        for i in range(index,self.lastUsedIndex+1):
            print(self.list[i])
    
    def deleteNode(self, value):
        if self.lastUsedIndex == 0:
            return 'tree empty'
        for i in range(1, self.lastUsedIndex+1):
            if self.list[i] == value:
                self.list[i] = self.list[self.lastUsedIndex]
                self.list[self.lastUsedIndex] = None
                self.lastUsedIndex-=1
                return 'successfully deleted'
        return 'no node found'

    def deleteTree(self):
        self.list = None
        return 'successfully deleted'


# newBT = BinaryTree(8)
# newBT.insertNode('a')
# newBT.insertNode('b')
# newBT.insertNode('c')
# newBT.insertNode('d')
# newBT.insertNode('e')
# newBT.insertNode('f')
# newBT.preOrderTraversal(1)
# newBT.inOrderTraversal(1)
# print(newBT.deleteNode('e'))


