class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        
        nums = sorted(nums)
        lst = []

        i = 0

        while i < (len(nums)-2):
            target = -nums[i]
            left = i+1
            right = len(nums)-1
            while left < right:
                if (nums[left] + nums[right]) == target:
                    lst.append([nums[i], nums[left], nums[right]])
                    left += 1
                    right -= 1
                    while left < right and nums[left] == nums[left-1]:
                        left += 1
                    while right > left and nums[right] == nums[right+1]:
                        right -= 1
                elif (nums[left] + nums[right]) < target:
                    left += 1
                else:
                    right -= 1
            
            i += 1
            while i < (len(nums)-2) and nums[i] == nums[i-1]:
                i += 1
        
        return lst