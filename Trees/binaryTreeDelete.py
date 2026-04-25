# Why Use the Deepest Node for Deletion?
# In a generic Binary Tree (not a BST), we don't have a specific order.
# To keep the tree balanced and compact, we replace the target node's data with
# the data of the deepest/rightmost node and then remove that deepest node.

import QueueLinkedList as queue


class TreeNode:
    """Class representation for a node in a Binary Tree."""

    def __init__(self, data):
        self.data = data
        self.leftChild = None
        self.rightChild = None


def getDeepestNode(root_node):
    """
    Finds and returns the deepest and rightmost node in the Binary Tree.
    Used as the replacement candidate during deletion.
    """
    if not root_node:
        return None

    custom_queue = queue.Queue()
    custom_queue.enqueue(root_node)

    deepest_tree_node = None
    while not custom_queue.isEmpty():
        current_node = custom_queue.dequeue()
        deepest_tree_node = current_node.value

        if deepest_tree_node.leftChild:
            custom_queue.enqueue(deepest_tree_node.leftChild)
        if deepest_tree_node.rightChild:
            custom_queue.enqueue(deepest_tree_node.rightChild)

    return deepest_tree_node


def deleteDeepestNode(root_node, d_node):
    """
    Locates the deepest node and removes its reference from its parent.
    """
    if not root_node:
        return

    custom_queue = queue.Queue()
    custom_queue.enqueue(root_node)

    while not custom_queue.isEmpty():
        current_node = custom_queue.dequeue()
        tree_node = current_node.value

        if tree_node is d_node:
            tree_node = None
            return

        if tree_node.rightChild:
            if tree_node.rightChild is d_node:
                tree_node.rightChild = None
                return
            else:
                custom_queue.enqueue(tree_node.rightChild)

        if tree_node.leftChild:
            if tree_node.leftChild is d_node:
                tree_node.leftChild = None
                return
            else:
                custom_queue.enqueue(tree_node.leftChild)


def deleteNodeBT(root_node, node_val):
    """
    Deletes a node with the specified value from the Binary Tree.

    1. Find the target node.
    2. Find the deepest node.
    3. Swap target node's data with deepest node's data.
    4. Delete the deepest node.
    """
    if not root_node:
        return "The tree is empty!"

    custom_queue = queue.Queue()
    custom_queue.enqueue(root_node)

    target_node = None
    # Level order traversal to find the node to be deleted
    while not custom_queue.isEmpty():
        current_node = custom_queue.dequeue()
        tree_node = current_node.value

        if tree_node.data == node_val:
            target_node = tree_node
            break  # Found the node to delete

        if tree_node.leftChild:
            custom_queue.enqueue(tree_node.leftChild)
        if tree_node.rightChild:
            custom_queue.enqueue(tree_node.rightChild)

    if target_node:
        # Step 2: Get the deepest node
        deepest_node = getDeepestNode(root_node)
        # Step 3: Replace target node's data with deepest node's data
        target_node.data = deepest_node.data
        # Step 4: Delete the deepest node
        deleteDeepestNode(root_node, deepest_node)
        return f"Successfully deleted node with value '{node_val}'"
    else:
        return f"Node with value '{node_val}' not found in the tree."


def levelOrderTraversal(root_node):
    """Utility function to see the current state of the tree."""
    if not root_node:
        print("Empty Tree")
        return

    custom_queue = queue.Queue()
    custom_queue.enqueue(root_node)

    results = []
    while not custom_queue.isEmpty():
        current_node = custom_queue.dequeue()
        tree_node = current_node.value
        results.append(str(tree_node.data))

        if tree_node.leftChild:
            custom_queue.enqueue(tree_node.leftChild)
        if tree_node.rightChild:
            custom_queue.enqueue(tree_node.rightChild)

    print("Level Order:", " -> ".join(results))


if __name__ == "__main__":
    # 1. Setup Binary Tree
    root = TreeNode("drinks")
    l1 = TreeNode("hot")
    r1 = TreeNode("cold")
    l2 = TreeNode("tea")
    r2 = TreeNode("coffee")

    root.leftChild = l1
    root.rightChild = r1
    l1.leftChild = l2
    l1.rightChild = r2

    print("--- Initial Tree ---")
    levelOrderTraversal(root)

    # 2. Delete a node
    delete_target = "hot"
    print(f"\nDeleting '{delete_target}'...")
    print(deleteNodeBT(root, delete_target))

    print("\n--- Final Tree ---")
    levelOrderTraversal(root)
