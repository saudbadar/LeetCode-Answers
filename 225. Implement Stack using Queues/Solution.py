class MyStack:

    def __init__(self):
        self.queue = deque()

    def push(self, x: int) -> None:
        self.queue.append(x)

    def pop(self) -> int:
        if(self.queue):
            return(self.queue.pop())
        return()

    def top(self) -> int:
        if(self.queue):
            return(self.queue[-1])
        return(None)

    def empty(self) -> bool:
        if(self.queue):
            return(False)
        return(True)