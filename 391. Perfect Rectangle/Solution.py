class Solution:
    def isRectangleCover(self, rectangles: List[List[int]]) -> bool:
        area, mySet = 0, set()
        lowestX, lowestY, highestX, highestY = sys.maxsize, sys.maxsize, -sys.maxsize, -sys.maxsize

        for rectangle in rectangles:
            lowestX, lowestY = min(lowestX, rectangle[0]), min(lowestY, rectangle[1])
            highestX, highestY = max(highestX, rectangle[2]), max(highestY, rectangle[3])

            area += ((rectangle[2] - rectangle[0]) * (rectangle[3] - rectangle[1]))

            if((rectangle[0], rectangle[1]) not in mySet):
                mySet.add((rectangle[0], rectangle[1]))
            else:
                mySet.remove((rectangle[0], rectangle[1]))
            if((rectangle[0], rectangle[3]) not in mySet):
                mySet.add((rectangle[0], rectangle[3]))
            else:
                mySet.remove((rectangle[0], rectangle[3]))
            if((rectangle[2], rectangle[1]) not in mySet):
                mySet.add((rectangle[2], rectangle[1]))
            else:
                mySet.remove((rectangle[2], rectangle[1]))
            if((rectangle[2], rectangle[3]) not in mySet):
                mySet.add((rectangle[2], rectangle[3]))
            else:
                mySet.remove((rectangle[2], rectangle[3]))
        if((lowestX, lowestY) not in mySet or (lowestX, highestY) not in mySet or (highestX, lowestY) not in mySet or (highestX, highestY) not in mySet or len(mySet) != 4):
            return(False)
        return(True if area == ((highestX - lowestX) * (highestY - lowestY)) else False)