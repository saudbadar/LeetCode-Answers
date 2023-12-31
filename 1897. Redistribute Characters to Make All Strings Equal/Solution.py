class Solution:
    def makeEqual(self, words: List[str]) -> bool:
        myDict, length = defaultdict(int), len(words)

        for word in words:
            for letter in word:
                myDict[letter] = myDict.get(letter, 0) + 1
        
        for val in myDict.values():
            if(val % length != 0):
                return(False)
        return(True)