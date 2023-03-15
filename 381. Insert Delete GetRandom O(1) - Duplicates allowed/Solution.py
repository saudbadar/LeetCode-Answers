class RandomizedCollection:

    def __init__(self):
        self.myDict, self.lst = collections.defaultdict(set), []
        

    def insert(self, val: int) -> bool:
        if(val in self.myDict):
            ret = False
        else:
            ret = True
        self.myDict[val].add(len(self.lst))
        self.lst.append(val)
        return(ret)

    def remove(self, val: int) -> bool:
        if(val in self.myDict):
            lastVal, removeIdx = self.lst[-1], next(iter(self.myDict[val]))
            if(lastVal == val):
                self.myDict[val].remove(len(self.lst) - 1)
            else:
                self.myDict[val].remove(removeIdx)
                self.myDict[lastVal].remove(len(self.lst) - 1)
                self.myDict[lastVal].add(removeIdx)
                self.lst[removeIdx] = lastVal
            self.lst.pop()
            if(not self.myDict[val]):
                del self.myDict[val]
            return(True)
        else:
            return(False)
        

    def getRandom(self) -> int:
        return(choice(self.lst))