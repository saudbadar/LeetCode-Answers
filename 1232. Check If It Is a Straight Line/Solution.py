class Solution:
    def checkStraightLine(self, coordinates: List[List[int]]) -> bool:
        if(coordinates[1][0] == coordinates[0][0]):
            for coordinate in coordinates[2:]:
                if(coordinate[0] != coordinates[0][0]):
                    return(False)
            return(True)
        
        slope = (coordinates[1][1] - coordinates[0][1])/(coordinates[1][0] - coordinates[0][0])
        prevX, prevY = coordinates[1][0], coordinates[1][1]
        for coordinate in coordinates[2:]:
            distX = coordinate[0] - prevX
            newY = prevY + (slope * distX)
            if(coordinate[1] != newY):
                return(False)
        return(True)