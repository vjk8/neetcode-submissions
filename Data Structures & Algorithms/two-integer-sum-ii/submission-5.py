class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        
        lst = []

        left = 0
        right = len(numbers)-1

        while left < right:
            if (numbers[left] + numbers[right]) == target:
                lst.append(left+1)
                lst.append(right+1)
                return lst
            elif (numbers[left] + numbers[right]) < target:
                left += 1
            else:
                right -= 1
        
        return lst