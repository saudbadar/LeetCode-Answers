class Solution:
    def rangeBitwiseAnd(self, left: int, right: int) -> int:
        leftVal, rightVal = bin(left), bin(right)
        if(len(leftVal) != len(rightVal)):
            return(0)
        ret = ""
        for valOne, valTwo in zip(leftVal[2:], rightVal[2:]):
            if(valOne == valTwo):
                ret +=  valOne
            else:
                break
        for _ in range(len(ret), len(leftVal) - 2):
            ret += '0'
        return(int(ret, 2))