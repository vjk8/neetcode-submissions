class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        seen = set(nums)
        starts = set()
        
        for elm in seen:
            if (elm - 1) not in seen:
                starts.add(elm)
        
        max_size = 0
        for elm in starts:
            curr_size = 1
            while (elm+1) in seen:
                curr_size += 1
                elm = elm + 1
            if curr_size > max_size:
                max_size = curr_size
        
        return max_size


