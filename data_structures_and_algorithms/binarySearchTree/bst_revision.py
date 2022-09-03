from queue_for_levelOrder import Queue


class BSTNode:
    def  __init__(self, data):
        self.data = data
        self.leftChild = None
        self.rightChild = None


def insertNode(rootNode, value):
    if rootNode.data == None:
        rootNode.data = value
    elif rootNode.data >= value:
        if rootNode.leftChild == None:
            rootNode.leftChild = BSTNode(value)
        else:
            insertNode(rootNode.leftChild, value)
    else:
        if rootNode.rightChild == None:
            rootNode.rightChild = BSTNode(value)
        else:
            insertNode(rootNode.rightChild, value)

def leverOrder(rootNode):
    if not rootNode:
        return
    else:
        queue = Queue()
        queue.enqueue(rootNode)
        while not(queue.isEmpty()):
            node = queue.dequeue()
            print(node.data.value)
            if node.leftChild is not None:
                queue.enqueue(node.data.leftChild)
            if node.rightChild is not None:
                queue.enqueue(node.data.rightChild)

def searchBST(rootNode, value):
    if rootNode.data == value:
        print("found")
    elif value > rootNode.data:
        if rootNode.rightChild == value:
            print("found")
        else:
            searchBST(rootNode.rightChild, value)
    else:
        if rootNode.leftChild == value:
            print("found")
        else:
            searchBST(rootNode.leftChild, value)

newBST =  BSTNode(None)
insertNode(newBST, 70)
insertNode(newBST, 50)
insertNode(newBST, 90)
insertNode(newBST, 30)
insertNode(newBST, 60)
insertNode(newBST, 80)
insertNode(newBST, 100)
insertNode(newBST, 20)
insertNode(newBST,40)
searchBST(newBST, 40)