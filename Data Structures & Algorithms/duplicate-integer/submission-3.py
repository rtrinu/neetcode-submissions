class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        setted = set(nums)
        if len(nums) > len(setted):
            return True
        return False