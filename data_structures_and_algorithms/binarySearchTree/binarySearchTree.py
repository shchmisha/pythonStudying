from queue_for_levelOrder import Queue


class BSTNode:
    def  __init__(self, data):
        self.data = data
        self.leftChild = None
        self.rightChild = None

def insertNode(rootNode, value):
    # insert all greater nodes to the left,lesser to the right
    if rootNode.data == None:
        rootNode.data = value
    elif rootNode.data >= value:
        if rootNode.leftChild is None:
            rootNode.leftChild = BSTNode(value)
        else:
            insertNode(rootNode.leftChild, value)
    else: 
        if rootNode.rightChild is None:
            rootNode.rightChild = BSTNode(value)
        else:
            insertNode(rootNode.rightChild, value)
    return 'successfully inserted'
    
def preOrderTraversal(root):
    if root is None:
        return
    else:
        print(root.data)
        preOrderTraversal(root.leftChild)
        preOrderTraversal(root.rightChild)

def inOrderTraversal(root):
    if root is None:
        return
    else:
        preOrderTraversal(root.leftChild)
        print(root.data)
        preOrderTraversal(root.rightChild)

def postOrderTraversal(root):
    if root is None:
        return
    else:
        preOrderTraversal(root.leftChild)
        print(root.data)
        preOrderTraversal(root.rightChild)
        
def levelOrderTraversal(root):
    if not root:
        return
    else:
        queue = Queue()
        queue.enqueue(root)
        while not(queue.isEmpty()):
            node = queue.dequeue()
            print(node.value.data)
            if node.value.leftChild is not None:
                queue.enqueue(node.value.leftChild)
            if node.value.rightChild is not None:
                queue.enqueue(node.value.rightChild)

def searchTree(root, value):
    if root.data == value:
        print('value found')
    elif value<root.data:
        if root.leftChild.data == value:
            print('value found')
        else:
            searchTree(root.leftChild, value)
    else:
        if root.rightChild.data == value:
            print('value found')
        else:
            searchTree(root.rightChild, value)

def minValue(node):
    current = node
    while current.leftChild is not None:
        current = current.leftChild
    return current

def deleteNode(root, value):
    if root is None:
        return root
    if value < root.data:
        root.leftChild = deleteNode(root.leftChild, value)
    elif value > root.data:
        root.rightChild = deleteNode(root.rightChild, value)
    else:
        if root.leftChild is None:
            temp = root.leftChild
            root = None
            return temp
        if root.rightChild is None:
            temp = root.rightChild
            root = None
            return temp
        temp = minValue(root.rightChild)
        root.data = temp.data
        root.rightChild = deleteNode(root.rightChild, temp.data)
    return root

def deleteBST(root):
    root.data = None
    root.leftChild = None
    root.rightChild = None
    return 'tree deleted'

        

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
deleteNode(newBST, 60)
levelOrderTraversal(newBST)