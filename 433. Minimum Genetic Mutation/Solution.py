class Solution:
    def minMutation(self, startGene: str, endGene: str, bank: List[str]) -> int:
        setBank, ret, visited = set(bank), sys.maxsize, set()
        if(endGene not in setBank):
            return(-1)
        
        def backtrack(depth, word):
            nonlocal ret, visited
            if(depth > ret):
                return()
            if(word == endGene):
                ret = min(depth, ret)
                return()
            newWord = ""
            for idx in range(len(word)):
                for letter in ['A', 'C', 'G', 'T']:
                    tempWord = newWord + letter + word[idx + 1:]
                    if(tempWord in setBank and tempWord not in visited):
                        visited.add(tempWord)
                        backtrack(depth + 1, tempWord)
                        visited.remove(tempWord)
                newWord += word[idx]
                
        backtrack(0, startGene)
        return(ret if ret is not sys.maxsize else -1)