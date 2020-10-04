from collections import defaultdict
import heapq
import sys

def dijkstra(graph, start):
    distance = {node: float("inf") for node in range(1, nodes+1)}
    distance[start] = 0
    queue = []
    heapq.heappush(queue, [distance[start], start])
    while queue:
        current_distance, current_node = heapq.heappop(queue)
        if distance[current_node] < current_distance:
            continue
        for adjacent, weight in graph[current_node]:
            d = current_distance + weight
            if d < distance[adjacent]:
                distance[adjacent] = d
                heapq.heappush(queue, [d, adjacent])
    return distance

nodes, lines = map(int, sys.stdin.readline().split())
start = int(sys.stdin.readline())

graph = defaultdict(list)
for _ in range(lines):
    depart, goal, weight = map(int, sys.stdin.readline().split())
    graph[depart].append((goal, weight))


result = dijkstra(graph, start)

for n in range(1, nodes+1):
    print(result[n] if result[n] != float("inf") else "INF")