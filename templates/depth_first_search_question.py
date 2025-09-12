"""
Depth First Search (DFS) Template and Example
------------------------------------------------
DFS is a fundamental graph traversal algorithm. It explores as far as possible along each branch before backtracking.

This example demonstrates DFS on an undirected graph represented as an adjacency list.
"""

def dfs(graph, start, visited=None):
    pass

if __name__ == "__main__":
    # --- Test Cases ---

    # Example graph (undirected)
    graph = {
        'A': ['B', 'C'],
        'B': ['A', 'D', 'E'],
        'C': ['A', 'F'],
        'D': ['B'],
        'E': ['B', 'F'],
        'F': ['C', 'E']
    }

    # Documentation: How DFS works on this graph
    """
    Graph structure:
        A
       / \
      B   C
     / \   \
    D   E---F
    
    DFS starting from 'A' will visit nodes in the following order (one possible order):
    A -> B -> D -> E -> F -> C
    
    Note: The exact order may vary depending on the order of neighbors in the adjacency list.
    """

    # Test cases using assertions
    result = dfs(graph, 'A')
    print("DFS traversal from 'A':", result)
    assert result == ['A', 'B', 'D', 'E', 'F', 'C'], "Test case 1 failed!"

    # Test DFS from another node
    result2 = dfs(graph, 'C')
    print("DFS traversal from 'C':", result2)
    assert result2 == ['C', 'A', 'B', 'D', 'E', 'F'] or result2 == ['C', 'F', 'E', 'B', 'A', 'D'], "Test case 2 failed!"

    # Test DFS on a disconnected graph
    disconnected_graph = {
        1: [2],
        2: [1],
        3: [4],
        4: [3]
    }
    result3 = dfs(disconnected_graph, 1)
    print("DFS traversal from 1:", result3)
    assert result3 == [1, 2], "Test case 3 failed!"

    result4 = dfs(disconnected_graph, 3)
    print("DFS traversal from 3:", result4)
    assert result4 == [3, 4], "Test case 4 failed!"

    print("All DFS test cases passed!")

