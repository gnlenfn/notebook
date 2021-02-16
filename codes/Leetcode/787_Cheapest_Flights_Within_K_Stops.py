class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, K: int) -> int:
        graph = collections.defaultdict(list)
        for u, v, w in flights:
            graph[u].append((v, w))
        
        queue = [(0, src, K)]
        
        while queue:
            price, node, k = heapq.heappop(queue)
            if node == dst:
                return price
            if k >= 0:
                for v, w in graph[node]:
                    alt = price + w
                    heapq.heappush(queue, (alt, v, k-1))
            
        return -1

"""
K번 안에 도착해야 하므로, 첫 노드에 K를 저장하고 이동할때마다 1씩 뺀다
"""