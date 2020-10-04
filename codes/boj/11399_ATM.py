from collections import deque
n = int(input())

line = deque(sorted(list(map(int, input().split()))))
time = 0
answer = []
while line:
    current = line.popleft()
    time += current
    answer.append(time)
print(sum(answer))


import heapq
n = int(input())
line = list(map(int, input().split()))
heapq.heapify(line)

time = 0
answer = []
while line:
    current = heapq.heappop(line)
    time += current
    answer.append(time)
print(sum(answer))