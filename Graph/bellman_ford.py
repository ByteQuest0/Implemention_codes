def bellman_ford(graph, src):
    # Step 1: Initialize distances from src to all vertices as infinity and previous as None
    table = {vertex: {'distance': float('inf'), 'previous': None} for vertex in graph}
    table[src]['distance'] = 0  # Set the distance of the source vertex to 0

    # Step 2: Relax edges |V| - 1 times
    for _ in range(len(graph) - 1):
        for u in graph:
            for v, weight in graph[u]:
                if table[u]['distance'] != float('inf') and table[u]['distance'] + weight < table[v]['distance']:
                    table[v]['distance'] = table[u]['distance'] + weight
                    table[v]['previous'] = u  # Update the previous node for path reconstruction

    # Step 3: Check for negative-weight cycles
    for u in graph:
        for v, weight in graph[u]:
            if table[u]['distance'] != float('inf') and table[u]['distance'] + weight < table[v]['distance']:
                print("Graph contains a negative weight cycle")
                return None

    return table

def print_path(result, target):
    path = []
    while target is not None:
        path.append(target)
        target = result[target]['previous']
    return path[::-1]  # Return the reversed path

# Example graph
graph = {
    'A': [('F', 3), ('B', 2), ('D', 5)],
    'B': [('E', 1)],
    'D': [('E', 1)],
    'E': [('C', -3), ('G', 3)],
    'C': [('B', 7), ('G', 4)],
    'G': [('D', -1)],
    'F': [('B', -4)],
}

# Compute shortest paths from source vertex 'A'
source = 'A'
result = bellman_ford(graph, source)

if result:
    print(f"Shortest distances from source vertex {source}:")
    for vertex, data in result.items():
        print(f"{vertex}: Distance = {data['distance']}, Previous = {data['previous']}")

    print("\nPaths from source to each vertex:")
    for vertex in result:
        path = print_path(result, vertex)
        print(f"Path to {vertex}: {' -> '.join(path)}")
