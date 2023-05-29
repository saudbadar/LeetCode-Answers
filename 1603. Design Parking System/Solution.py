class ParkingSystem:

    def __init__(self, big: int, medium: int, small: int):
        self.lst = [[], [0, big], [0, medium], [0, small]]
        

    def addCar(self, carType: int) -> bool:
        if(self.lst[carType][0] == self.lst[carType][1]):
            return(False)
        else:
            self.lst[carType][0] += 1
            return(True)
        