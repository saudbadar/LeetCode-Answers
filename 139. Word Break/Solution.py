class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        queue, mySet, finalLength = deque([0]), set(), len(s)
        mySet.add(0)

        while(queue):
            idx = queue.popleft()
            if(idx == finalLength):
                return(True)
            for word in wordDict:
                length = len(word)
                if(s[idx:idx + length] == word and (idx + length) not in mySet):
                    queue.append(idx + length)
                    mySet.add(idx + length)
        return(False)