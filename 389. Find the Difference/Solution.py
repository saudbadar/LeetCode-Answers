class Solution:
    def findTheDifference(self, s: str, t: str) -> str:
        ret = 0
        for letter in s:
            ret ^= ord(letter)
        for letter in t:
            ret ^= ord(letter)
        return(chr(ret))