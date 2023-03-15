class RandomizedSet:

    def __init__(self):
        self.myDict, self.lst = {}, []
        

    def insert(self, val: int) -> bool:
        if(val not in self.myDict):
            self.myDict[val] = len(self.lst)
            self.lst.append(val)
            return(True)
        else:
            return(False)
        

    def remove(self, val: int) -> bool:
        if(val in self.myDict):
            lastVal, removeIdx = self.lst[-1], self.myDict[val]
            self.lst[removeIdx], self.myDict[lastVal] = lastVal, removeIdx
            self.lst.pop()
            del self.myDict[val]
            return(True)
        else:
            return(False)
        

    def getRandom(self) -> int:
        return(choice(self.lst))