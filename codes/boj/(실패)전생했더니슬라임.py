import heapq
from sys import stdin

n = int(stdin.readline())
for _ in range(n):
    num_slimes = int(stdin.readline())
    slimes = list(map(int, stdin.readline().split()))
    if len(slimes) == 1:
        print(1)
        break
    heapq.heapify(slimes)
    electric = 1
    while len(slimes) > 1:
        first = heapq.heappop(slimes)
        second = heapq.heappop(slimes)
        heapq.heappush(slimes, first * second)
        electric *= (first * second)
    
    print(electric % 1000000007)

