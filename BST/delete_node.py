from collections import deque


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


def minValueNode(bstNode):
    current = bstNode
    while current.leftChild is not None:
        current = current.leftChild

    return current


def deleteNode(rootNode, target):
    """
    Deletes a node with the given target value from the BST.
    Returns the root of the modified BST.
    """
    if rootNode is None:
        return None

    # Step 1: Navigate to the node to be deleted
    if target < rootNode.data:
        rootNode.leftChild = deleteNode(rootNode.leftChild, target)
    elif target > rootNode.data:
        rootNode.rightChild = deleteNode(rootNode.rightChild, target)
    else:
        # Step 2: Once the node is found, handle the deletion cases

        # Case 1 & 2: Node with only one child or no child
        if rootNode.leftChild is None:
            return rootNode.rightChild
        elif rootNode.rightChild is None:
            return rootNode.leftChild

        # Case 3: Node with two children
        # Get the inorder successor (smallest node in the right subtree)
        temp = minValueNode(rootNode.rightChild)
        
        # Copy the inorder successor's data to this node
        rootNode.data = temp.data
        
        # Delete the inorder successor from the right subtree
        rootNode.rightChild = deleteNode(rootNode.rightChild, temp.data)

    return rootNode


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

    # 4. Delete nodes
    print("\n--- Testing Deletion ---")
    
    print("Deleting 30 (node with two children 20, 40)...")
    rootNode = deleteNode(rootNode, 30)
    levelOrderTraversal(rootNode)

    print("\nDeleting 90 (node with one child 80)...")
    rootNode = deleteNode(rootNode, 90)
    levelOrderTraversal(rootNode)

    print("\nDeleting 70 (root node)...")
    rootNode = deleteNode(rootNode, 70)
    levelOrderTraversal(rootNode)

    print("\nDeleting 10 (leaf node)...")
    rootNode = deleteNode(rootNode, 10)
    levelOrderTraversal(rootNode)
