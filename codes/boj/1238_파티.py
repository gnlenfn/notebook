from collections import defaultdict, Counter
import heapq
import sys
"""
학생들이 왔다갔다는 거리는
왕복 거리를 말하는 것이었다!
"""
def dijkstra(graph, start):
    distance = {node: float("inf") for node in range(1, n+1)}
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

n, m, start = map(int, sys.stdin.readline().split())
graph = defaultdict(list)
graph_back = defaultdict(list)
for _ in range(m):
    depart, goal, cost = map(int, sys.stdin.readline().split())
    graph[depart].append((goal, cost))
    graph_back[goal].append((depart, cost))

to_party = dijkstra(graph, start)
to_home  = dijkstra(graph_back, start)
result = Counter(to_party) + Counter(to_home)
print(max(result.values()))
