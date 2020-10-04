n, m = map(int, input().split())
matrix = [[] for _ in range(n+1)]
visited = [0] * (n+1)

for _ in range(m):
    x, y = map(int, input().split())
    matrix[x].append(y)

    