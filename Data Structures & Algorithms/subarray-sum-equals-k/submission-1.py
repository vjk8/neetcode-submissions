class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        
        count = 0
        prefix_sums = {0: 1}
        cummulative = 0

        for i in range(len(nums)):
            cummulative += nums[i]
            if (cummulative - k) in prefix_sums:
                count += prefix_sums[cummulative - k]
            
            prefix_sums[cummulative] = prefix_sums.get(cummulative, 0) + 1
        
        return count