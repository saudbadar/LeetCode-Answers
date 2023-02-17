class Solution:
    def isHappy(self, n: int) -> bool:
        ret, mySet = n, set()
        while(ret != 1):
            tempRet, placement = ret, 0
            while(tempRet != 0):
                placement += pow((tempRet % 10), 2)
                tempRet //= 10
            tempRet = ret = placement
            if(ret in mySet):
                return(False)
            mySet.add(ret)
        return(True)