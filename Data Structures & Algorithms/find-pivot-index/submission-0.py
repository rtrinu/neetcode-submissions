class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        prefix, postfix = [0] * len(nums), [0] * len(nums)
        prefix_total,postfix_total = 0,0
        for i in range(len(nums)):
            prefix[i] = prefix_total
            prefix_total+=nums[i]
        for i in range(len(nums)-1, -1,-1):
            postfix[i] = postfix_total
            postfix_total+=nums[i]
       
        for i in range(len(nums)):
            if prefix[i] == postfix[i]:
                return i
        return -1

        

        
