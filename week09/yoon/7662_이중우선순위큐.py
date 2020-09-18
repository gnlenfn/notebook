import heapq, sys

input = sys.stdin.readline

for _ in range(int(input())):
    max_heap, min_heap = [], []
    del_max_heap, del_min_heap = [], []

    for _ in range(int(input())):
        command, num = input().split()
        num = int(num)
        if command == "I":
            heapq.heappush(min_heap, num)
            heapq.heappush(max_heap, -num)
        else: # command == "D"
            if num == 1 and max_heap:
                heapq.heappush(del_max_heap, -heapq.heappop(max_heap))
            elif num == -1 and min_heap:
                heapq.heappush(del_min_heap, -heapq.heappop(min_heap))
        
        while max_heap and del_max_heap and max_heap[0] == del_max_heap[0]:
            heapq.heappop(max_heap)
            heapq.heappop(del_max_heap)
        
        while min_heap and del_min_heap and min_heap[0] == del_min_heap[0]:
            heapq.heappop(min_heap)
            heapq.heappop(del_min_heap)

    if not max_heap:
        print("EMPTY")
    else:
        print(-max_heap[0], min_heap[0])
