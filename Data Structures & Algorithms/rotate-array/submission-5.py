class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """

        # swap and keep a modula counter
        n = len(nums)
        new_lst = [0 for _ in range(n)]


        for i in range(n):
            new_lst[(i+k)%n] = nums[i]
        
        nums[:] = new_lst