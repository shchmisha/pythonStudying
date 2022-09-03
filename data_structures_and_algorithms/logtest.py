import math

class TreeNode:
    def __init__(self, data=None):
        self.data = data
        self.leftChild = None
        self.rightChild = None

def insertNode(rootNode, newNode):
    if not rootNode:
        rootNode = newNode
    else:
        queue = [rootNode]
        while queue:
            root = queue.pop(0)
            if (root.leftChild is not None):
                queue.append(root.leftChild)
            else:
                root.leftChild = newNode
                return "successfully inserted"
            if (root.rightChild is not None):
                queue.append(root.rightChild)
            else:
                root.rightChild = newNode
                return "successfully inserted"

def levelOrderTraversal(root):
    if not root:
        return
    else:
        queue = [root]
        while queue:
            node = queue.pop(0)
            print(node.data)
            if (node.leftChild is not None):
                queue.append(node.leftChild)
            if (node.rightChild is not None):
                queue.append(node.rightChild)

# n=amnt of docs
n=5

# calculate the amount of levels needed to fit all hashes
lvl = math.floor(math.log(n)/math.log(2))
print(lvl)

# calculate amount of nodes needed to fill out these levels
# we need to fill the last level
root = TreeNode(1)
while lvl>0:
    numOfNodes = 2**lvl
# find recursivee function to find the sum of all the nodes in each level
# print(numOfNodes)
    for i in range(numOfNodes):
        node=TreeNode(0)
        insertNode(root, node)
    lvl-=1

levelOrderTraversal(root)
