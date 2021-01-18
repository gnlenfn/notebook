import collections
# Stack solution
class Solution:
    def removeDuplicateLetters(self, s: str) -> str:
        count, seen, stack = collections.Counter(s), set(), []
        for char in s:
            count[char] -= 1
            if char in stack:
                continue
            
            while stack and char < stack[-1] and count[stack[-1]] > 0:
                seen.remove(stack.pop())
            stack.append(char)
            seen.add(char)
            
        return "".join(stack)


