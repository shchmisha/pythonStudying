from queue_for_levelOrder import Queue

class TreeNode:
    def __init__(self, data):
        self.data = data
        self.leftChild = None
        self.rightChild = None

newBT = TreeNode('Drinks')
leftChild = TreeNode("Hot")
rightChild = TreeNode("Cold")
tea = TreeNode('Teas')
coffee = TreeNode('Coffee')

fanta = TreeNode('Fanta')

leftChild.leftChild = tea
leftChild.rightChild = coffee


rightChild.rightChild = fanta

newBT.leftChild = leftChild
newBT.rightChild = rightChild

def preOrderTraversal(root):
    if not root:
        return
    print(root.data)
    preOrderTraversal(root.leftChild)
    preOrderTraversal(root.rightChild)

def inOrderTraversal(root):
    if not root:
        return
    inOrderTraversal(root.leftChild)
    print(root.data)
    inOrderTraversal(root.rightChild)

def postOrderTraversal(root):
    if not root:
        return
    postOrderTraversal(root.leftChild)
    postOrderTraversal(root.rightChild)
    print(root.data)

def levelOrderTraversal(root):
    if not root:
        return
    else:
        queue = Queue()
        queue.enqueue(root)
        while not(queue.isEmpty()):
            node = queue.dequeue()
            print(node.value.data)
            if (node.value.leftChild is not None):
                queue.enqueue(node.value.leftChild)
            if (node.value.rightChild is not None):
                queue.enqueue(node.value.rightChild)



def searchBT(root, value):
    if not root:
        return 'root does not exist'
    else:
        queue = Queue()
        queue.enqueue(root)
        while not(queue.isEmpty()):
            node = queue.dequeue()
            if node.value.data == value:
                return 'success'
            if (node.value.leftChild is not None):
                queue.enqueue(node.value.leftChild)
            if (node.value.rightChild is not None):
                queue.enqueue(node.value.rightChild)
        return 'value not found'

def insertNode(rootNode, newNode):
    if not rootNode:
        rootNode = newNode
    else:
        queue = Queue()
        queue.enqueue(rootNode)
        while not(queue.isEmpty()):
            root = queue.dequeue()
            if (root.value.leftChild is not None):
                queue.enqueue(root.value.leftChild)
            else:
                root.value.leftChild = newNode
                return "successfully inserted"
            if (root.value.rightChild is not None):
                queue.enqueue(root.value.rightChild)
            else:
                root.value.rightChild = newNode
                return "successfully inserted"





def getDeepestNode(root):
    if not root:
        return 'root does not exist'
    else:
        queue = Queue()
        queue.enqueue(root)
        while not(queue.isEmpty()):
            node = queue.dequeue()
            if (node.value.leftChild is not None):
                queue.enqueue(node.value.leftChild)
            if (node.value.rightChild is not None):
                queue.enqueue(node.value.rightChild)
        deepestNode = node.value
        return deepestNode

def deleteDeepestNode(root, dNode):
    if not root:
        return 'root does not exist'
    else:
        queue = Queue()
        queue.enqueue(root)
        while not(queue.isEmpty()):
            node = queue.dequeue()
            if node.value is dNode:
                node.value = None
                return
            if node.value.rightChild:
                if node.value.rightChild is dNode:
                    node.value.rightChild = None
                    return
                else:
                    queue.enqueue(node.value.rightChild)
            if node.value.leftChild:
                if node.value.leftChild is dNode:
                    node.value.leftChild = None
                    return
                else:
                    queue.enqueue(node.value.leftChild)

def deleteNode(rootNode, node):
    if not rootNode:
        return 'binary tree empty'
    else:
        queue = Queue()
        queue.enqueue(rootNode)
        while not queue.isEmpty():
            root = queue.dequeue()
            if root.value.data == node:
                dNode = getDeepestNode(rootNode)
                root.value.data = dNode.data
                deleteDeepestNode(rootNode, dNode)
                return "successfully deleted"
            if (root.value.leftChild is not None):
                queue.enqueue(root.value.leftChild)
            if (root.value.rightChild is not None):
                queue.enqueue(root.value.rightChild)
        return  "failed to delete"

def deleteBinaryTree(root):
    root.value = None
    root.leftChild = None
    root.rigthChild = None
    return "successfully deleted"

# cola = TreeNode('Cola')
# print(insertNode(newBT, cola))

print(deleteNode(newBT, 'Teas'))