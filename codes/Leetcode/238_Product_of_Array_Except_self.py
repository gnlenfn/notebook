from typing import List
class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        out = []
        result = 1
        for i in range(len(nums)):
            out.append(result)
            result = result * nums[i]
        
        tmp = 1
        for i in range(len(nums)-1, -1, -1):
            out[i] = out[i] * tmp
            tmp = tmp * nums[i]
        return out
            