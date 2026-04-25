# Why Level Order (BFS) for Insertion?
# Level order traversal allows us to find the first available empty slot in the tree
# (from left to right and top to bottom), ensuring the tree remains as compact as possible.

import QueueLinkedList as queue


class TreeNode:
    """Class representation for a node in a Binary Tree."""

    def __init__(self, data):
        self.data = data
        self.leftChild = None
        self.rightChild = None


def insertBinaryTree(root_node, new_data):
    """
    Inserts a new node into the Binary Tree at the first available position using Level Order Traversal.

    Time Complexity: O(n) - where n is the number of nodes in the tree.
    Space Complexity: O(n) - queue can hold up to n/2 nodes in a full tree.

    Args:
        root_node (TreeNode): The starting node of the tree.
        new_data: The value to be stored in the new node.

    Returns:
        str: Success message once the node is inserted.
    """
    if not root_node:
        return "The tree is empty. Please initialize root manually."

    new_node = TreeNode(new_data)
    custom_queue = queue.Queue()
    custom_queue.enqueue(root_node)

    while not custom_queue.isEmpty():
        current_node = custom_queue.dequeue()
        tree_node = current_node.value

        # Check left child first
        if tree_node.leftChild:
            custom_queue.enqueue(tree_node.leftChild)
        else:
            tree_node.leftChild = new_node
            return f"Successfully inserted '{new_data}' as a left child!"

        # Check right child next
        if tree_node.rightChild:
            custom_queue.enqueue(tree_node.rightChild)
        else:
            tree_node.rightChild = new_node
            return f"Successfully inserted '{new_data}' as a right child!"


def levelOrderTraversal(root_node):
    """Utility function to verify the insertion by printing all nodes."""
    if not root_node:
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

    print("Current Level Order Traversal:", " -> ".join(results))


if __name__ == "__main__":
    # 1. Setup Initial Binary Tree
    root = TreeNode("drinks")
    root.leftChild = TreeNode("hot")
    root.rightChild = TreeNode("cold")

    print("--- Initial State ---")
    levelOrderTraversal(root)

    # 2. Perform Insertions
    print("\nAttempting to insert 'coffee'...")
    print(insertBinaryTree(root, "coffee"))

    print("\nAttempting to insert 'tea'...")
    print(insertBinaryTree(root, "tea"))

    print("\n--- Final State ---")
    levelOrderTraversal(root)
