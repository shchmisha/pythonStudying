

class AVLNode:
    def __init__(self, data=None):
        self.data = data
        self.leftChild = None
        self.rightChild = None
        self.height = 1

def getHeight(rootNode):
    if not rootNode:
        return 0
    return rootNode.height

def rightRotate(disbalancedNode):
    newRoot = disbalancedNode.leftChild
    disbalancedNode.leftChild = disbalancedNode.leftChild.rightChild
    newRoot.rightChild = disbalancedNode
    disbalancedNode.height = 1 + max(getHeight(disbalancedNode.leftChild), getHeight(disbalancedNode.rightChild))
    newRoot.height = 1 + max(getHeight(newRoot.leftChild), getHeight(newRoot.rightChild))
    return newRoot

def leftRotate(disbalancedNode):
    newRoot = disbalancedNode.rightChild
    disbalancedNode.rightChild = disbalancedNode.rightChild.leftChild
    newRoot.leftChild = disbalancedNode
    disbalancedNode.height = 1 + max(getHeight(disbalancedNode.leftChild), getHeight(disbalancedNode.rightChild))
    newRoot.height = 1 + max(getHeight(newRoot.leftChild), getHeight(newRoot.rightChild))
    return newRoot

def getBalance(rootNode):
    if not rootNode:
        return 0
    return getHeight(rootNode.leftChild) - getHeight(rootNode.rightChild)

def insertNode(rootNode, value):
    if not rootNode:
        return AVLNode(value)
    elif value < rootNode.data:
        rootNode.leftChild = insertNode(rootNode.leftChild, value)
    else:
        rootNode.rightChild = insertNode(rootNode.rightChild, value)

    rootNode.height = 1 + max(getHeight(rootNode.leftChild), getHeight(rootNode.rightChild))
    balance = getBalance(rootNode)
    if balance < -1 and rootNode.rightChild.data > value:
        rootNode.rightChild = rightRotate(rootNode.rightChild)
        return leftRotate(rootNode)
    if balance > 1 and rootNode.leftChild.data > value:
        return rightRotate(rootNode)
    if balance < -1 and rootNode.rightChild.data < value:
        return leftRotate(rootNode)
    if balance > 1 and rootNode.leftChild.data < value:
        rootNode.leftChild = leftRotate(rootNode.leftChild)
        return rightRotate(rootNode)
    return rootNode

def traverse(rootNode):
    queue = [rootNode]
    while queue:
        node = queue.pop(0)
        print(node.data)
        if node.leftChild is not None:
            queue.append(node.leftChild)
        if node.rightChild is not None:
            queue.append(node.rightChild)

newAVL = AVLNode(5)
print(newAVL.data)
newAVL = insertNode(newAVL, 10)
newAVL = insertNode(newAVL, 15)
newAVL = insertNode(newAVL, 20)
traverse(newAVL)