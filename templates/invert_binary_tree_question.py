from typing import Optional

from test_fixtures import TreeNode, BinaryTree

def invert(node: TreeNode) -> Optional[TreeNode]:
    # Depth-first traversal; time complexity is O(n) where n is the number of nodes
    pass

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