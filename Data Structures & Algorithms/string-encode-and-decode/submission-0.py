class Solution:

    def encode(self, strs: List[str]) -> str:

        s = ""
        for st in strs:
            length = len(st)
            s += str(length) + "#" + st
        return s

    def decode(self, s: str) -> List[str]:

        lst = []
        i = 0

        while i < len(s):
            t_lst = []
            num = 0
            while s[i] != "#":
                num = num*10 + int(s[i])
                i += 1
            i += 1
            while num > 0:
                t_lst.append(s[i])
                i += 1
                num -= 1

            word = "".join(t_lst)
            lst.append(word)
        
        return lst
                


