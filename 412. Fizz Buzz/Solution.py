class Solution:
    def fizzBuzz(self, n: int) -> List[str]:
        ret = []

        for i in range(1, n + 1):
            threeCheck, fiveCheck = False, False
            if((i % 3) == 0):
                threeCheck = True
            if((i % 5) == 0):
                fiveCheck = True
            
            if(threeCheck and fiveCheck):
                ret.append("FizzBuzz")
            elif(threeCheck):
                ret.append("Fizz")
            elif(fiveCheck):
                ret.append("Buzz")
            else:
                ret.append(str(i))
        return(ret)