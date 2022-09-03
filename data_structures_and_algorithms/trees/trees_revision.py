from queue_for_levelOrder import Queue

class TreeNode:
    def __init__(self, data):
        self.data = data
        self.leftChild = None
        self.rightChild = None

def insertNode(rootNode, newNode):
    if not rootNode:
        rootNode = newNode
    else:
        queue = Queue()
        queue.enqueue(rootNode)
        while not(queue.isEmpty()):
            node = queue.dequeue
            if node.leftChild is not None:
                queue.enqueue(node.leftChild)
            else:
                node.leftChild = newNode
                return "inserted"
            if node.rightChild is not None:
                queue.enqueue(node.rightChild)
            else:
                node.rightChild = newNode
                return "inserted"

def preOrderTraversal(rootNode):
    if not rootNode:
        return
    else:
        print(rootNode.data)
        preOrderTraversal(rootNode.leftChild)
        preOrderTraversal(rootNode.rightChild)

def inOrderTraversal(rootNode):
    if not rootNode:
        return
    else:
        preOrderTraversal(rootNode.leftChild)
        print(rootNode.data)
        preOrderTraversal(rootNode.rightChild)

def postOrderTraversal(rootNode):
    if not rootNode:
        return
    else:
        preOrderTraversal(rootNode.leftChild)
        preOrderTraversal(rootNode.rightChild)
        print(rootNode.data)