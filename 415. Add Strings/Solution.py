class Solution:
    def addStrings(self, num1: str, num2: str) -> str:
        carryOn, ret = 0, ""
        def helperFunction(nums, idx):
            nonlocal carryOn, ret
            for i in reversed(nums[:-idx]):
                temp = ord(i) - 48 + carryOn
                carryOn, add = temp // 10, temp % 10
                ret = str(add) + ret
        
        for valOne, valTwo in zip(reversed(num1), reversed(num2)):
            temp = ord(valOne) + ord(valTwo) - 96 + carryOn
            carryOn, add = temp // 10, temp % 10
            ret = str(add) + ret

        if(len(num1) > len(num2)):
            helperFunction(num1, len(num2))
        elif(len(num2) > len(num1)):
            helperFunction(num2, len(num1))
        if(carryOn):
            ret = str(carryOn) + ret
        return(ret) 