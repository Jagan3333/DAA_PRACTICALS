
# Practical 10: Kruskal's Algorithm

vertices = 5

edges = [
    (0, 1, 2),
    (0, 3, 6),
    (1, 2, 3),
    (1, 3, 8),
    (1, 4, 5),
    (2, 4, 7),
    (3, 4, 9)
]

parent = list(range(vertices))


def find(i):
    if parent[i] != i:
        parent[i] = find(parent[i])
    return parent[i]


def union(u, v):
    parent[find(u)] = find(v)


edges.sort(key=lambda edge: edge[2])

total_cost = 0
edge_count = 0

print("Edge\tWeight")
print("Minimum Spanning Tree:")

for u, v, weight in edges:
    if find(u) != find(v):
        union(u, v)
        print(f"{u} - {v}\t{weight}")
        total_cost += weight
        edge_count += 1

    if edge_count == vertices - 1:
        break

print("Total Minimum Cost:", total_cost)
