class Solution:
    def removeDuplicateLetters(self, s: str) -> str:
        lastPos, visited, lst = {}, set(), []
        
        for idx, letter in enumerate(s):
            lastPos[letter] = idx
        
        for idx, letter in enumerate(s):
            if(letter in visited):
                continue
            while(lst and lst[-1] > letter and lastPos[lst[-1]] > idx):
                visited.remove(lst.pop())
            visited.add(letter)
            lst.append(letter)
        return("".join(lst))