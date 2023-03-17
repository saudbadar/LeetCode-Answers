class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        countRansom = Counter(ransomNote)
        for letter in magazine:
            if(letter in countRansom):
                countRansom[letter] -= 1
                if(countRansom[letter] == 0):
                    del countRansom[letter]
        return(False if countRansom else True)