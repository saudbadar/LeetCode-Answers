class Solution:
    def maxVowels(self, s: str, k: int) -> int:
        ret, myDict = 0, {'a', 'e', 'i', 'o', 'u'}
        for i in range(k):
            if(s[i] in myDict):
                ret += 1
        ans = ret
        for i in range(k, len(s)):
            if(s[i - k] in myDict):
                ret -= 1
            if(s[i] in myDict):
                ret += 1
            ans = max(ret, ans)
        return(ans)