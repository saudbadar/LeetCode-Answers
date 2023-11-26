class Solution:
    def sortVowels(self, s: str) -> str:
        lst, vowel, ret = [], set(['a','e','i','o','u','A','E','I','O','U']), ""
        for letter in s:
            if(letter in vowel):
                lst.append(ord(letter))
        lst.sort(reverse=True)
        for letter in s:
            if(letter in vowel):
                ret += chr(lst.pop())
            else:
                ret += letter
        return(ret)