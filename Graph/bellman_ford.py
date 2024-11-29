def bellman_ford_optimized(graph, src):
    # Step 1: Initialize distances and previous nodes in a single dictionary
    table = {vertex: {'distance': float('inf'), 'previous': None} for vertex in graph}
    table[src]['distance'] = 0

    relaxation = False  # Flag to track if any updates occur in this iteration

    # Step 2: Relax edges |V| - 1 times, with early stopping using relaxation flag
    for i in range(len(graph) - 1):
        for u in graph:
            for v, weight in graph[u]:
                if table[u]['distance'] != float('inf') and table[u]['distance'] + weight < table[v]['distance']:
                    table[v]['distance'] = table[u]['distance'] + weight
                    table[v]['previous'] = u
                    relaxation = True
        # If no updates were made, we can break early
        if not relaxation:
            break

    # Step 3: Check for negative-weight cycles only if updates occurred
    if relaxation:  # Only check for negative cycles if relaxation occurred
        for u in graph:
            for v, weight in graph[u]:
                if table[u]['distance'] != float('inf') and table[u]['distance'] + weight < table[v]['distance']:
                    print("Graph contains a negative weight cycle")
                    return None

    return table


def print_table(table):
    print("Table of distances and previous nodes:")
    for vertex, data in table.items():
        print(f"{vertex}: Distance = {data['distance']}, Previous = {data['previous']}")


def print_path(table, src, dest):
    path = []
    current = dest
    while current != src:
        path.append(current)
        current = table[current]['previous']
    path.append(src)
    path.reverse()
    print(f"Shortest path from {src} to {dest}: {' -> '.join(path)}")


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
table = bellman_ford_optimized(graph, source)

if table:
    print_table(table)
    # Example: Print the shortest path from A to G
    print_path(table, source, 'G')
