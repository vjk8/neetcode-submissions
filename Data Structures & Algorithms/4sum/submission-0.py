class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        n = len(nums)
        nums.sort()
        lst = []
        i = 0

        while i < len(nums):
            first = nums[i]
            j = i+1
            while j < len(nums):
                second = nums[j]
                left = j+1
                right = n-1

                while left < right:
                    third = nums[left]
                    fourth = nums[right]

                    if (first + second+ third +fourth) == target:
                        lst.append([first, second, third, fourth])
                        left += 1
                        right -= 1
                        while left < right and nums[left] == nums[left-1]:
                            left += 1
                        while right > left and nums[right] == nums[right+1]:
                            right -= 1
                    elif (first + second+ third +fourth) < target:
                        left += 1
                    else:
                        right -= 1
                j += 1
                while j < (len(nums)-2) and nums[j] == nums[j-1]:
                    j += 1
            
            i += 1
            while i < (len(nums)-3) and nums[i] == nums[i-1]:
                i += 1
        
        return lst


        