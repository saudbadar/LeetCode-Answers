class HitCounter:

    def __init__(self):
        self.queue = collections.deque()
        

    def hit(self, timestamp: int) -> None:
        self.queue.append(timestamp)
        while((self.queue[-1] - self.queue[0]) > 300):
            self.queue.popleft()

    def getHits(self, timestamp: int) -> int:
        while(self.queue and (timestamp - self.queue[0]) >= 300):
            self.queue.popleft()
        return(len(self.queue))