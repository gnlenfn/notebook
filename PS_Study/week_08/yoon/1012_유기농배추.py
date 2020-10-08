from collections import deque

def bfs(a, b, field):
    queue = deque()
    queue.append((a, b))
    while queue:
        row, col = queue.popleft()
        for dx, dy in zip([0, 0, 1, -1], [1, -1, 0, 0]):
            new_row, new_col = row + dy, col + dx
            if 0 <= new_row < len(field) and 0 <= new_col < len(field[0]) and field[new_row][new_col]: 
                queue.append((new_row, new_col))
                field[new_row][new_col] = 0

    return 1 # 한 개 그룹 찾음

tc = int(input())
for _ in range(tc):
    colunms, rows, worms = map(int, input().split())
    field = [[0] * colunms for _ in range(rows)]        # 0: visited, 1: not visited
    for _ in range(worms):
        col, row = map(int, input().split())
        field[row][col] = 1
    answer = 0
    for y in range(rows):
        for x in range(colunms):
            if field[y][x] == 1:
                answer += bfs(y, x, field)

    print(answer)

