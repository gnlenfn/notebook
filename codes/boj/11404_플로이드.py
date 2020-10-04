import sys
n = int(sys.stdin.readline())

costs = [[float("inf")] * n for _ in range(n)]
route = int(sys.stdin.readline())
for _ in range(route):
    depart, arrive, cost = map(int, sys.stdin.readline().split())
    costs[depart-1][arrive-1] = min(costs[depart-1][arrive-1], cost)

for cur in range(n):
    costs[cur][cur] = 0
    for row in range(n):
        for col in range(n):
            costs[row][col] = min(costs[row][col], costs[row][cur] + costs[cur][col])
    
for row in costs:
    for col in range(n):
        if row[col] == float("inf"):
            row[col] = 0
        print(row[col], end=" ")
    print()