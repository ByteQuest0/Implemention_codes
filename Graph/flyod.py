import math

# Function for the Floyd-Warshall algorithm returning final matrices
def floyd_warshall_matrices(n, dist):
    INF = math.inf
    # Initialize predecessor (previous_node) matrix
    previous_node = [[None] * n for _ in range(n)]
    nodes = [chr(65 + i) for i in range(n)]  # Map indices to 'A', 'B', 'C', ...

    # Initialize previous_node for direct edges
    for i in range(n):
        for j in range(n):
            if i != j and dist[i][j] != INF:
                previous_node[i][j] = nodes[i]  # Previous node is the source node

    # Main Floyd-Warshall algorithm
    for k in range(n):
        for i in range(n):
            for j in range(n):
                if dist[i][k] + dist[k][j] < dist[i][j]:
                    dist[i][j] = dist[i][k] + dist[k][j]
                    previous_node[i][j] = previous_node[k][j]  # Update to reflect the predecessor

    # Check for negative cycles
    for i in range(n):
        if dist[i][i] < 0:
            print("Negative cycle detected.")
            return None, None

    return dist, previous_node


# Function to reconstruct and print the path
def reconstruct_path(previous_node, start, end):
    nodes = [chr(65 + i) for i in range(len(previous_node))]
    path = []
    current = end
    while current is not None and current != start:
        path.append(current)
        current = previous_node[nodes.index(start)][nodes.index(current)]
    if current is None:
        print(f"No path from {start} to {end}.")
        return
    path.append(start)
    path.reverse()
    print(" -> ".join(path))


# Helper function to print matrices
def print_matrix(matrix):
    for row in matrix:
        print(row)


# Example graph
INF = math.inf
dist_matrix = [
    [0, 2, INF, 3],
    [3, 0, 2, INF],
    [INF, INF, 0, 4],
    [-2, 6, INF, 0]
]

n = 4

# Run the modified Floyd-Warshall algorithm
dist, previous_node = floyd_warshall_matrices(n, dist_matrix)

if dist and previous_node:
    print("Final Distance Matrix:")
    print_matrix(dist)
    print("\nFinal Previous Node Matrix:")
    print_matrix(previous_node)

    # Example of reconstructing a path
    reconstruct_path(previous_node, 'C', 'B')
