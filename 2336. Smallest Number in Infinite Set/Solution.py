class SmallestInfiniteSet:

    def __init__(self):
        self.heap, self.minVal = [], 1

    def popSmallest(self) -> int:
        if(self.heap):
            return(heapq.heappop(self.heap))
        else:
            self.minVal += 1
            return(self.minVal - 1)
    

    def addBack(self, num: int) -> None:
        if(num < self.minVal and num not in self.heap):
            heapq.heappush(self.heap, num)