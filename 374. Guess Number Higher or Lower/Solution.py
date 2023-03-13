class Solution:
    def guessNumber(self, n: int) -> int:
        left, right = 0, n
        while(left <= right):
            middle = (left + right) // 2
            val = guess(middle)
            if(val > 0):
                left = middle + 1
            elif(val < 0):
                right = middle - 1
            else:
                break
        return(middle)