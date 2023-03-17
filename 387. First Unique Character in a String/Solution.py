class Solution:
    def firstUniqChar(self, s: str) -> int:
        myDict, mySet = {}, set()
        for idx, letter in enumerate(s):
            if(letter not in myDict):
                if(letter not in mySet):
                    myDict[letter] = idx
            else:
                del myDict[letter]
                mySet.add(letter)
        return(-1 if not myDict else next(iter(myDict.values())))