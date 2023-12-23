class Solution:
    def isPathCrossing(self, path: str) -> bool:
        seen, curPos, myDict = set([(0,0)]), [0,0], {"N": [1,0], "S": [-1,0], "E": [0,1], "W": [0,-1]}
        for letter in path:
            curPos[0] += myDict[letter][0]
            curPos[1] += myDict[letter][1]
            if((curPos[0], curPos[1]) in seen):
                return(True)
            seen.add((curPos[0], curPos[1]))
        return(False)