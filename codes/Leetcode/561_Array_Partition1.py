from typing import List

class Solution:
    def arrayPairSum(self, nums: List[int]) -> int:
        return sorted(nums)[::2]
        