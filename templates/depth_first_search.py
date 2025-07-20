# depth first search
# used to solve a wide range of problems
# from tree to graph to combinatorial problems and is
# very useful in tech interviews
def dfs(graph, start, visited=None):
    if visited is None:
        visited = set()
    visited.add(start)
    for next in graph[start] - visited:
        dfs(graph, next, visited)
    return visited