# Why Level Order (BFS)?
# It uses a Queue to find the target closest to the root first (optimal for searching nearby nodes)
# and avoids the "Recursion Depth" limits of recursive DFS traversals.

import QueueLinkedList as queue


class TreeNode:
    """Class representation for a node in a Binary Tree."""

    def __init__(self, data):
        self.data = data
        self.leftChild = None
        self.rightChild = None


def levelOrderSearch(root_node, target):
    """
    Searches for a target value in the Binary Tree using Level Order Traversal (BFS).

    Time Complexity: O(n) - where n is the number of nodes in the tree.
    Space Complexity: O(n) - in the worst case (full tree), the queue holds n/2 nodes.

    Args:
        root_node (TreeNode): The starting node of the tree.
        target: The data value to search for.

    Returns:
        bool: True if target is found, False otherwise.
    """
    if not root_node:
        return False

    custom_queue = queue.Queue()
    custom_queue.enqueue(root_node)

    while not custom_queue.isEmpty():
        current_node = custom_queue.dequeue()

        # 'current_node' is a Node object from our Queue; its '.value' is the actual TreeNode
        tree_node = current_node.value

        if tree_node.data == target:
            return True

        # Process children [In BFS, we move from left to right]
        if tree_node.leftChild:
            custom_queue.enqueue(tree_node.leftChild)
        if tree_node.rightChild:
            custom_queue.enqueue(tree_node.rightChild)

    return False


if __name__ == "__main__":
    # --- Setup Binary Tree ---
    root = TreeNode("drinks")
    left = TreeNode("hot")
    right = TreeNode("cold")
    root.leftChild = left
    root.rightChild = right

    # --- Search Test ---
    target_value = "hot"
    print(f"Searching for '{target_value}' in Binary Tree...")

    if levelOrderSearch(root, target_value):
        print("Result: Target found!")
    else:
        print("Result: Target NOT found!")
