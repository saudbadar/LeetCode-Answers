class Solution:
    def removeStars(self, s: str) -> str:
        ret = []
        for letter in s:
            if(letter == "*"):
                ret.pop()
            else:
                ret.append(letter)
        return(''.join(ret))