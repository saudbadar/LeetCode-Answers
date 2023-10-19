# """
# This is the interface that allows for creating nested lists.
# You should not implement it, or speculate about its implementation
# """
#class NestedInteger:
#    def isInteger(self) -> bool:
#        """
#        @return True if this NestedInteger holds a single integer, rather than a nested list.
#        """
#
#    def getInteger(self) -> int:
#        """
#        @return the single integer that this NestedInteger holds, if it holds a single integer
#        Return None if this NestedInteger holds a nested list
#        """
#
#    def getList(self) -> [NestedInteger]:
#        """
#        @return the nested list that this NestedInteger holds, if it holds a nested list
#        Return None if this NestedInteger holds a single integer
#        """

class NestedIterator:
    def __init__(self, nestedList: [NestedInteger]):
        self.current, self.lst = 0, []
        self.createList(nestedList)

    def createList(self, nestedList: [NestedInteger]):
        for newLst in nestedList:
            if(newLst.isInteger()):
                self.lst.append(newLst.getInteger())
            else:
                self.createList(newLst.getList())

    def next(self) -> int:
        if(self.current < len(self.lst)):
            ret = self.lst[self.current]
            self.current += 1
            return(ret)
        else:
            return()
        
    def hasNext(self) -> bool:
        if(self.current < len(self.lst)):
            return(True)
        else:
            return(False)
         
# Your NestedIterator object will be instantiated and called as such:
# i, v = NestedIterator(nestedList), []
# while i.hasNext(): v.append(i.next())