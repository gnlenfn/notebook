from typing import List

class Solution:
    def dailyTemperatures(self, T: List[int]) -> List[int]:
        stack = []
        result = [0] * len(T)
        days = 0
        for idx, current in enumerate(T):
            while stack and T[stack[-1]] < current:
                last = stack.pop()
                result[last] = idx - last
            stack.append(idx)
        
        return result