class Solution:
    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:
        lengthOne, lengthTwo, mySet = len(s1), len(s2), set()
        if(lengthOne + lengthTwo != len(s3)): 
            return(False)
        
        def backtracking(posOne, posTwo, loc):
            nonlocal mySet
            if(loc == len(s3)):
                return(True)
            if(posOne < len(s1) and s1[posOne] == s3[loc] and (posOne, posTwo, loc) not in mySet):
                if(backtracking(posOne + 1, posTwo, loc + 1)):
                    return(True)
            if(posTwo < len(s2) and s2[posTwo] == s3[loc] and (posOne, posTwo, loc) not in mySet):
                if(backtracking(posOne, posTwo + 1, loc + 1)):
                    return(True)
            mySet.add((posOne, posTwo, loc))
            return(False)
        return(backtracking(0,0,0))