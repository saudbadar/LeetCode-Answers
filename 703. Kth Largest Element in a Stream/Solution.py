class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        self.heap, self.length = [], k
        for num in nums:
            if(len(self.heap) < k):
                heapq.heappush(self.heap, num)
            elif(self.heap[0] < num):
                heapq.heapreplace(self.heap, num)
        

    def add(self, val: int) -> int:
        if(len(self.heap) < self.length):
            heapq.heappush(self.heap, val)
        elif(self.heap[0] < val):
            heapq.heapreplace(self.heap, val)
        return(self.heap[0])