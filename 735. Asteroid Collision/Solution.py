class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        leftLst, ret = [], []

        for num in asteroids:
            if(num < 0):
                if(leftLst):
                    absVal, add = abs(num), True
                    while(leftLst):
                        if(leftLst[-1] > absVal):
                            break
                        elif(leftLst[-1] < absVal):
                            leftLst.pop()
                        else:
                            leftLst.pop()
                            add = False
                            break
                    if(not leftLst and add):
                        ret.append(num)
                else:
                    ret.append(num)
            else:
                leftLst.append(num)
        return(ret + leftLst)
                    