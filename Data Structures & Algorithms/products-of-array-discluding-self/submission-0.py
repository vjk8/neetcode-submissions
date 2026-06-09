class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        
        prefix = [1 for _ in range(len(nums))]
        cummulative = 1

        for i in range(0, len(nums)-1):
            cummulative = cummulative * nums[i]
            prefix[i+1] = cummulative
        
        cummulative = 1
        for i in range(len(nums)-1, 0, -1):
            cummulative = cummulative * nums[i]
            prefix[i-1] = prefix[i-1] * cummulative
        
        return prefix