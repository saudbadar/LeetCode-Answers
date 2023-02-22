class Solution:
    def isPerfectSquare(self, num: int) -> bool:
        left, right = 1, num
        while(left <= right):
            middle = (left + right) // 2
            val = pow(middle, 2)
            if(val == num):
                return(True)
            elif(val > num):
                right = middle - 1
            else:
                left = middle + 1
        return(False)