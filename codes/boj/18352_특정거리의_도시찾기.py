from collections import defaultdict
import heapq
import sys

def dijkstra(graph, start):
    distance = {node: float("inf") for node in range(1, cities+1)}
    distance[start] = 0
    queue = []
    heapq.heappush(queue, [distance[start], start])
    while queue:
        current_distance, current_city = heapq.heappop(queue)
        if distance[current_city] < current_distance:
            continue
        
        for adjcent, weight in graph[current_city]:
            d = current_distance + weight
            if d < distance[adjcent]:
                distance[adjcent] = d
                heapq.heappush(queue, [d, adjcent])
    return distance

graph = defaultdict(list)
cities, roads, dist, departure = map(int, sys.stdin.readline().split())
for _ in range(roads):
    depart, goal = map(int, sys.stdin.readline().split())
    graph[depart].append((goal, 1))

result = dijkstra(graph, departure)
answer = [city for city in result if result[city] == dist]
if answer:
    for c in answer:
        print(c)
else:
    print(-1)
