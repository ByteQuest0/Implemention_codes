from collections import deque

# Define the graph
graph = {
    'A': ['B', 'C'],
    'B': ['G', 'A'],
    'C': ['A', "G", 'F'],
    'D': ['E'],
    'E': ['D', 'F'],
    'F': ['C', "G", 'E'],
    "G": ["B", "F", "C"]
}

from collections import deque

def bfs(graph, start_node):
    visited = set()  # Set to keep track of visited nodes
    queue = deque([start_node])  # Queue for BFS traversal
    traversal = []  # List to store traversal order

    while queue:
        node = queue.popleft()  # Remove the first node in the queue
        if node not in visited:
            visited.add(node)  # Mark the node as visited
            traversal.append(node)  # Add the node to traversal order

            # Add neighbors to the queue if they haven't been visited
            for neighbor in graph[node]:
                if neighbor not in visited:
                    queue.append(neighbor)

    return traversal


# Perform BFS starting from node 'A'
start_node = 'A'
bfs_traversal = bfs(graph, start_node)
print("BFS Traversal:", bfs_traversal)
