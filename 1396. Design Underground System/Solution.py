class UndergroundSystem:

    def __init__(self):
        self.myDict = {}
        self.inOut = {}
        

    def checkIn(self, id: int, stationName: str, t: int) -> None:
        self.inOut[id] = (stationName, t)

    def checkOut(self, id: int, stationName: str, t: int) -> None:
        startLoc, startTime = self.inOut[id]
        self.inOut.pop(id)
        diff = t - startTime
        if((startLoc, stationName) not in self.myDict):
            self.myDict[(startLoc, stationName)] = [1, diff]
        else:
            self.myDict[(startLoc, stationName)][0] += 1
            self.myDict[(startLoc, stationName)][1] += diff

    def getAverageTime(self, startStation: str, endStation: str) -> float:
        return(self.myDict[(startStation, endStation)][1]/self.myDict[(startStation, endStation)][0])