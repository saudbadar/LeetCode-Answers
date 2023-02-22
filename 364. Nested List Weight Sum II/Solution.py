class Solution:
    def depthSumInverse(self, nestedList: List[NestedInteger]) -> int:
        maxDepth, ret = 0, 0
        
        def findDepth(lst, depth):
            nonlocal maxDepth
            if(lst):
                maxDepth = max(maxDepth, depth)
            for tempLst in lst:
                if(not tempLst.isInteger()):
                    findDepth(tempLst.getList(), depth + 1)
        
        def findSum(lst, depth):
            nonlocal ret
            for tempLst in lst:
                if(tempLst.isInteger()):
                    ret += (tempLst.getInteger() * depth)
                else:
                    findSum(tempLst.getList(), depth - 1)
            

        findDepth(nestedList, 1)
        findSum(nestedList, maxDepth)
        return(ret)