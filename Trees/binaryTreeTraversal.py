import QueueLinkedList as queue


class TreeNode:
    def __init__(self, data):
        self.data = data
        self.rightChild = None
        self.leftChild = None


root = TreeNode("Drinks")
leftChild = TreeNode("Hot")
rightChild = TreeNode("Cold")

root.leftChild = leftChild
root.rightChild = rightChild


def preOrderTraversal(rootNode):
    if not rootNode:
        return

    # preorder traversal pattern (root -> left -> right)
    print(rootNode.data)
    preOrderTraversal(rootNode.leftChild)
    preOrderTraversal(rootNode.rightChild)


def inOrderTraversal(rootNode):
    if not rootNode:
        return

    # inorder traversal pattern (left -> root -> right)
    inOrderTraversal(rootNode.leftChild)
    print(rootNode.data)
    inOrderTraversal(rootNode.rightChild)


def postOrderTraversal(rootNode):
    if not rootNode:
        return

    # post-order traversal pattern (left -> right -> root)
    postOrderTraversal(rootNode.leftChild)
    postOrderTraversal(rootNode.rightChild)
    print(rootNode.data)


def levelOrderTraversal(rootNode):
    if not rootNode:
        return

    # Queue is queue using Linked List.
    customQueue = queue.Queue()
    # Insert "Drinks" TreeNode in the Queue.
    customQueue.enqueue(rootNode)

    while not (customQueue.isEmpty()):
        # pop the left-most node [FIFO, since its a queue]
        root = customQueue.dequeue()
        treeNode = root.value  # root.value is the TreeNode object
        print(treeNode.data)

        if treeNode.leftChild is not None:
            customQueue.enqueue(treeNode.leftChild)

        if treeNode.rightChild is not None:
            customQueue.enqueue(treeNode.rightChild)


# preOrderTraversal(root)
# inOrderTraversal(root)
# postOrderTraversal(root)
levelOrderTraversal(root)
