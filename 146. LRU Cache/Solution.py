class LRUCache:

    def __init__(self, capacity: int):
        self.myDict = OrderedDict()
        self.counter, self.limit = 0, capacity
        
    def get(self, key: int) -> int:
        if(key in self.myDict):
            ret = self.myDict[key]
            self.myDict.pop(key)
            self.myDict[key] = ret
            return(ret)
        else:
            return(-1)

    def put(self, key: int, value: int) -> None:
        if(key in self.myDict):
            self.myDict.pop(key)
            self.myDict[key] = value
        elif(self.counter == self.limit):
            remove = next(iter(self.myDict.keys()))
            self.myDict.pop(remove)
            self.myDict[key] = value
        else:
            self.myDict[key] = value
            self.counter += 1
        return()