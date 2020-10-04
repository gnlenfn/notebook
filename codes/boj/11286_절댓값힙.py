import heapq
from sys import stdin

n = int(stdin.readline())
heap = []
for _ in range(n):
    t = int(stdin.readline())
    if heap and t == 0:
        tmp = heapq.heappop(heap)
        print(tmp[1])
    elif not heap and t == 0:
        print(0)
    else:
        heapq.heappush(heap, (abs(t), t))