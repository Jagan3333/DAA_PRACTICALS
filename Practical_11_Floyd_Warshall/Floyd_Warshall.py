
# Floyd-Warshall Algorithm

INF = float('inf')

graph = [
    [0,   5,   INF, 10],
    [INF, 0,   3,   INF],
    [INF, INF, 0,   1],
    [INF, INF, INF, 0]
]

n = len(graph)
dist = [row[:] for row in graph]

for k in range(n):
    for i in range(n):
        for j in range(n):
            dist[i][j] = min(
                dist[i][j],
                dist[i][k] + dist[k][j]
            )

print("Shortest Distance Matrix:")

for row in dist:
    for value in row:
        if value == INF:
            print("INF", end="\t")
        else:
            print(int(value), end="\t")
    print()
