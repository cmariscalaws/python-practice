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

    # Test cases using assertions with print statements for setup, expected, and result
    test_cases = [
        ('A', 'F', ['A', 'C', 'F']),
        ('A', 'E', ['A', 'B', 'E']),
        ('D', 'F', ['D', 'B', 'E', 'F']),
        ('A', 'A', ['A']),
        ('D', 'Z', []),
    ]

    for start, goal, expected in test_cases:
        print("Graph:", graph_example)
        print(f"Start: {start}, Goal: {goal}")
        print("Expected:", expected)
        result = bfs_shortest_path(graph_example, start, goal)
        print("Result:", result)
        assert result == expected, f"Test failed for start={start}, goal={goal}"
        print("Test passed!\n" + "-"*40)

    print("All BFS test cases passed!")
