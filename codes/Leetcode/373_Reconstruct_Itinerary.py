from typing import List
from collections import defaultdict, deque

class Solution:
    def findItinerary(self, tickets: List[List[str]]) -> List[str]:
        graph = defaultdict(lambda: deque())
        
        for depart, arrive in tickets:
            graph[depart].append(arrive)

        route = []
        def dfs(city):
            while graph[city]:
                dfs(graph[city].popleft())
            route.append(city)
        
        dfs("JFK")
        
        return route[::-1]

"""
1. 주어진 input에 맞게 그래프를 그린다.
2. 인접리스트 형태로 그래프를 그렸고, 딕셔너리형태로 생성함
3. dfs 함수의 인자로 인접리스트의 좌측부터 대입
4. 가장 최근에 도착하는 공항부터 route에 append 된다.
5. route를 역순으로 반환
"""