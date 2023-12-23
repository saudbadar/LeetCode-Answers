class Solution:
    def maxScore(self, s: str) -> int:
        numOfOnes, numOfZeros, ret = s[1:].count("1"), 1 if s[0] == "0" else 0, 0
        for letter in s[1: len(s) - 1]:
            ret = max(ret, numOfZeros + numOfOnes)
            if(letter == "0"):
                numOfZeros += 1
            else:
                numOfOnes -= 1
        return(max(ret, numOfZeros + numOfOnes))