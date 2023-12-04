class Solution:
    def largestGoodInteger(self, num: str) -> str:
        maxVal, ret = -1, ""
        for i in range(len(num) - 2):
            if(num[i] == num[i + 1] and num[i + 1] == num[i + 2]):
                tempVal = int(num[i: i + 3])
                if(maxVal < tempVal):
                    maxVal, ret = tempVal, num[i: i + 3]
        return(ret)
        