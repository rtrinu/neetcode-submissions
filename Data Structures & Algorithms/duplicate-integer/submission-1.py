class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        values = set(nums)
        if len(values) < len(nums):
            return True
        else:
            return False