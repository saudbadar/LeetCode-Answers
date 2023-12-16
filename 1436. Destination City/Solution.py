class Solution:
    def destCity(self, paths: List[List[str]]) -> str:
        startAdd, destAdd = set(), set()
        for startLoc, endLoc in paths:
            startAdd.add(startLoc)
            if(startLoc in destAdd):
                destAdd.remove(startLoc)
            if(endLoc not in startAdd):
                destAdd.add(endLoc)
        return(destAdd.pop())