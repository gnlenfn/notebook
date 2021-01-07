from typing import List

class Solution:
    def trap(self, height: List[int]) -> int:
        volume = 0
        stack = []
        for h in range(len(height)):            
            while stack and height[h] > height[stack[-1]]:
                top = stack.pop()
                if not stack:
                    break
                
                distance = h - stack[-1] - 1
                water = min(height[h], height[stack[-1]]) - height[top]
                volume += distance * water
            stack.append(h)
        
        return volume