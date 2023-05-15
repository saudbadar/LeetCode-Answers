class Solution:
    def calcEquation(self, equations: List[List[str]], values: List[float], queries: List[List[str]]) -> List[float]:
        myDict, ret = defaultdict(dict), []
        for equ, val in zip(equations, values):
            myDict[equ[0]][equ[1]] = val
            myDict[equ[1]][equ[0]] = 1/val
        
        def search(loc, target, visited, val):
            nonlocal ret, insert
            visited.add(loc)
            for newPos, multiple in myDict[loc].items():
                if(newPos == target and not insert):
                    insert = True
                    ret.append(val * multiple)
                if(newPos not in visited):
                    search(newPos, target, visited, val * multiple)
        
        for idx, query in enumerate(queries):
            insert = False
            search(query[0], query[1], set(), 1)
            if(len(ret) != (idx + 1)):
                ret.append(float(-1))
        return(ret)