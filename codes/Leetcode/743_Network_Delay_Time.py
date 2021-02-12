from typing import List
import collections, heapq

class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        graph = collections.defaultdict(list)
        for u, v, w in times:
            graph[u].append((v, w))
            
        queue = [(0, k)]
        dist = collections.defaultdict(int) # time for each vertex
        
        while queue:
            time, node = heapq.heappop(queue)
            if node not in dist: 
                dist[node] = time
                for v, w in graph[node]:
                    alt = time + w
                    heapq.heappush(queue, (alt, v))
                    
        if len(dist) == n:
            return max(dist.values())
        
        return -1
        

"""
6-11 lines 
--> 인접리스트로 그래프 만들기
--> dist는 각 정점까지 도달하는 시간을 저장

15 line
--> BFS 순회 하면서 다익스트라 진행
--> queue가 우선순위큐 이므로 (최소힙) 시간이 작은 순서대로 pop 될것
    따라서 dist에 들어있는 정점은 항상 최소 시간으로 값이 정해져있음
    --> dist에 없는 node만 진행

21 line
--> dist.values() (각 정점까지 걸리는 시간) 중 최대값을 찾으면 모든 정점이 도달하는 시간 반환
그 길이가 전체 정점 수와 일치하지 않으면 도달하지 못한 정점이 있다는 것이므로 -1 반환
"""