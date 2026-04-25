class BSTNode:
    """Class representation for a node in a Binary Search Tree (BST)."""

    def __init__(self, data):
        self.data = data
        self.leftChild = None
        self.rightChild = None

    def __str__(self):
        return str(self.data)


def insertToBST(node, value):
    """
    Inserts a value into the BST.
    Rule: Left Child <= Node < Right Child.
    """
    # this is only executed when root is None
    if node is None:
        BSTNode(value)
    else:
        if value <= node.data:
            if node.leftChild is None:
                node.leftChild = BSTNode(value)
            else:
                insertToBST(node.leftChild, value)
        else:
            if node.rightChild is None:
                node.rightChild = BSTNode(value)
            else:
                insertToBST(node.rightChild, value)

    return "Node created Successfully"


from collections import deque


def levelOrderTraversal(root_node):
    """Utility to verify the BST structure using breadth-first search."""
    if not root_node:
        return

    # We use deque for O(1) popleft() operations
    queue = deque([root_node])

    while queue:
        current = queue.popleft()  # Efficient O(1) removal from the front
        print(current.data, end=" ")

        if current.leftChild:
            queue.append(current.leftChild)
        if current.rightChild:
            queue.append(current.rightChild)
    print()


if __name__ == "__main__":
    # 1. Create the Root
    rootNode = BSTNode(70)

    # 2. Build the initial BST structure
    values_to_insert = [50, 90, 30, 60, 80, 100, 20, 40]
    for val in values_to_insert:
        insertToBST(rootNode, val)

    print("Initial BST Structure (Level Order):")
    levelOrderTraversal(rootNode)

    # 3. Insert new values as requested: 10 and 95
    print("\nInserting 10 and 95...")
    insertToBST(rootNode, 10)
    insertToBST(rootNode, 95)

    print("Final BST Structure after inserts (Level Order):")
    levelOrderTraversal(rootNode)
