from typing import List

# Brute-Force Solution
class Solution:
    def twoSum_brute_force(self, nums: List[int], target: int) -> List[int]:
        for i in range(len(nums)-1):
            for j in range(i+1, len(nums)):
                if nums[i] + nums[j] == target:
                    return [i, j]

# subtract num from target
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        num_maps = {}
        for idx, num in enumerate(nums):
            num_maps[num] = idx
            
        for idx, num in enumerate(nums):
            if target - num in num_maps and num_maps[target - num] != idx:
                return idx, num_maps[target-num]

"""
Brute force solution is expected time consuming, but it only takes 48ms on LeetCode.
While the other solution takes 52ms.
"""