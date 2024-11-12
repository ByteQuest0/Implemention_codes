import heapq

# Define the graph
graph = {

    'A': [('F', 3), ('B', 2), ('D', 5)],
    'B': [('F', 4), ('A', 2), ('E', 1), ('C', 7)],
    'D': [('A', 5), ('E', 6), ('G', 8)],
    'E': [('B', 1), ('D', 6), ('C', 3), ('G', 2)],
    'C': [('B', 7), ('E', 3), ('G', 4)],
    'G': [('D', 8), ('E', 2), ('C', 4)],
    'F': [('A', 3), ('B', 4)],
}


def dijkstra(graph, start):
    # Initialize distances to infinity and set start node distance to zero
    distances = {node: float('inf') for node in graph}
    distances[start] = 0

    # Priority queue to select the node with the smallest tentative distance
    priority_queue = [(0, start)]

    while priority_queue:
        # Pop the node with the smallest distance
        current_distance, current_node = heapq.heappop(priority_queue)

        # Skip if we have already found a better path
        if current_distance > distances[current_node]:
            continue

        # Evaluate the neighbors
        for neighbor, weight in graph[current_node]:
            distance = current_distance + weight

            # If a shorter path to neighbor is found
            if distance < distances[neighbor]:
                distances[neighbor] = distance
                # Add neighbor to the priority queue
                heapq.heappush(priority_queue, (distance, neighbor))

    return distances

# Example usage:
start_node = 'A'  # You can change this to 'F' or any other node
minimal_distances = dijkstra(graph, start_node)

# Print the minimal distances from the start node to each node
print(f"Minimal distances from node '{start_node}':")
for node, distance in minimal_distances.items():
    print(f"Distance to {node}: {distance}")
