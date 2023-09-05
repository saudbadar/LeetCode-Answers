class Solution:
    def validWordSquare(self, words: List[str]) -> bool:
        lenWord = len(words)
        for idx, word in enumerate(words):
            if(len(word) > lenWord):
                return(False)
            for newIdx in range(len(word)):
                newWord = words[newIdx]
                if(len(newWord) <= idx or word[newIdx] != words[newIdx][idx]):
                    return(False)
        return(True)
        