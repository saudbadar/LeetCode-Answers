class Solution:
    def knightDialer(self, n: int) -> int:
        nextMove = {1: (6,8), 2: (7,9), 3: (4,8), 4: (3,9,0), 5: (), 6: (1,7,0), 7: (2,6), 8: (1,3),
        9: (2,4), 0: (4,6)}
        curMove = {1: 1, 2: 1, 3: 1, 4: 1, 5: 1, 6: 1, 7: 1, 8: 1, 9: 1, 0: 1}

        for i in range(1, n):
            tempDict = {1: 0, 2: 0, 3: 0, 4: 0, 5: 0, 6: 0, 7: 0, 8: 0, 9: 0, 0: 0}
            for j in range(10):
                for z in nextMove[j]:
                    tempDict[z] += curMove[j]
            curMove = tempDict
        return(sum(curMove.values()) % (10**9 + 7))