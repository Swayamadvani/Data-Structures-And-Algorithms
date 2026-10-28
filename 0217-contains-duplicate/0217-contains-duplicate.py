class Solution:
    def containsDuplicate(self, nums: list[int]) -> bool:
        x = set()
        for i in range(len(nums)):
            if nums[i] in x:
                return True
            else:
                x.add(nums[i])
        return False