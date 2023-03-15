class PhoneDirectory:

    def __init__(self, maxNumbers: int):
        self.mySet = set()
        for i in range(maxNumbers):
            self.mySet.add(i)
        

    def get(self) -> int:
        if(self.mySet):
            return(self.mySet.pop())
        else:
            return(-1)
        

    def check(self, number: int) -> bool:
        if(number in self.mySet):
            return(True)
        else:
            return(False)
        

    def release(self, number: int) -> None:
        self.mySet.add(number)