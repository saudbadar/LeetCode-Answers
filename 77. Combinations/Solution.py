class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        retList = []
        def backtrack(combo):
            if(len(combo) == k):
                retList.append(combo.copy())
            else:
                if(not combo):
                    start = 1
                else:
                    start = combo[-1] + 1
                for i in range(start, n + 1):
                    combo.append(i)
                    backtrack(combo)
                    combo.remove(i)
        backtrack([])
        return(retList)