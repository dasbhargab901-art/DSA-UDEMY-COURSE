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


def searchNode(node, target):
    if not node:
        return "NOT AVAILABLE!"

    if node.data == target:
        return "Target found!"

    if target < node.data:
        return searchNode(node.leftChild, target)
    else:
        return searchNode(node.rightChild, target)


print(searchNode(rootNode, 21))
