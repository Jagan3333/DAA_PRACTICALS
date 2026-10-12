
# Practical 9: Prim's Algorithm

graph = [
    [0, 2, 0, 6, 0],
    [2, 0, 3, 8, 5],
    [0, 3, 0, 0, 7],
    [6, 8, 0, 0, 9],
    [0, 5, 7, 9, 0]
]

V = len(graph)
selected = [False] * V
selected[0] = True

total_cost = 0
print("Edge \tWeight")

for _ in range(V - 1):
    minimum = float('inf')
    x = 0
    y = 0

    for i in range(V):
        if selected[i]:
            for j in range(V):
                if not selected[j] and graph[i][j] != 0:
                    if graph[i][j] < minimum:
                        minimum = graph[i][j]
                        x = i
                        y = j

    print(f"{x} - {y}\t{minimum}")
    total_cost += minimum
    selected[y] = True

print("Total Minimum Cost:", total_cost)
