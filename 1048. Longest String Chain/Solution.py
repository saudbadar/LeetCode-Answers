class Solution:
    def longestStrChain(self, words: List[str]) -> int:
        myDict = {}
        for word in sorted(words, key=len):
            myDict[word] = 0
            for i in range(len(word)):
                myDict[word] = max(myDict.get(word[:i] + word[i + 1:], 0) + 1, myDict[word])
        return(max(myDict.values()))