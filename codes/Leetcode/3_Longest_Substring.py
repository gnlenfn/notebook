class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if not s:
            return 0
        start = max_length = 0
        used = dict()
        
        for idx, char in enumerate(s):
            if char in used and start <= used[char]:
                start = used[char] + 1
            else:
                max_length = max(max_length, idx - start + 1)
            
            used[char] = idx
            
        return max_length