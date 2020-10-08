import sys
from collections import deque

def bfs():
    while queue:
        current = queue.popleft()
        if current == RESULT:
            print(distance[current])
            return
        str_current = str(current)
        target = str_current.find('9')
        x, y = target // 3, target % 3
        for dx, dy in zip([-1, 1, 0, 0], [0, 0, -1, 1]):
            nx, ny = x + dx, y + dy
            if nx < 0 or nx >= 3 or ny < 0 or ny >= 3:
                continue
            new_target = nx * 3 + ny
            current_list = list(str_current)
            current_list[target], current_list[new_target] = current_list[new_target], current_list[target]
            nd = int("".join(current_list))
            if not distance.get(nd):
                distance[nd] = distance[current] + 1
                queue.append(nd)
    print(-1)

sys.stdin = open("input.txt", "r")
puzzle = [list(map(int, sys.stdin.readline().split())) for _ in range(3)]

m = 0
for row in range(3):
    for col in range(3):
        if not puzzle[row][col]:
            puzzle[row][col] = 9
            start = (row, col)
        m = m*10 + puzzle[row][col]

RESULT = 123456789
distance = dict()
queue = deque()
queue.append(m)
distance[m] = 0
bfs()
