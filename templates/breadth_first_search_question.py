def bfs_shortest_path(graph, start, goal):
    pass

if __name__ == "__main__":
    # --- Test Cases ---

    # Example graph (undirected)
    graph_example = {
        'A': ['B', 'C'],
        'B': ['A', 'D', 'E'],
        'C': ['A', 'F'],
        'D': ['B'],
        'E': ['B', 'F'],
        'F': ['C', 'E']
    }

    # Test cases using assertions
    # Shortest path from A to F is A -> C -> F
    assert bfs_shortest_path(graph_example, 'A', 'F') == ['A', 'C', 'F']
    # Shortest path from A to E is A -> B -> E
    assert bfs_shortest_path(graph_example, 'A', 'E') == ['A', 'B', 'E']
    # Shortest path from D to F is D -> B -> E -> F
    assert bfs_shortest_path(graph_example, 'D', 'F') == ['D', 'B', 'E', 'F']
    # Path from A to A is just ['A']
    assert bfs_shortest_path(graph_example, 'A', 'A') == ['A']
    # No path from D to a non-existent node
    assert bfs_shortest_path(graph_example, 'D', 'Z') == []

    print("All BFS test cases passed!")

    """
    Algorithm Explanation:
    ---------------------
    - BFS uses a queue to explore nodes in order of their distance from the start node.
    - Each time a node is dequeued, all its unvisited neighbors are enqueued with the path taken so far.
    - The first time the goal node is found, the shortest path is returned (since BFS explores shortest paths first in unweighted graphs).
    - The visited set prevents revisiting nodes and getting stuck in cycles.
    - This implementation returns the actual path, not just the distance.
    
    Time Complexity: O(V + E), where V is the number of vertices and E is the number of edges.
    Space Complexity: O(V), for the queue and visited set.
    """
