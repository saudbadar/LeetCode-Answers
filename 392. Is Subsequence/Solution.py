class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        pos, lenS = 0, len(s)
        if(not s):
            return(True)
        for letter in t:
            if(letter == s[pos]):
                pos += 1
                if(pos == lenS):
                    return(True)
        return(False) 