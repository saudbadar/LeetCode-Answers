class Solution:
    def reverseWords(self, s: str) -> str:
        lst, ret = s.split(), ""
        for word in lst:
            ret += (word[::-1] + " ")
        return(ret[:-1])