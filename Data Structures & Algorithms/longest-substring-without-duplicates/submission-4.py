class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        
        left = 0
        right = 0
        maxx = 0
        count = 0
        seen = set()

        while right < len(s):
            elm = s[right]
            if elm in seen:
                while s[left] != elm:
                    seen.remove(s[left])
                    left += 1
                    count -= 1
                left += 1
            else:
                count += 1
            seen.add(elm)
            if count > maxx:
                maxx = count
                print(s[left:right])
            right += 1
        
        return maxx

        