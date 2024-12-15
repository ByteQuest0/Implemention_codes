import heapq

def prims_algorithm(graph, start):
    """
    Function to implement Prim's Algorithm to find the Minimum Spanning Tree (MST).

    :param graph: A dictionary where keys are nodes, and values are lists of tuples (neighbor, weight).
    :param start: The starting node for the algorithm.
    :return: The MST as a list of edges and the total cost of the MST.
    """
    # Priority queue to store edges with weights
    priority_queue = []
    # To keep track of visited nodes
    visited = set()
    # Resulting MST edges and total weight
    mst_edges = []
    total_cost = 0

    # Start with the initial node
    visited.add(start)
    for neighbor, weight in graph[start]:
        heapq.heappush(priority_queue, (weight, start, neighbor))

    while priority_queue:
        weight, u, v = heapq.heappop(priority_queue)
        if v not in visited:
            # Add edge to MST
            visited.add(v)
            mst_edges.append((u, v))
            total_cost += weight

            # Add edges of the newly visited node
            for neighbor, weight in graph[v]:
                if neighbor not in visited:
                    heapq.heappush(priority_queue, (weight, v, neighbor))

    return mst_edges, total_cost


# Example usage
graph = {
    'A': [('B', 2), ('D', 5), ('F', 3)],
    'B': [('A', 2), ('C', 7), ('D', 2), ('F', 4)],
    'C': [('B', 7), ('D', 1)],
    'D': [('B', 2), ('C', 1), ('A', 5)],
    'F': [("A", 3), ("B", 4)]
}

start_node = 'A'
mst, cost = prims_algorithm(graph, start_node)
print("Minimum Spanning Tree:", mst)
print("Total Cost:", cost)
