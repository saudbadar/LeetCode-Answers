class Solution:
    def lexicalOrder(self, n: int) -> List[int]:
        ret = []

        def recursion(val):
            for i in range(10):
                tempVal = val + i
                if(tempVal <= n):
                    ret.append(tempVal)
                if((tempVal * 10) <= n and tempVal != 0):
                    recursion(tempVal * 10)
        recursion(0)      
        return(ret[1:])