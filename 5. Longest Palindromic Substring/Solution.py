class Solution:
    def longestPalindrome(self, s: str) -> str:
        lengthS, ret = len(s), ""
        
        for idx, letter in enumerate(s):
            left = right = idx
            while((left - 1) >= 0 and (right + 1) < lengthS and s[left - 1] == s[right + 1]):
                left -= 1
                right += 1
            if((right - left + 1) > len(ret)):
                ret = s[left: right + 1]
            if(idx > 0 and s[idx] == s[idx - 1]):
                left, right = idx - 1, idx
                while((left - 1) >= 0 and (right + 1) < lengthS and s[left - 1] == s[right + 1]):
                    left -= 1
                    right += 1
                if((right - left + 1) > len(ret)):
                    ret = s[left: right + 1]
        return(ret)
