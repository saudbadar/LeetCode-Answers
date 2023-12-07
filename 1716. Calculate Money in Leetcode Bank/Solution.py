class Solution:
    def totalMoney(self, n: int) -> int:
      prevVal, nextWeek, ret = 0, 0, 0
      for i in range(n):
        if((i % 7) == 0):
          prevVal = nextWeek
          nextWeek += 1
        prevVal += 1
        ret += prevVal
      return(ret)