class Solution:
    def largestOddNumber(self, num: str) -> str:
      length = len(num)
      for idx in range(length - 1, -1 , -1):
        if((int(num[idx]) % 2) != 0):
          return(num[:idx + 1])
      return("")
