class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        hashset = set(nums)
        longest = 0
        for n in hashset:
            if n-1 not in hashset:
                beg = n
                count = 1
                while beg+1 in hashset:
                    beg+=1
                    count+=1
                longest= max(longest,count)
        return longest
