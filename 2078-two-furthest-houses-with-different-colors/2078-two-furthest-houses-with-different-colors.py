from typing import List

class Solution:
    def maxDistance(self, colors: List[int]) -> int:
        n = len(colors)
        ans = 0
        
        # Check from the start to find different colors
        for i in range(n):
            if colors[i] != colors[0]:
                ans = max(ans, i)
            if colors[n - 1 - i] != colors[-1]:
                ans = max(ans, i)
        
        return ans
           # Output: 1
