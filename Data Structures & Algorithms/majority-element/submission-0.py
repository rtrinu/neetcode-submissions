class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        nums = sorted(nums)
        middle = nums[len(nums)//2]
        return middle