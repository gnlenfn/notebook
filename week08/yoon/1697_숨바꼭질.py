from collections import deque

def move_position(next, current):
    if 0 <= next <= MAX and (time[next] == 0 or time[current] + 1 < time[next]):
        time[next] = time[current] + 1
        queue.append(next)

def solution():
    while queue:
        current = queue.popleft()
        if current == end:
            return time[current]
        
        move_position(current + 1, current)
        move_position(current - 1, current)
        move_position(current * 2, current)


MAX = 100000
start, end = map(int, input().split())
queue = deque([start])
time = [0] * (MAX + 1)

print(solution())