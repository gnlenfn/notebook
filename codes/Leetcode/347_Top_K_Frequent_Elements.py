from typing import List
import collections
import heapq

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq = collections.Counter(nums)
        heap = []
        
        for f in freq:
            heapq.heappush(heap, (-freq[f], f))
        
        topk = []
        for _ in range(k):
            topk.append(heapq.heappop(heap)[1])
        
        return topk


    def pythonic(self,  nums: List[int], k: int) -> List[int]:
        return list(zip(*collections.Counter(nums).most_common(k)))[0]