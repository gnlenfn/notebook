from collections import defaultdict
import heapq, sys

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

departure, arrive = map(int, sys.stdin.readline().split())
nodes, lines = map(int, sys.stdin.readline().split())

graph = defaultdict(list)
for _ in range(lines):
    depart, goal = map(int, sys.stdin.readline().split())
    graph[depart].append((goal, 1))
    graph[goal].append((depart, 1))
result = dijkstra(graph, departure)
print(result, arrive)
print(result[arrive] if result[arrive] != float("inf") else -1)