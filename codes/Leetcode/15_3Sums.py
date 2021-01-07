from typing import List

class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums = sorted(nums)
        result = []
        for i in range(len(nums)-2):
            # 중복제거
            if i > 0 and nums[i] == nums[i-1]:
                continue
                
            # 세 수의 합
            left, right = i + 1, len(nums) - 1
            while left < right:
                sums = nums[i] + nums[left] + nums[right]
                if sums < 0:
                    left += 1
                elif sums > 0:
                    right -= 1
                else:
                    result.append((nums[i], nums[left], nums[right]))
                    
                    while left < right and nums[left] == nums[left + 1]:
                        left += 1
                    while left < right and nums[right] == nums[right - 1]:
                        right -= 1
                    
                    left += 1
                    right -= 1
        return result
        