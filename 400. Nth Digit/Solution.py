class Solution:
    def findNthDigit(self, n: int) -> int:
        digit, count, pos = 1, 9, 1

        while((count * digit) < n):
            n -= (count * digit)
            count *= 10
            digit += 1
            pos *= 10
        
        pos += (n - 1) // digit
        pos = str(pos)
        return(int(pos[(n - 1) % digit]))