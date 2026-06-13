class Solution:
    def maxArea(self, heights: List[int]) -> int:
        # amount of water = height of shorter * dist between 2

        amount = 0
        left = 0
        right = len(heights)-1

        while left < right:
            curr_amount = (right - left) * min(heights[left], heights[right])
            if curr_amount > amount:
                amount = curr_amount
            
            if heights[left] < heights[right]:
                left += 1
            else:
                right -= 1
        
        return amount