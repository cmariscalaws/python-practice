from .tree_node import TreeNode

class BinaryTree:
    def __init__(self, root=None):
        self.root = root

    @staticmethod
    def from_list(values):
        """
        Build a binary tree from a level-order list of values.

        Args:
            values (list): List of values in level-order, where None represents missing nodes.

        Returns:
            BinaryTree: A binary tree constructed from the given list.
        """
        if not values:
            return BinaryTree()  # Return an empty tree if the input list is empty

        # Create TreeNode objects for each value (None for missing nodes)
        nodes = [TreeNode(val) if val is not None else None for val in values]
        kids = nodes[::-1]  # Reverse the list for efficient popping from the end
        root = kids.pop()  # The first node is the root of the tree

        # Assign left and right children for each node in level order
        for node in nodes:
            if node:
                if kids: node.left = kids.pop()  # Assign left child if available
                if kids: node.right = kids.pop()  # Assign right child if available

        return BinaryTree(root)  # Return the constructed binary tree

    def to_list(self):
        """
        Convert the binary tree to a level-order list representation.

        Returns:
            list: Level-order list of node values, with None for missing nodes.
        """
        result = []  # List to store node values
        queue = [self.root]  # Start with the root node in the queue
        while queue:
            node = queue.pop(0)  # Remove the first node from the queue
            if node:
                result.append(node.val)  # Add the node's value to the result
                queue.append(node.left)  # Add left child to the queue
                queue.append(node.right)  # Add right child to the queue
            else:
                result.append(None)  # Add None for missing nodes
        # Remove trailing None values for cleaner output
        while result and result[-1] is None:
            result.pop()
        return result

    def __str__(self):
        return str(self.to_list())