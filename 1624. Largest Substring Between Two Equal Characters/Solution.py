class Solution:
    def maxLengthBetweenEqualCharacters(self, s: str) -> int:
        myDict, ret = {}, -1
        for idx, letter in enumerate(s):
            if(letter in myDict):
                ret = max(ret, idx - myDict[letter] - 1)
            else:
                myDict[letter] = idx
        return(ret)