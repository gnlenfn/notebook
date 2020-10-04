from collections import defaultdict
import heapq
import sys

def dijkstra(graph, start, end):
    distances = {str(node): [float("inf"), start] for node in range(1, n+1)}
    distances[start] = [0, start]
    queue = []
    heapq.heappush(queue, [distances[start][0], start])

    while queue:
        current_distance, current_node = heapq.heappop(queue)
        if distances[current_node][0] < current_distance:
            continue
        for adjacent, weight in graph[current_node].items():
            distance = current_distance + weight
            print(distances)
            if distance < distances[adjacent][0]:
                distances[adjacent] = [distance, current_node]
                heapq.heappush(queue, [distance, adjacent])
    path = end
    path_output = end + '->'
    while distances[path][1] != start:
        path_output += distances[path][1] + '->'
        path = distances[path][1]
    path_output += start
    print (path_output)
    return distances


n = int(sys.stdin.readline())
m = int(sys.stdin.readline())
graph = defaultdict(dict)
for _ in range(m):
    depart, goal, cost = sys.stdin.readline().split()
    cost = int(cost)
    graph[depart][goal] = cost
departure, arrive = sys.stdin.readline().split()

dijkstra(graph, departure, arrive)
