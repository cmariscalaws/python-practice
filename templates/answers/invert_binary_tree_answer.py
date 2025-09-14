from typing import Optional

from templates.utils import TreeNode, BinaryTree

def invert(node: TreeNode) -> Optional[TreeNode]:
    # Depth-first traversal; time complexity is O(n) where n is the number of nodes

    if node is None:
        return None  # Base case: if the node is None, return None

    # Recursively invert the left subtree
    left = invert(node.left)
    # Recursively invert the right subtree
    right = invert(node.right)

    # Swap the left and right children
    node.left, node.right = right, left

    return node  # Return the current node after inversion

# Test
if __name__ == "__main__":
    # Build tree:      1
    #                /   \
    #               2     3
    #              / \   / \
    #             4   5 6   7
    tree = BinaryTree.from_list([1, 2, 3, 4, 5, 6, 7])
    expected = [1, 3, 2, 7, 6, 5, 4]
    # Expected tree:   1
    #                /   \
    #               3     2
    #              / \   / \
    #             7   6 5   4
    print("Original:", tree.to_list())  # [1, 2, 3, 4, 5, 6, 7]
    invert(tree.root)
    print("Inverted:", tree.to_list())  # [1, 3, 2, 7, 6, 5, 4]
    print("Expected:", expected)
    assert tree.to_list() == expected, f"Expected {expected}, but got {tree.to_list()}"