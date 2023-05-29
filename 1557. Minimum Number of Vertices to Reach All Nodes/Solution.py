class Solution:
    def findSmallestSetOfVertices(self, n: int, edges: List[List[int]]) -> List[int]:
        mySet = set(range(n))
        for fromNode, toNode in edges:
            if(toNode in mySet):
                mySet.remove(toNode)
        return(list(mySet))