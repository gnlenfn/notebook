import collections

class Solution:
    def numJewelsInStones(self, jewels: str, stones: str) -> int:
        answer = collections.defaultdict(int)
        for s in stones:
            if s in jewels:
                answer[s] += 1
        
        return sum(answer.values())