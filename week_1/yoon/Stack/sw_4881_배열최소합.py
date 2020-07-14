def adjacent(x):
    global tmp, result

    if result < tmp:
        return

    if x == n:
        if tmp < result:
            result = tmp
        return

    for i in range(n):
        if not visited[i]:
            visited[i] = True
            tmp += matrix[x][i]
            adjacent(x + 1)
            visited[i] = False
            tmp -= matrix[x][i]

T = int(input())
for test_case in range(1, T + 1):
    n = int(input())
    matrix = [list(map(int, input().split())) for _ in range(n)]
    visited = [False] * n
    tmp, result = 0, 100
    adjacent(0)

    print(f'#{test_case} {result}') 

