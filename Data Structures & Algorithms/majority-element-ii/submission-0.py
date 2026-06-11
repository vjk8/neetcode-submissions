class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:

        count = len(nums)/3
        ht = {}
        ret = set()

        for num in nums:
            ht[num] = ht.get(num, 0) + 1
            if ht[num] > count:
                ret.add(num)

        lst = []

        for elm in ret:
            lst.append(elm)
        return lst
        