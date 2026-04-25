# BST is very similar to Binary tree. The only difference is that the leftChild =< node < Right
class BSTNode:
    def __init__(self, data):
        self.data = data
        self.leftChild = None
        self.rightChild = None


newBST = BSTNode(None)
