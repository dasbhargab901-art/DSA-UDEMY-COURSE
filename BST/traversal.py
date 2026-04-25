class BSTNode:
    def __init__(self, data):
        self.data = data
        self.leftChild = None
        self.rightChild = None


rootNode = BSTNode(17)
left1 = BSTNode(10)
right1 = BSTNode(25)
rootNode.leftChild = left1
rootNode.rightChild = right1

# child of left child
left2 = BSTNode(7)
right2 = BSTNode(12)
left1.rightChild = right2
left1.leftChild = left2

# child of right child
left3 = BSTNode(20)
right3 = BSTNode(30)
right1.rightChild = right3
right1.leftChild = left3


def preOrderTraversal(node):
    if not node:
        return

    print(node.data)
    preOrderTraversal(node.leftChild)
    preOrderTraversal(node.rightChild)


def inOrderTraversal(node):
    if not node:
        return

    inOrderTraversal(node.leftChild)
    print(node.data)
    inOrderTraversal(node.rightChild)


def postOrderTraversal(node):
    if not node:
        return

    postOrderTraversal(node.leftChild)
    postOrderTraversal(node.rightChild)
    print(node.data)


# preOrderTraversal(rootNode)
inOrderTraversal(rootNode)
# postOrderTraversal(rootNode)
