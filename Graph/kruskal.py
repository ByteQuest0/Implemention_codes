class DisjointSet:
    def __init__(self, vertices):
        self.parent = {v: v for v in vertices}
        self.rank = {v: 0 for v in vertices}

    def find(self, vertex):
        if self.parent[vertex] != vertex:
            self.parent[vertex] = self.find(self.parent[vertex])  # Path compression
        return self.parent[vertex]

    def union(self, root1, root2):
        if self.rank[root1] > self.rank[root2]:
            self.parent[root2] = root1
        elif self.rank[root1] < self.rank[root2]:
            self.parent[root1] = root2
        else:
            self.parent[root2] = root1
            self.rank[root1] += 1


def kruskal(graph):
    # Step 1: Extract all edges from the adjacency list and sort them by weight
    edges = []
    for vertex, neighbors in graph.items():
        for neighbor, weight in neighbors:
            if (neighbor, vertex, weight) not in edges:  # Avoid duplicate edges
                edges.append((vertex, neighbor, weight))

    edges.sort(key=lambda edge: (edge[2], edge[0], edge[1]))  # Sort edges by weight, then by vertices for tie-breaking

    # Step 2: Initialize disjoint sets for cycle detection
    vertices = list(graph.keys())
    disjoint_set = DisjointSet(vertices)

    # Step 3: Iterate through edges and construct the MST
    mst = []
    for u, v, weight in edges:
        root_u = disjoint_set.find(u)
        root_v = disjoint_set.find(v)

        # If u and v are not in the same set, include this edge in the MST
        if root_u != root_v:
            mst.append((u, v, weight))
            disjoint_set.union(root_u, root_v)

    return mst


# Input graph
graph = {
    'A': [('F', 3), ('B', 2), ('D', 1)],
    'B': [('A', 2), ('B', 7), ('D', 2), ('F', 4)],
    'D': [('A', 1), ('B', 2), ('C', 5)],
    'C': [('B', 7), ('D', 5)],
    'F': [('B', 4), ('A', 3)],
}

# Run Kruskal's algorithm
mst = kruskal(graph)
print("Minimum Spanning Tree:", mst)
