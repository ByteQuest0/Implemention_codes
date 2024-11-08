graph = {
    'A': ['B', 'C'],
    'B': ['G', 'A'],
    'C': ['A', "G", 'F'],
    'D': ['E'],
    'E': ['D', 'F'],
    'F': ['C', "G", 'E'],
    "G": ["B", "F", "C"]
}


def dfs(graph, vertex, visited):
    visited.add(vertex)
    print(vertex, end=" ")  # Process the vertex
    for neighbor in graph[vertex]:
        if neighbor not in visited:
            dfs(graph, neighbor, visited)


visited = set()
dfs(graph, 'A', visited)

print("\n")


def dfs_iterative(graph, start):
    visited = set()
    stack = [start]

    while stack:
        vertex = stack.pop()
        if vertex not in visited:
            visited.add(vertex)
            print(vertex, end=" ")  # Process the vertex
            # Push all unvisited neighbors to the stack
            for neighbor in reversed(graph[vertex]):
                if neighbor not in visited:
                    stack.append(neighbor)


# Example usage
dfs_iterative(graph, 'A')
