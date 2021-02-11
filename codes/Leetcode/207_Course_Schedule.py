from typing import List
import collections

class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        graph = collections.defaultdict(list)
        for x, y in prerequisites:
            graph[x].append(y)
            
        visited = set()
        traced  = set()
        
        def dfs(c):
            if c in traced:
                return False
            
            if c in visited:
                return True
            
            traced.add(c)
            for t in graph[c]:
                if not dfs(t):
                    return False
            
            traced.remove(c)
            visited.add(c)
            
            return True
        
        for x in list(graph):
            if not dfs(x):
                return False
        return True

"""
그래프의 순환이 있으면 False를 반환하도록 하는 문제
1. 인접리스트로 그래프 만들기
2. traced -> 이미 방문한 노드 표시(순환 판별용) / visited -> 이미 방문한 노드 표시(가지치기 용)

"""