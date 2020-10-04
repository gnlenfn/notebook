import heapq
from sys import stdin

n = int(stdin.readline())
heap = []
for _ in range(n):
    k = int(stdin.readline())
    if k == 0 and heap:
        o = heapq.heappop(heap)
        print(-o)        
    elif k == 0 and not heap:
        print(0)        
    else:
        heapq.heappush(heap, -k)
