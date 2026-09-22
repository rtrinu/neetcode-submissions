class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        seen = {}
        output = []
        for num in nums:
            if num not in seen:
                seen[num] = 0
            seen[num]+= 1
        seen = sorted(seen.items(), key=lambda x:x[1], reverse=True)
        for i in range(k):
            output.append(seen[i][0])
        return output