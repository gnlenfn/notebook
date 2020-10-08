from collections import defaultdict
import heapq
def solution(N, road, K):
    answer = 0
    graph = defaultdict(list)
    for depart, goal, cost in road:
        graph[depart].append((goal, cost))
        graph[goal].append((depart, cost))
    cost_map = dijkstra(graph, 1)
    for town in cost_map:
        if cost_map[town] <= K:
            answer += 1
    return answer

def dijkstra(graph, start):
    distances = {node: float("inf") for node in graph}
    distances[start] = 0
    queue = []
    heapq.heappush(queue, [distances[start], start])
    while queue:
        current_distance, current_node = heapq.heappop(queue)
        if distances[current_node] < current_distance:
            continue
        for adjacent, weight in graph[current_node]:
            distance = current_distance + weight
            if distance < distances[adjacent]:
                distances[adjacent] = distance
                heapq.heappush(queue, [distance, adjacent])
    return distances